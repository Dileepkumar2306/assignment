from flask import Flask,request,render_template

app = Flask(_name_)

@app.route('/', methods=['GET','POST'])
def home:
if request.method == 'POST':
    return f"<h2>Hello,!</h2><a href='/'>.Go back</a>"
return render_template('b.html')dd