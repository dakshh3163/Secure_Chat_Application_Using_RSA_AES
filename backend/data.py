USERS = {}          # username -> {public_key, private_key}
CONNECTIONS = {}    # username -> websocket

def register_user(username, public_key, private_key):
    USERS[username] = {
        "public": public_key,
        "private": private_key
    }

def store_connection(username, ws):
    CONNECTIONS[username] = ws

def get_connection(username):
    return CONNECTIONS.get(username)

def get_public_key(username):
    return USERS[username]["public"]

def get_private_key(username):
    return USERS[username]["private"]

def get_users():
    return USERS.keys()

