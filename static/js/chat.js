async function sendMessage() {
    const inputField = document.getElementById("message");
    const userMessage = inputField.value.trim();
    if (!userMessage) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p class="user"><b>You:</b> ${userMessage}</p>`;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();
        chatBox.innerHTML += `<p class="bot"><b>Bot:</b> ${data.response}</p>`;
    } catch (error) {
        chatBox.innerHTML += `<p class="bot" style="color:red;"><b>Error:</b> Could not connect to server.</p>`;
    }

    inputField.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}

document.getElementById("message").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // prevent newline
        sendMessage();
    }
});

function sendQuickMessage(text) {
    document.getElementById("message").value = text;
    sendMessage();
}

function toggleChat() {
    const chatContainer = document.getElementById("chat-container");
    chatContainer.style.display = chatContainer.style.display === "flex" ? "none" : "flex";
}

function goToService(path) {
    // Redirect to your website services page
    window.open("https://theessentialindia.com" + path, "_blank");
}


