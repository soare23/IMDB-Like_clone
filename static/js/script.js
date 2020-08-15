// // Form verification
// document.getElementById('form').addEventListener('submit', verifyForm);
// let errorEl = document.getElementById('error');
// errorEl.style.display = 'none';

// function verifyForm(e) {
//   e.preventDefault();
//   let password = document.getElementById('password');
//   let password2 = document.getElementById('password2');
//   let username = document.getElementById('user');
//   let errorEl = document.getElementById('error');

//   if (password.value === password2.value) {
//     console.log(username.value);
//     console.log(password.value);

//     let dataToSend = {
//       username: username.value,
//       password: password.value,
//     };

//     fetch(`/register`, {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify(dataToSend),
//       cache: 'no-cache',
//     })
//       .then((window.location.href = '/login'))
//       .catch((err) => {
//         console.log(err);
//       });
//   } else {
//     console.log('a mers');
//     // errorEl.style.display = 'flex';
//     password.value = '';
//     password2.value = '';
//   }
// }
