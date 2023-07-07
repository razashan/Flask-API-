from flask import Flask,redirect,url_for

app =Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my youtube Channel"

@app.route('/success/<int:score>')
def success(score):
    return "Hello I want to tell you that i got this score"+str(score)+" in Maths"

@app.route('/fail/<int:score>')
def fail(score):
    return "Hello I want to tell you that i got this score "+str(score)+" in Maths and I am fail"

@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks <50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score = marks))


if __name__=='__main__':
    app.run(debug=True)