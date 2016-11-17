from chatterbot import ChatBot
from examples.settings import TWITTER
import logging
from sys import argv

if argv[1] == "train":
    i = 0
    while i < 1000:
        i += 1
        stream_handler = logging.StreamHandler()
        handler = logging.FileHandler(filename='trainer.log', mode='w', encoding='utf-8')
        logging.basicConfig(level=logging.INFO, handlers=[handler, stream_handler])

        chatbot = ChatBot("TwitterBot",
                          logic_adapters=[
                              "chatterbot.adapters.logic.ClosestMatchAdapter"
                          ],
                          input_adapter="chatterbot.adapters.input.TerminalAdapter",
                          output_adapter="chatterbot.adapters.output.TerminalAdapter",
                          database="./database.db",
                          twitter_consumer_key=TWITTER["CONSUMER_KEY"],
                          twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
                          twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
                          twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
                          trainer="chatterbot.trainers.TwitterTrainer"
                          )

        chatbot.train()

        chatbot.logger.info('Twitter Training Step {0} of 1000 done.'.format(str(i)))

elif argv[1] == "export":
    logging.basicConfig(level=logging.INFO)
    chatbot = ChatBot("Export Trainer")
    chatbot.trainer.export_for_training('./export.json')

else:
    print('     ChatBot Trainer v1.0 by Soundoflight      ')
    print('-----------------------------------------------')
    print('  Please supply one of the following Options:  ')
    print('-----------------------------------------------')
    print('train = uses an given Twitter Account to train!')
    print('                                               ')
    print('     export = export the Bot data as json      ')
    print('-----------------------------------------------')

