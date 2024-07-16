// script.js

document.addEventListener('DOMContentLoaded', function() {
    const chatTrigger = document.getElementById('chat-trigger');
    const chatContainer = document.getElementById('chat-container');
    const chatbotFrame = document.getElementById('chatbot-frame');

    chatTrigger.addEventListener('click', function() {
        if (chatContainer.style.display === 'block') {
            chatContainer.style.display = 'none';
        } else {
            chatContainer.style.display = 'block';
            chatbotFrame.src = "https://console.dialogflow.com/api-client/demo/embedded/0ab19b89-3d75-4e78-9a43-b269dc52c6f1";
        }
    });
});
