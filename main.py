import tkinter as tk
import telebot
import config # config.py


# Initializing a Tkinter window
window = tk.Tk(className=" Telegram Bot Message Sender")
window.geometry("750x500") # Width, Height

# Text
label_chatId = tk.Label(text="Chat ID")
label_message = tk.Label(text="Message")
label_token = tk.Label(text="Bot token")

# Enter
txt_enter = tk.Text(width=40, height=20)
ent_enterId = tk.Entry(width=53)
ent_token = tk.Entry(width=53)

# CheckBoxes
var_checkBox_consoleLogBot = False
var_checkBox_consoleLogChat = False
var_checkBox_consoleLogMessage = False
def checkBoxEdit_Token():
    global var_checkBox_consoleLogBot
    if var_checkBox_consoleLogBot == False:
        var_checkBox_consoleLogBot = True
    else:
        var_checkBox_consoleLogBot = False
def checkBoxEdit_Chat():
    global var_checkBox_consoleLogChat
    if var_checkBox_consoleLogChat == False:
        var_checkBox_consoleLogChat = True
    else:
        var_checkBox_consoleLogChat = False
def checkBoxEdit_Message():
    global var_checkBox_consoleLogMessage
    if var_checkBox_consoleLogMessage == False:
        var_checkBox_consoleLogMessage = True
    else:
        var_checkBox_consoleLogMessage = False
checkBox_consoleLogBot = tk.Checkbutton(text="Console Log Token", command=checkBoxEdit_Token)
checkBox_consoleLogChat = tk.Checkbutton(text="Console Log ChatID", command=checkBoxEdit_Chat)
checkBox_consoleLogMessage = tk.Checkbutton(text="Console Log Message", command=checkBoxEdit_Message)

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
    if '=' in token: # If you write '=' in token
        token = config.BOTS_LIST.get(token[1:])
    bot = telebot.TeleBot(token)
    if '=' in chatId: # If you write '=' in chatId
        chatId = config.USER_LIST.get(chatId[1:])
    try:
        bot.send_message(chatId, f"{user_message}")
        if var_checkBox_consoleLogBot and not (var_checkBox_consoleLogChat):
            print(f"Token: {token}\n")
        if var_checkBox_consoleLogBot and var_checkBox_consoleLogChat:
            print(f"Token: {token}")
        if var_checkBox_consoleLogChat:
            print(f"ChatID: {chatId}\n")
        if var_checkBox_consoleLogMessage:
            print(f"Your message has been sent:\n{user_message}\n----------------------\n")
        else:
            print(f"Your message has been sent!\n----------------------\n")
    except Exception as error: # If an error occurs
        print(f'(ERROR) {error} \n----------------------\n')

# Creating a function that is called when the clear button is clicked
def buttonClearClicked():
    txt_enter.delete("1.0", tk.END)
    
# Creating buttons
btn_send = tk.Button(window, text="Send", command=buttonSendClicked)
btn_clear = tk.Button(window, text="Clear", command=buttonClearClicked)

# Setting objects in a window
label_token.grid(column=0, row=0, pady=5)
label_chatId.grid(column=0, row=1, pady=5)
label_message.grid(column=0, row=2, pady=5)

checkBox_consoleLogBot.place(x=510, y=5)
checkBox_consoleLogChat.place(x=510, y=35)
checkBox_consoleLogMessage.place(x=510, y=65)

ent_token.grid(column=1, row=0, pady=5)
ent_enterId.grid(column=1, row=1, pady=5)
txt_enter.grid(column=1, row=2, pady=5)

btn_send.grid(column=3, row=2, padx=5)
btn_clear.grid(column=2, row=2, padx=5)

# Running Tkinter mainloop
window.mainloop()