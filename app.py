from flask import Flask, render_template,request,jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)



mongo = PyMongo(app)

@app.route('/')
def home_page():
    try:
        online_users = mongo.db.user.find({"online": True})
        online_users_list = list(online_users)
        return render_template("index.html", online_users=online_users_list, name=name, movies=movies)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/home')
def index():
    return render_template('index.html', name=name, movies=movies)


name = 'keming'
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



# @app.route('/home')

if __name__ == '__main__':
    app.run(debug=True)