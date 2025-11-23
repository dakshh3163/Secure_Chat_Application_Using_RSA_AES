let ws;
let username;

function connect() {
    username = document.getElementById("user").value;
    ws = new WebSocket(`ws://localhost:8000/ws/${username}`);

    const status = document.getElementById("status");
    if (status) {
        status.textContent = "✔";
    }

    ws.onmessage = (msg) => {
        const data = JSON.parse(msg.data);
        const chat = document.getElementById("chat");
        chat.innerHTML += `<div><b>${data.from}:</b> ${data.message}</div>`;
        chat.scrollTop = chat.scrollHeight;
    };
    const connection = document.getElementById("connectionBtn");
    if (connection) {
        connection.textContent = "Connected";
    }
    document.title = username;
}

function sendMsg() {
    const target = document.getElementById("target").value;
    const text = document.getElementById("msg").value;
    const chat = document.getElementById("chat");
    chat.innerHTML += `<div><b>Me -> ${target}:</b> ${text}</div>`;
    chat.scrollTop = chat.scrollHeight;
    let div = document.getElementById("chat");
    div.scrollTop = div.scrollHeight;

    ws.send(JSON.stringify({
        to: target,
        message: text
    }));
}
document.getElementById("msg").addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        sendMsg();
    }
});



