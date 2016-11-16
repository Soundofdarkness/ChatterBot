from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

chatterbot = ChatBot("Training Bot")

chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english"
)