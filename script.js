const chat = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");

function addMsg(who, text) {
  const p = document.createElement("p");
  p.textContent = who + ": " + text;
  chat.appendChild(p);
}

async function send() {
  const userText = input.value.trim();
  if (!userText) return;
  addMsg("You", userText);
  input.value = "";

  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userText }),
  });
  const data = await res.json();
  addMsg("AI", data.reply);
}

sendBtn.addEventListener("click", send);
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") send();
});