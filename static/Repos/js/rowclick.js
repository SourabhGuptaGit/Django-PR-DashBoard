const rows = document.querySelectorAll('#data_rows');

// Loop through each row and add a click event listener
rows.forEach((row) => {
  row.addEventListener('click', () => {
    // Get the email value from the clicked row
    const email = row.cells[1].textContent.trim();

    // Set the value of the search input field to the email value
    document.querySelector('#search-input').value = email;

    // Submit the form
    document.querySelector('#search-form').submit();
  });
});




//   // Add a click event listener to the search button
//   document.querySelector('#search-input').addEventListener('click', () => {
//     // Submit the form
//     document.querySelector('#search-form').submit();
//   });