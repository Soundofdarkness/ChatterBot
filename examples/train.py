from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

chatterbot = ChatBot("Training Bot")

chatterbot.trainer.export_for_training("./export.json")