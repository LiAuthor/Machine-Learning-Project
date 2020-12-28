from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import jsonify
from chatterbot.response_selection import get_random_response
bot = ChatBot(
    'Example Bot',
    response_selection_method=get_random_response
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # logic_adapters=[
    #    {
    #        'import_path': 'chatterbot.logic.BestMatch',
    #        'default_response': '哈哈哈，没有听懂你在说什么',
    #        'maximum_similarity_threshold': 0.90
    #    }
    # ]
)

app = Flask(__name__, static_url_path="/static")


# ---- 这里提供了一个api，对到chatterbot的input
@app.route("/message", methods=["GET", "POST"])
def get_bot_response():
    #userText = request.args.get('message')
    # print(userText)
    # return str(bot.get_response(userText))  # 这一句代码对接了input
    req_msg = request.form['msg']
    res_msg_temp = str(bot.get_response(req_msg))
    # print(res_msg_temp)
    res_msg = res_msg_temp.replace("。", "。\n")
    print(res_msg)
    return jsonify({'text': res_msg})
    # return userText


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8808, debug=True)
