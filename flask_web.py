from flask import Flask,render_template, jsonify,request
from agent import run_conversion


app = Flask(__name__)   
@app.route('/process_message',methods = ['POST'])
def process_message_func():
    msg = request.json['message']
    print("We are getting ", msg)
    resp = run_conversion(msg)
    return jsonify({"response":resp})


@app.route('/') 
def hello():
    return render_template("index.html")
    # All index.html that codes must in the templates folder
    # All css,js and images must be in the static folder


if __name__ == "__main__":  
    app.run(host= "0.0.0.0",port = 5000,debug=True)  # run the server