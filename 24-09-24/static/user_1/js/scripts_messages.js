// Get the conversation list and conversation details elements
let conversationList = document.getElementById('messageList');
let conversationDetails = document.getElementById('messageDetail');

// Function to open the conversation details (used for mobile)
function openConversation() {
    conversationList.style.display = 'none';
    conversationDetails.style.display = 'block';
}

// Function to go back to the conversation list
function goBack() {
    conversationList.style.display = 'block';
    conversationDetails.style.display = 'none';
}

// Function to handle initial visibility for responsive design
window.onload = function() {
    if (window.innerWidth <= 768) {
        conversationDetails.style.display = 'none';
    }
};

// Listen for window resize event to handle dynamic responsiveness
window.onresize = function() {
    if (window.innerWidth > 768) {
        conversationList.style.display = 'block';
        conversationDetails.style.display = 'block';
    } else {
        conversationDetails.style.display = 'none';
        conversationList.style.display = 'block';
    }
};
