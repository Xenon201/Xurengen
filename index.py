from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return de los datos a continuacion:
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True ,port=8790)
