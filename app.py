from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('hello.html',name=name)
    return '''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit">
        </form>
        '''




if __name__ == '__main__':
    app.run(debug=True)
