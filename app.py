<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask
from flask import url_for
from markupsafe import escape
>>>>>>> 7b443d62d88e4a6563cfcf1a2885c8df75930daf

app = Flask(__name__)


@app.route('/')
<<<<<<< HEAD
def index():
    return render_template('index.html', name=name, movies=movies)


name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
=======
def hello():
    return '<h1>Welcome to My 阵地!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'User:{escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='keming'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'
>>>>>>> 7b443d62d88e4a6563cfcf1a2885c8df75930daf



# @app.route('/home')

if __name__ == '__main__':
    app.run(debug=True)