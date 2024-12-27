
# Telegram Bot Project

## Overview
This project is a Telegram bot that provides the following functionalities:
- Alerts and notifications based on schedules.
- User management using SQLite.

## Features
1. **Alerts and Notifications**: Sends reminders to all registered users.
2. **User Management**: Tracks and manages users interacting with the bot.

## Setup Instructions
1. Clone this repository or download the files.
2. Install Python 3.8+ and required libraries:
   ```bash
   pip install python-telegram-bot schedule sqlite3
   ```
3. Replace `YOUR_BOT_TOKEN` in `telegram_bot.py` with your bot's token from BotFather.
4. Run the bot:
   ```bash
   python telegram_bot.py
   ```

## How to Use
1. Start the bot on Telegram by typing `/start`.
2. The bot will automatically add users to the database.
3. Alerts are scheduled to send daily at 10:00 AM.

## Database
- The SQLite database `users.db` stores user information:
  - `user_id`: Telegram user ID.
  - `username`: Telegram username.
  - `first_name`: User's first name.
  - `last_name`: User's last name.

## License
This project is licensed under the MIT License.
