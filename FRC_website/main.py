from flask import Flask, render_template, request, redirect, flash

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'



db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def index2():
    return render_template('index.html')


@app.route('/oduller')
def oduller():
    return render_template('oduller.html')

@app.route('/gecmistemalar')
def gecmistemalar():
    return render_template('gecmis.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100), nullable=False)

    mesaj = db.Column(db.String(200), nullable=False)

    # Nesnenin ve kimliğin çıktısı
    def __repr__(self):
        return f'<Card {self.id}>'


@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == "POST":
       fullname = request.form.get("fullname")
       mesaj = request.form.get("mesaj")
       if fullname != "" and mesaj != "":
        card = Card(fullname=fullname, mesaj=mesaj)
            
        db.session.add(card)
        db.session.commit()

        flash("Mesajı gönderdiniz!","success")
       else:
        flash("İsim ve mesaj bilgilerini doldurunuz.","error")
       return redirect('/contact')
    else:   
        return render_template('contact.html')


if __name__ == "__main__":
    with app.app_context():
         db.create_all()
    app.run(debug=True)