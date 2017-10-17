
import time
import re
from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)
add_list=[]
f = open("templates/my-form.html","r");
text=[i.splitlines()[0] for i in f]
ip_dict={}
def check_url_img(str):
    c = re.findall('<img src="?\'?([^"\'>]*)', str)
    if len(c)==1:
        cc = c[0].split(".")
        if "gif" in cc or "jpg" in cc or "png" in cc:
            str='<img src="{}"  style="width:304px;height:228px;">'.format(c[0])
    return str
@app.route("/")
def hello():
    text[2] = "<head>"
    in_ip = request.remote_addr
    if in_ip not in ip_dict:
        ip_dict.update({in_ip:"Your name"})
        text[2] = "<head><script>alert(\"welcome! {}\");</script>".format(in_ip)
        text[72] = '<label >Your Name:</label> <input style="color:darkblue" type="text" name="fname" id="123" value="{}">'.format("Your name")
        text[64] = "<h1 id=""demo"">【{}】 welcome! ( ◕‿‿◕ ) </h1>".format("yourname")
    else:
        text[72] = '<label >Your Name:</label> <input style="color:darkblue" type="text" name="fname" id="123" value="{}">'.format(ip_dict[in_ip])
        text[64] = "<h1 id=""demo"">【{}】 welcome! ( ◕‿‿◕ ) </h1>".format(ip_dict[in_ip])
    return "".join(text)
@app.route("/input",methods=[ 'POST'])
def do():
    in_ip = request.remote_addr
    rec_name = request.form['fname']
    if in_ip in ip_dict:
        if ip_dict[in_ip]=="Your name":
            ip_dict[in_ip]=rec_name;
    rec=request.form['sendtext']
    rec=check_url_img(rec)

    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    add_list.append("{}【{}】:{}".format(now_time,rec_name,rec))
    print("{} {}【{}】:{}".format(in_ip,now_time,rec_name,rec))
    text[80]="<p>{}".format("<br>".join(add_list))
    text[72]='<label >Your Name:</label> <input style="color:darkblue" type="text" name="fname" id="123" value="{}">'.format(ip_dict[in_ip])
    text[64]="<h1 id=""demo"">【{}】 welcome! ( ◕‿‿◕ ) </h1>".format(ip_dict[in_ip])
    # list.append('{}:{}'.format(name,rtext))
    # print(list)
    #return "<br>".join(list)
    return  redirect(url_for('hello'))
if __name__ == "__main__":
    app.run(host='192.168.1.6',port=2914,threaded=True,debug=0)