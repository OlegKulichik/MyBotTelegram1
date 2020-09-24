from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    PrefixHandler,
    Filters,
)
import os
import random


class TelegramBot(Updater):
    def __init__(self, token: str):
        super().__init__(token, use_context=True)

    def command(self, name: str):
        def _handler(func):
            self.dispatcher.add_handler(CommandHandler(name, func))

        return _handler

    def prefix(self, pref: [str], name: str):
        def _handler(func):
            self.dispatcher.add_handler(PrefixHandler(pref, name, func))

        return _handler

    def text(self):
        def _handler(func):
            self.dispatcher.add_handler(MessageHandler(Filters.text, func))

        return _handler

    def run(self):
        self.start_polling()
        self.idle()
