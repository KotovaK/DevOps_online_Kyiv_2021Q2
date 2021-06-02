from flask import Flask, render_template
import random

app = Flask(__name__)
images = [
   "https://illustrators.ru/uploads/illustration/image/816802/main_816802_original.jpg",
    "https://cs7.pikabu.ru/post_img/big/2014/07/02/8/1404299284_1561822350.jpg",
    "https://natelegram.ru/wp-content/uploads/2018/03/cat_prog-320x320.jpg",
    "https://nocens.net/i/2/21403277010.jpg",
    "https://img1.liveinternet.ru/images/attach/c/0/113/154/113154651_1400615030_demotivatory_02_1.jpg",
    "https://cs13.pikabu.ru/post_img/2020/12/12/7/1607768622182584986.jpg",
    "https://media.proglib.io/wp-uploads/2018/06/junior_vs_senior.png"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
