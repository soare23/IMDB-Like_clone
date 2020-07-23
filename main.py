from flask import Flask, render_template, url_for, request, redirect, jsonify
from data import queries
import math
from dotenv import load_dotenv
from data import data_manager
import requests
import json
import datetime


load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows/most-rated/<int:page>', methods=["GET", "POST"])
def most_rated(page):
    counter = 0
    headers = data_manager.SHOWS_HEADERS
    order_by = request.args.get('order_by')
    order = request.args.get('order')
    last_page_data = queries.get_max_page()
    last_page = math.ceil(last_page_data[0]['last_page']/15)
    for element in range(0, last_page):
        if page == element:
            counter = element * 15
            if order_by:
                shows = queries.get_most_rated_shows(order_by, order, counter)
            else:
                shows = queries.get_most_rated_shows(2, "ASC", counter)
            current_page = page
            return render_template('shows.html', headers=headers, shows=shows, current_page=current_page)


@app.route('/show/<id>', methods=["GET", "POST"])
def show_details(id):
    show_actors = queries.get_actors_by_show_id(id)
    seasons_data = queries.get_seasons_data_by_id(id)
    show_details = queries.get_show_details(id)
    show_genre = queries.get_show_genre_by_id(id)
    return render_template('show-details.html', show_details=show_details, genres=show_genre, actors=show_actors, seasons=seasons_data)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
