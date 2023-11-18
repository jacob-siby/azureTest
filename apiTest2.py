from flask import Flask, jsonify, request 
  
# creating a Flask app 
app = Flask(__name__) 
  
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 
  
  
# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/home/<l>', methods = ['GET']) 
def disp(l): 
    l=l.split(',')
    l=[int(x) for x in l]
  
    return jsonify({'max': sum(l)}) 
  
  
# driver function 
if __name__ == '_main_': 
  
    app.run(host='0.0.0.0',port=5000)