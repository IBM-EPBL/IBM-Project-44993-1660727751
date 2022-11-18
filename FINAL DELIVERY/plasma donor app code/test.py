# from flask import Flask,request,flash,render_template
# from flask_mail import Mail,Message
# 
# app =Flask(__name__)
# mail=Mail(app)
# app.secret_key="123"
# 
# 
# def mail():
#         with app.app_context():
#                 print("working..")
#                 fmail='cse19.mohamedmahroof@petengg.ac.in'
#                 tmail ='cse19.rebison@petengg.ac.in'
#                 fpwd = 'MOHAMEDMAHROOF'
#                 message = 'Flask'
#                 body = 'Hello'
# 
#                 app.config['MAIL_SERVER']='smtp.gmail.com'
#                 app.config['MAIL_PORT']=465
#                 app.config['MAIL_USERNAME']='cse19.mohamedmahroof@petengg.ac.in'
#                 app.config['MAIL_PASSWORD']='MOHAMEDMAHROOF'
#                 app.config['MAIL_USE_TLS']=False
#                 app.config['MAIL_USE_SSL']=True
# 
#                 mail = Mail(app)
#                 msg=Message(message,sender='cse19.mohamedmahroof@petengg.ac.in',recipients=['cse19.rebison@petengg.ac.in'])
#                 msg.body=body
#                 mail.send(msg)
#                 flash("Mail Sented Successfully", 'success')
# 
# mail()
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cse19.mohamedmahroof@petengg.ac.in'
app.config['MAIL_PASSWORD'] = 'MOHAMEDMAHROOF'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'cse19.mohamedmahroof@petengg.ac.in', recipients = ['cse19.pradeesh@petengg.ac.in'])
   msg.body = "send panniyachi la mairuu"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
