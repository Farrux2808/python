import telegrambot
result = telegrambot.getLastMessage()
message = result['message']
chat = {
    'chat_id' : message['from']['id'],
    'emoji' : ''
}
telegrambot.bot('sendDice',chat)