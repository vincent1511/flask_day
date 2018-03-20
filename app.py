#coding:utf-8
from flask import Flask, request, render_template    #記得要import render_template

app = Flask(__name__)
mark = ""
def writeFile(data):
    f = open("E:\\python\\flash_day\\123.txt","w")
    f.write(data)
    f.close()

#網頁執行/say_hello時，會導至index.html
@app.route('/',methods=['GET'])
def getdata():
    return render_template('index.html')

#index.html按下submit時，會取得前端傳來的username，並回傳"Hellold! "+name
@app.route('/',methods=['POST'])
def submit():
    global mark;
    name = request.form.get('username')
    s = request.form.get('submit')
    if s == "Submit":
        mark = mark + name + "<br>"
        return render_template('index.html')

    elif s == "Submit_1":
        return "Hello, " + name + "1234"

if __name__ == '__main__':
    app.run(debug=True)
