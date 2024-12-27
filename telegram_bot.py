from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
import sqlite3
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio

# Replace with your actual bot token
TOKEN = "8172473605:AAFbRkSs9ysiFxg5iOrZxx13glfbknhSrnc"

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to the Persist Ventures Bot!")

# Function to handle the /reminder command
async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=context.job.chat_id, text="Reminder: Don't forget to check your tasks!")

async def schedule_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text("Reminder scheduled!")
    # Schedule a reminder in 10 seconds (example)
    context.job_queue.run_once(send_reminder, 10, chat_id=chat_id)

# Function to handle saving the user to the database
async def save_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "unknown"
    cursor.execute("INSERT OR IGNORE INTO users (id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    await update.message.reply_text(f"User {username} saved!")

# Function to fetch the user report
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fetching your report...")

# Function to handle menu option buttons
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == '1':
        await query.edit_message_text(text="You selected Option 1")
    elif query.data == '2':
        await query.edit_message_text(text="You selected Option 2")

# Create or connect to the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)""")
conn.commit()

# Main function to run the bot
def main():
    # Create the Application object with the bot token
    application = Application.builder().token(TOKEN).build()

    # Add command handlers for /start, /save_me, /report
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("save_me", save_user))
    application.add_handler(CommandHandler("report", report))
    application.add_handler(CommandHandler("reminder", schedule_reminder))

    # Add the inline button handler
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CallbackQueryHandler(button))

    # Add scheduler to the bot
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_task, "interval", minutes=1)
    scheduler.start()

    # Run the bot (starts polling for updates)
    application.run_polling()

# Function for scheduled task (just a simple print)
def scheduled_task():
    print("Scheduled task executed!")

# Function to create the menu with options
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data='1')],
        [InlineKeyboardButton("Option 2", callback_data='2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

if __name__ == "__main__":
    main()
