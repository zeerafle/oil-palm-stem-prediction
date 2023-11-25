// document.querySelector('form').addEventListener('submit', async (event) => {
//     event.preventDefault();
//     const formData = new FormData(event.target);
//     try {
//         const response = await fetch('/prediction', {
//             method: 'POST',
//             body: formData
//         });
//         document.getElementById('prediction-result').innerText = await response.text();
//     } catch (error) {
//         console.log(error);
//     }
// });

// async function predict() {
//     try {
//         const form = document.getElementById('upload-form')
//         const formData = new FormData(form);
//
//         const response = await fetch('/prediction', {
//             method: 'POST',
//             body: formData
//         });
//         document.getElementById('prediction-result').innerText = await response.text();
//     } catch (error) {
//         console.log(error);
//     }
// }