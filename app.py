import os
from flask import Flask

app = Flask(__name__)

@app.route('/env')
def env():
    list = []
    for a in os.environ:
        env = (a+':'+ os.getenv(a))
        list.append(env)
    return "<br>".join(list)

@app.route('/')
def root():
    list = ["/env"]
    return "test1ss) Urls:<br><br>"+" <br>".join(list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
