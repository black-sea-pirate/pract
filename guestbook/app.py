from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)

messages = []

@app.route('/', methods = ['GET'])
def home_page():
    sorted_messages = sorted(messages, key=lambda msg: msg['likes'], reverse=True)
    return render_template('index.html', messages=sorted_messages)

@app.route('/add', methods = ['POST'])
def add_comment():
    author = request.form.get('author')
    content = request.form.get('content')
    if author and content:
        message = {'author':author, 'content':content, 'likes': 0}
        messages.append(message)
    return redirect(url_for('home_page'))

@app.route('/delete/<int:index>', methods = ['GET'])
def delete_comment(index):
    if 0 <= index < len(messages):
        messages.pop(index)
    return redirect(url_for('home_page'))

@app.route('/like/<int:index>')
def like(index):
    if 0 <= index < len(messages):
        messages[index]['likes']+=1
    return redirect(url_for('home_page'))

if __name__ == '__main__':
    app.run(debug=True)
