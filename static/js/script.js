let videoURLs = document.querySelector('iframe');
videoURLs.src = videoURLs.src.replace('watch?v=', 'embed/');

// // let nextBtn = document.getElementById('next');
// // let previousBtn = document.getElementById('previous');
// // let count = 0;

// // function nextData() {
// //   let dataToSend = {
// //     counter: count,
// //   };

// //   fetch(`${window.origin}/shows/most-rated/`, {
// //     method: 'POST',
// //     headers: {
// //       'Content-Type': 'application/json',
// //     },
// //     body: JSON.stringify(dataToSend),
// //     cache: 'no-cache',
// //   });
// // }

// // nextBtn.addEventListener('click', () => {
// //   count += 15;
// //   nextData();
// // });
// // previousBtn.addEventListener('click', () => {
// //   if (count > 0) {
// //     count -= 15;
// //   }
// //   nextData();
// // });

// // showList = []

// let titleBtn = document.getElementById('title');
// let yearBtn = document.getElementById('year');
// let runtimeBtn = document.getElementById('runtime');
// let ratingBtn = document.getElementById('rating');
// let title = '';
// let year = '';
// let runtime = '';
// let rating = '';

// // send data with fetch

// function sortingData() {
//   let dataToSend = {
//     title: title,
//     year: year,
//     runtime: runtime,
//     rating: rating,
//   };

//   fetch(`${window.location}`, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify(dataToSend),
//     cache: 'no-cache',
//   });
// }

// // add event listenres

// titleBtn.addEventListener('click', (e) => {
//   title = e.target.innerText;
//   sortingData();
// });
// yearBtn.addEventListener('click', (e) => {
//   year = e.target.innerText;
//   sortingData();
// });
// runtimeBtn.addEventListener('click', (e) => {
//   runtime = e.target.innerText;
//   sortingData();
// });
// ratingBtn.addEventListener('click', (e) => {
//   rating = e.target.innerText;
//   sortingData();
// });
