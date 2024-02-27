------------------------ ENG ------------------------

This program provides the ability to write on behalf of a bot in Telegram chats, without the need to launch the bot.
To do this you need:
1. Enter the Telegram bot token in the 'Bot token' field;
2. Enter the Telegram chat ID in the 'ChatID' field;
3. Enter the message you want to send in the 'Message' field.

The 'Send' button sends your message.
The 'Clear' button clears the 'Message' field.

Please note that the bot can only write to those users who launched the bot.
If you need to paste something into a field, you need to switch your keyboard layout to English.

You can make things easier for yourself by filling out the 'config.py' file (which can be opened in any text editor).
In it you can change the lists BOTS_LIST (list of bots) and USER_LIST (list of users).
Example:
BOTS_LIST = {
    'mybot1': '1234567890:ThKHG-H6bfhF7ngfbkbFH1hjbFh_j9E',
    'mybot2': '0987654321:hfjKf-mkfdlNGlvn36lvjlNVklm_mf8'
    }

USER_LIST = {
    'user1': '1111111111',
    'user2': '2222222222'
    }
Then in the 'Bot token' and 'ChatID' fields you can enter, for example, '=mybot1' and '=user1' respectively, with the '=' key sign at the beginning.
The '=' sign means that you are taking data from a pre-prepared list.
In this case ('=mybot1' and '=user1') the message will be sent to the user with ID '1111111111' from the bot with the token '1234567890:ThKHG-
H6bfhF7ngfbkbFH1hjbFh_j9E'.

The program was written using the Python programming language and the tkinter and telebot libraries.
My GitHub: https://github.com/kyuvverty

------------------------ RUS ------------------------

Данная программа предоставляет возможность писать от имени бота в чаты Telegram, без необходимости запуска бота.
Для этого необходимо:
1. Вести в поле 'Bot token' токен Telegram бота;
2. Ввести в поле 'ChatID' ID чата Telegram;
3. Ввести сообщение в поле 'Message', которое хотите отправить.

Кнопка 'Send' отправляет ваше сообщение.
Кнопка 'Clear' очищает поле 'Message'.

Учтите, что бот может писать только тем пользователям, которые запускали бота.
Если вам необходимо вставить что-либо в поле, необходимо переключить раскладку клавиатуры на английскую.

Вы можете упростить себе задачу, заполнив файл 'config.py' (его можно открыть в любом текстовом редакторе).
В нем вы можете изменить списки BOTS_LIST (список ботов) и USER_LIST (список пользователей).
К примеру:
BOTS_LIST = {
    'mybot1': '1234567890:ThKHG-H6bfhF7ngfbkbFH1hjbFh_j9E',
    'mybot2': '0987654321:hfjKf-mkfdlNGlvn36lvjlNVklm_mf8'
    }

USER_LIST = {
    'user1': '1111111111',
    'user2': '2222222222'
    }

Тогда в поля 'Bot token' и 'ChatID' вы можете вписать, к примеру, '=mybot1' и '=user1' соответственно, с ключевым знаком '=' в начале.
Знак '=' означает, что вы берете данные из заранее заготовленного списка.
В данном случае ('=mybot1' и '=user1') сообщение будет отправлено пользователю с ID '1111111111' от бота с токеном '1234567890:ThKHG-H6bfhF7ngfbkbFH1hjbFh_j9E'.

Программа была написана с помощью языка программирования Python и библиотек tkinter и telebot.
Мой GitHub: https://github.com/kyuvverty