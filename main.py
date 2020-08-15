from flask import Flask, render_template, url_for, request, redirect, jsonify, flash, session, escape
from data import queries
import math
from dotenv import load_dotenv
from data import data_manager
import requests
import json
import datetime
import util

load_dotenv()
app = Flask('codecool_series')
app.config["SECRET_KEY"] = 'UF9y5KFUzcgGsYCG4ZsslQ'


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
    print(show_actors)
    return render_template('show-details.html', show_details=show_details, genres=show_genre, actors=show_actors, seasons=seasons_data)


@app.route('/register', methods=["GET", "POST"])
def register():
    session['status'] = 0
    if request.method == "POST":
        # result = request.get_json()
        # username = result['username']
        # password = result['password']
        username = request.form.get('username').lower()
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if queries.check_if_user_exist(username):
            flash('Username already exists. Please choose a different username')
            return redirect(url_for('register'))
        elif password != password2:
            flash('Passwords do not match')
            return redirect(url_for('register'))
        else:
            hashed_password = util.hash_password(password)
            queries.add_new_user(username, hashed_password)
            flash('Registration succesful. Log in to continue.')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username').lower()
        password = request.form.get('password')
        user_data = queries.get_user_details_by_username(username)
        print(user_data)
        if user_data == []:
            session['status'] = 1
            flash("Username dose not exist.")
            redirect(url_for('login'))
        else:
            saved_password = user_data[0]['password']
            if util.verify_password(password, saved_password):
                session["username"] = user_data[0]['username']
                return redirect(url_for('index'))
            else:
                session['status'] = 1
                flash("Wrong username or password")
                return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout', methods=["POST", "GET"])
def logout():
    session.pop('username', None)
    session.pop('status', None)
    return redirect(url_for('index'))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
