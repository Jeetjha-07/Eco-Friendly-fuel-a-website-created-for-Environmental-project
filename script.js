// Add any JavaScript functionality you need for your website
// For example, you can use JavaScript to fetch and display dynamic data, or add interactive features.
document.getElementById('showFormButton').addEventListener('click', function() {
    // Show the form when the "Yes" button is clicked
    document.getElementById('surveyForm').style.display = 'block';
    // Set the Google Form URL when showing the form
    document.getElementById('googleForm').src = 'https://forms.gle/6pend1AhnDj9uwV78';
});

document.getElementById('closeFormButton').addEventListener('click', function() {
    // Hide the form when the "Close" button is clicked
    document.getElementById('surveyForm').style.display = 'none';
    // Clear the Google Form URL when hiding the form
    document.getElementById('googleForm').src = '';
});

// Initially hide the form when the page loads
document.getElementById('surveyForm').style.display = 'none';

// Add this code to your existing script.js or create a new JavaScript file
document.getElementById('darkModeToggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
});

// Add a function to toggle dark mode
function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    // Apply styles for dark mode to specific sections
    const sectionsToStyle = document.querySelectorAll('.rounded-box');
    sectionsToStyle.forEach(section => {
        section.style.backgroundColor = body.classList.contains('dark-mode') ? '#333' : '#f8f8f8';
        section.style.color = body.classList.contains('dark-mode') ? '#fff' : '#333';
    });
}

// ... (existing code)


function toggleSubtopics(topicId) {
    const subtopics = document.getElementById(topicId).getElementsByClassName("subtopics")[0];
    
    // Check if the subtopics are currently hidden
    const isHidden = subtopics.style.display === "none" || subtopics.style.display === "";
    
    // Set the display property based on the current state
    subtopics.style.display = isHidden ? "block" : "none";
}
