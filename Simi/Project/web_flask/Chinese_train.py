from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# 创建一个机器人，命名为Ｓimi
bot = ChatBot('Simi')
# 使用语料训练模型
trainer = ChatterBotCorpusTrainer(bot)
# 指定语料范围使用模型开始训练
trainer.train("../corpus/Chinese/")

# 测试训练结果
print("开始聊天吧...")
while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


# DONE
