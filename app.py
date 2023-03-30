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
@app.route('/')
def index():
    lox='thhWqxAVtvXygH7VukqgQqIbu342'
    datas=db.child("User").child(lox).child('Notes').get()
    return render_template('index.html',datas=datas)
app.run(debug=True)
 