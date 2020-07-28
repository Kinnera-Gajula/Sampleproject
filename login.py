import json
from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
def make_error(status_code, message):
    response = jsonify({
        'status': status_code,
        'msg': message,
    })
    
    #response.status_code = status_code
    return response
@app.route("/")
def index():
    
    return render_template('log.html')
@app.route('/login',methods = ['POST', 'GET'])
def output():
    digits='no'
    alpha='no'

    if request.method == 'POST':
        username=request.form['username']
        pwd=request.form['password']
        for i in username:
            if not i.isalpha():
                return make_error(203,"Failure:only characters allowed in username")
        if len(pwd)>=6:
            for i in pwd:
                if i.isalpha():
                    alpha='yes'
                elif i.isdigit():
                    digits='yes'
            if alpha=='yes':
                if digits=='yes':
                    return make_error(200,"success")
                else:
                    return make_error(202,"Failure:password to have 1 character and 1 number")
        else:
            return make_error(201,"Failure: password must be of length 6")
        

if __name__ == "__main__":
    app.run(debug=True)
