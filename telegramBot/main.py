import correncesApi
import telegrambot
lastId = -1
amount = 0
amount2 = 0

while True:
    result = telegrambot.getLastMessage()
    message = result['message']
    chat = {
        'chat_id' : message['from']['id'],
        'text' : 'Button',
        'reply_markup' : {
            'keyboard' : [[{'text' : 'UZS'},{'text' : 'USD'}], [{'text' : 'RUB'},{'text' : 'EUR'}]],
            'resize_keyboard' : True
        }
    }
    if result:
        if message.get('text') == '/start':
            text = f"Assalomu alaykum {message['from']['first_name']} {message['from']['last_name']}. \n UZS(so'm) ga convert qilinayotgan summani kirinting!"
            chat['text'] = text
        elif ((message.get('text') == 'UZS' or message.get('text') == 'RUB' or message.get('text') == 'USD' or message.get('text') == 'EUR') and amount != amount2):
            amount2 = correncesApi.correnyConvert(amount,message.get('text'),'UZS')
            text = message.get('text')
            chat['text'] = f'{amount} {text} {amount2} UZS(so\'m)'
            amount = amount2
        elif message.get('photo'):
            photo = message['photo']
            chat['text'] = ''
            chat['photo'] = photo[0].get('file_id')
        else :
            text = message.get('text')
            try:
                amount = int(text)
                chat['text'] = 'Valutani tanlang'
            except:
                chat['text'] = "UZS(so'm) ga convert qilinayotgan summani kirinting!"

        if lastId != result['update_id']:
            lastId = result['update_id']
            telegrambot.button(chat)