from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def menu_bar():
    return render_template('menu_bar.html')

if __name__ == '__main__':
    app.run(debug=True)
