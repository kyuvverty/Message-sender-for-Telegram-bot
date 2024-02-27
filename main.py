import tkinter as tk
import telebot
import config # config.py


# Initializing a Tkinter window
window = tk.Tk(className=" Telegram Bot Message Sender")
window.geometry("600x500") # Width, Height

# Text
label_chatId = tk.Label(text="Chat ID")
label_message = tk.Label(text="Message")
label_token = tk.Label(text="Bot token")

# Enter
txt_enter = tk.Text(width=40, height=20)
ent_enterId = tk.Entry(width=53)
ent_token = tk.Entry(width=53)

# Variables
chatId = "chatId"
user_message = "message"
token = "token"

# Create a function that is called when the submit button is clicked
def buttonSendClicked():
    global user_message, chatId, token

    user_message = txt_enter.get("1.0", tk.END)
    chatId = ent_enterId.get()
    token = ent_token.get()
    if '=' in token: # If you write - in token
        bot = telebot.TeleBot(config.BOTS_LIST.get(token[1:]))
        print(token)
    else:
        bot = telebot.TeleBot(token)
    if '=' in chatId: # If you write - in chatId
        chatId = config.USER_LIST.get(chatId[1:])
    try:
        bot.send_message(chatId, f"{user_message}")
        print(f"Your message has been sent to {chatId}:\n{user_message}\n----------------------\n")
    except Exception as error: # If an error occurs
        print(f'(ERROR) {error} \n----------------------\n')

# Creating a function that is called when the clear button is clicked
def buttonClearClicked():
    txt_enter.delete("1.0", tk.END)
    
# Creating buttons
btn_send = tk.Button(window, text="Send", command=buttonSendClicked)
btn_clear = tk.Button(window, text="Clear", command=buttonClearClicked)

# Setting objects in a window
label_token.grid(column=0, row=0)
label_chatId.grid(column=0, row=1)
label_message.grid(column=0, row=2)

ent_token.grid(column=1, row=0)
ent_enterId.grid(column=1, row=1)
txt_enter.grid(column=1, row=2)

btn_send.grid(column=2, row=0, padx=5)
btn_clear.grid(column=2, row=2, padx=5)

# Running Tkinter mainloop
window.mainloop()