from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def sent():
    return render_template('shortlst.html')

if __name__ == '__main__':
    app.run(debug=True)