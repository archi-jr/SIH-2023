// script.js

// Function to fetch and display CSV data
async function displayCSV() {
    try {
        const response =  fetch("Symptoms and Illnesses.csv"); // Replace with your CSV file path
        const data =  response.text();
        const rows = data.split('\n');
        const table = document.createElement('table');

        // Loop through each row and create table rows and cells
        rows.forEach(row => {
            const rowData = row.split(',');
            const tableRow = document.createElement('tr');
            rowData.forEach(cellData => {
                const tableCell = document.createElement('td');
                tableCell.textContent = cellData;
                tableRow.appendChild(tableCell);
            });
            table.appendChild(tableRow);
        });

        // Display the table in the 'csv-table' div
        const csvTable = document.getElementById('csv-table');
        csvTable.appendChild(table);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the displayCSV function to load and display the CSV data
displayCSV();
