import correncesApi
import telegrambot
lastId = -1

while True:
    result = telegrambot.getLastMessage()
    message = result['message']
    if result:
        if message['text'] == '/start':
            text = f"Assalomu alaykum {message['from']['first_name']} {message['from']['last_name']}"
        else:
            text = message['text']
        chat = {
            'chat_id' : message['from']['id'],
            'text' :text,
            'parse_mode' : 'HTML'
        }
        if lastId != result['update_id']:
            lastId = result['update_id']
            telegrambot.bot('sendMessage',chat)

amount = correncesApi.correnyConvert(100,'USD','UZS')