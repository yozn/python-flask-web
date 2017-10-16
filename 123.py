from flask import Flask, render_template,request
app = Flask(__name__)
list=[]
@app.route("/")
def hello():
    return render_template('my-form.html')
@app.route("/input")
def do():
    name=request.args.get('fname')
    rtext = request.args.get('sendtext')
    list.append('{}:{}'.format(name,rtext))
    print(list)
    return "<br>".join(list)
if __name__ == "__main__":
    app.run(host='140.134.27.130',port=2914,threaded=True)