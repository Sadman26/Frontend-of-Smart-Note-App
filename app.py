from flask import *
import pyrebase
app = Flask(__name__,template_folder='temp')
firebaseConfig = {
  "apiKey": "AIzaSyAowhZs3yUIdWdsHwNvgicuasMg5XfNf9c",
  "authDomain": "carbon26xe.firebaseapp.com",
  "databaseURL": "https://carbon26xe-default-rtdb.firebaseio.com",
  "projectId": "carbon26xe",
  "storageBucket": "carbon26xe.appspot.com",
  "messagingSenderId": "449840099328",
  "appId": "1:449840099328:web:7f8b863ae6b4a46f8d68e5",
  "measurementId": "G-TSTE0TQN8X"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth=firebase.auth()
@app.route('/',methods=['POST','GET'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        try:
            user=auth.sign_in_with_email_and_password(email,password)
            if(user):
                return redirect(url_for('notes'))
        except:
            return render_template('login.html')
    return render_template('login.html')
@app.route('/homepage')
def notes():
    data=db.child('Admin_access').child('Notes').get()
    return render_template('index.html',datas=data)
app.run(debug=True)
 