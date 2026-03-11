import telebot
TOKEN = "8715068986:AAF1_x5Y8bxlT9LV4VTAjVk05VqXcS_nLi8"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"مرحباً {message.from_user.first_name}! 👋\n"
        "أنا بوتك الجديد 🤖\n\n"
        "جرّب الأوامر التالية:\n"
        "/help - للمساعدة\n"
        "/about - معلومات عني"
    )
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "📝 قائمة الأوامر:\n\n"
        "/start - بدء المحادثة\n"
        "/help - عرض هذه الرسالة\n"
        "/about - معلومات عن البوت\n"
        "/time - الوقت الحالي\n\n"
        "يمكنك أيضاً إرسال أي رسالة وسأردّ عليك!"
    )
@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(
        message.chat.id,
        "🤖 أنا بوت تيليجرام بسيط\n"
        "تم برمجتي بلغة Python 🐍\n"
        "صُنعت بواسطة: Emir"
    )
@bot.message_handler(commands=['time'])
def send_time(message):
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.send_message(message.chat.id, f"🕐 الوقت الحالي:\n{now}")
@bot.message_handler(content_types=['text'])
def echo_message(message):
    user_text = message.text
    bot.send_message(
        message.chat.id,
        f"📩 أنت كتبت:\n{user_text}\n\n"
        f"عدد الحروف: {len(user_text)}"
    )
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "📸 صورة جميلة! شكراً على المشاركة")
# الرد على الملصقات
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.reply_to(message, "😄 ملصق رائع!")
print("=" * 50)
print("✅ البوت يعمل الآن...")
print("📱 افتح تيليجرام وابحث عن البوت")
print("⚠️  اضغط Ctrl+C لإيقاف البوت")
print("=" * 50)

bot.polling(none_stop=True)