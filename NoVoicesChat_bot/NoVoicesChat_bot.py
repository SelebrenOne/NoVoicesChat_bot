import random
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

RANDOM_TEXTS = [
    "Привет! Как дела? "
]

# Функция, которая будет обрабатывать голосовые сообщения
def handle_voice(update: Update, context: CallbackContext):
    # Проверяем, что сообщение пришло из группы или супергруппы
    if update.message.chat.type in ["group", "supergroup"]:
        # Выбираем случайный текст из списка
        random_text = random.choice(RANDOM_TEXTS)
        
        # Отправляем текст в ответ на голосовое сообщение
        update.message.reply_text(random_text, reply_to_message_id=update.message.message_id)

def main():
    # Токен бота
    updater = Updater("u bot token past here", use_context=True)
    dp = updater.dispatcher

    # Регистрируем обработчик голосовых сообщений
    dp.add_handler(MessageHandler(Filters.voice, handle_voice))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()