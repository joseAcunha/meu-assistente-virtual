document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');

    const API_URL = 'http://127.0.0.1:8000/chat';

    function addMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');

        if (sender === 'user') {
            messageDiv.classList.add('user-message');
            messageDiv.textContent = message;
        } else {
            messageDiv.classList.add('bot-message');
            messageDiv.innerHTML = marked.parse(message);
        }
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    async function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') return;

        addMessage(message, 'user');
        userInput.value = '';

        const loadingMessageDiv = document.createElement('div');
        loadingMessageDiv.classList.add('message', 'bot-message', 'bg-white', 'self-start', 'max-w-[75%]', 'italic', 'text-gray-500');
        loadingMessageDiv.textContent = 'Assistente digitando...';
        chatMessages.appendChild(loadingMessageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            chatMessages.removeChild(loadingMessageDiv);

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(`Erro na API: ${response.status} - ${errorData.detail || 'Erro desconhecido'}`);
            }

            const data = await response.json();
            addMessage(data.response, 'bot');
        } catch (error) {
            if (chatMessages.contains(loadingMessageDiv)) {
                chatMessages.removeChild(loadingMessageDiv);
            }
            console.error('Erro ao enviar mensagem:', error);
            addMessage('Ops! Houve um problema ao conectar com o assistente. Por favor, tente novamente.', 'bot');
        }
    }

    sendButton.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});