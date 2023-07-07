from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to the Krish Youtubes  Channel'

@app.route('/hello')
def helle():
    return "So you got me "



if __name__=='__main__':
    app.run()