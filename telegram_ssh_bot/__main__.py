import time 

import subprocess

from telebot import TeleBot

from telebot.util import smart_split

from settings import BOT_TOKEN
from settings import GLOBAL_DELAY


def execute_command(command) -> str:
    try:
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return f"Known Error: {e.output}"
    except Exception as exc:
        return f"Critical Error: {exc}"


class BasicTelegramBot:

    def __init__(
        self
    ):
        self.bot = TeleBot(BOT_TOKEN)

    def send_any_size_message(self, chat_id: int, text: str) -> None:
        chunks = smart_split(text, 4000)
        for message in chunks:
            self.bot.send_message(chat_id=chat_id, text=f"```{message}```", parse_mode="Markdown")
            time.sleep(GLOBAL_DELAY)


def main() -> int:

    bot_service = BasicTelegramBot()
    telegram_bot = bot_service.bot

    @telegram_bot.message_handler(commands=["exec"])
    def exec_command(message) -> None:
        chat_id = message.chat.id
        command_result = execute_command(message.text.split("exec")[-1])
        bot_service.send_any_size_message(
            chat_id, 
            command_result
        )

    print(f"Bot has been started!")

    telegram_bot.infinity_polling(timeout=60)

    return 1


if __name__ == "__main__":
    main()