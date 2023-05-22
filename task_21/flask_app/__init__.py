from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/')
@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/')
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)