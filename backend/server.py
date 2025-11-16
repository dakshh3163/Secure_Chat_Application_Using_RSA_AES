from fastapi import FastAPI, WebSocket

from crypto import rsa_encrypt, rsa_decrypt, aes_encrypt, rsa_keygen
import json
import data


app = FastAPI()

@app.post("/register")
async def register(user: dict):
    username = user["username"]

    pub, priv = rsa_keygen()
    data.register_user(username, pub, priv)

    return {"public_key": pub, "private_key": priv}


@app.websocket("/ws/{username}")
async def websocket_endpoint(ws: WebSocket, username: str):
    await ws.accept()
    data.store_connection(username, ws)

    while True:
        msg = await ws.receive_text()
        payload = json.loads(msg)

        target = payload["to"]
        message = payload["message"]

        target_ws = data.get_connection(target)
        if target_ws:
            await target_ws.send_text(
                json.dumps({
                    "from": username,
                    "message": message
                })
            )
