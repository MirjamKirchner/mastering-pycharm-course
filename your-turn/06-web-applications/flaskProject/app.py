import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    from data import fake_data
    orders = fake_data.get_orders()
    return flask.render_template('index.html', orders=orders)


if __name__ == '__main__':
    app.run()
