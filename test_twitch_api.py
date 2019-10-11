import pytwitcherapi
import webbrowser
import time
import threading
import queue

session = pytwitcherapi.TwitchSession()
url = session.get_auth_url()

session.start_login_server()
webbrowser.open(url)

while not session.authorized:
    time.sleep(2)

time.sleep(2)

print("Authorized")

session.shutdown_login_server()


channel = session.get_channel("thebasementclub")
client = pytwitcherapi.IRCClient(session,channel)


print("bot in chat")
thread_chat_update = threading.Thread(target=client.process_forever)
thread_chat_update.start()

while True:
    try:
        messages = client.messages.get(False)
        if messages.text == "!ping":
            client.send_msg("pong!")
    except queue.Empty:
        pass