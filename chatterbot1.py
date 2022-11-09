from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

print('Cheers')

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "I didn't understand your question, nevertheless check our job offers! "
                                "https://r.mtdv.me/articles/job_offer",
            'maximum_similarity_threshold': 0.5
        }
    ],
    database_uri='sqlite:///database.db'
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("./conversations.yml")

while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
