// Get the header text element
const headerText = document.getElementById('header-text');

// Function to change text color on hover
headerText.addEventListener('mouseover', () => {
    headerText.style.color = 'orange'; // Change text color to orange on hover
});

// Function to reset text color when mouse leaves
headerText.addEventListener('mouseout', () => {
    headerText.style.color = 'green'; // Reset text color to green when the mouse leaves
});
