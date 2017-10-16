from flask import Flask, render_template,request
app = Flask(__name__)
add_list=[]
f = open("templates/my-form.html","r");
text=[i.splitlines()[0] for i in f]
def add_web(html_text,add_list):
    a=1
    return a

@app.route("/")
def hello():
    return "".join(text)
@app.route("/input",methods=[ 'POST'])
def do():
    rec_name = request.form['fname']
    rec=request.form['sendtext']
    add_list.append(rec)
    text[81]="<p>{}".format("<br>".join(add_list))
    print(text[81],add_list)
    # list.append('{}:{}'.format(name,rtext))
    # print(list)
    #return "<br>".join(list)
    return "".join(text)
if __name__ == "__main__":

    app.run(host='140.134.27.130',port=2914,threaded=True)