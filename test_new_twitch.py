import twitch
import webbrowser
import time
import threading
import queue


h = twitch.Helix('rst4gol14h5s86eax89ju3ot6uipuy')

chat = twitch.Chat(channel='thebasementclub', nickname='Banishment_of_this_World', oauth='oauth:g62i86e9gtdc5fyj2suncmcxplqc6r')

chat.subscribe(lambda message: print(message.channel, message.sender, message.text))

# thread_chat_update = threading.Thread(target=client.process_forever)
# thread_chat_update.start()

# while True:
#     try:
#         messages = client.messages.get(False)
#         if messages.text == "!ping":
#             client.send_msg("pong!")
#     except queue.Empty:
#         pass

# print('done')