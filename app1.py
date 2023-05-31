from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='db'
db=SQLAlchemy(app)

@app.route("/")
def index():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM product")
    result=cur.fetch_all()
    cur.close()
    return render_template('report.html',product=result)
class Product(db.Model):
    prod_id=db.Columns(db.Integer, primary_key=True)

class Location(db.Model):
    loc_id=db.Columns(db.Integer, primary_key=True)

class ProdMovement(db.Model):
    movement_id=db.Columns(db.String(60),primary_key=True)
    timestamp=db.Columns(db.DateTime)
    from_loc=db.Columns(db.String(60),db.Foreign_key('location.loc_id'))
    to_loc=db.Columns(db.String(60),db.Foreign_key('location.loc_id'))
    prod_id=db.Columns(db.String(60),db.Foreign_key('product.prod_id'))
    qty=db.Columns(db.Integer)
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/prod/add",method=['GET','POST'])
def prod_add():
    if request.method=='POST':
     return render_template('prod.html')

@app.route("/prod/move",method=['GET','POST'])
def prod_move():
    if request.method=='POST':
     return render_template('movement.html')

@app.route("/prod/move",method=['GET','POST'])
def bal_report():
    if request.method=='POST':
     return render_template('report.html')

@app.route("/prod/edit",method=['GET','POST'])
def prod_add():
    if request.method=='POST':
     return render_template('prod.html')



@app.route("/about")
def aboutme():
    return "<p>This is about section</p>"

@app.route("/add")
def addproduct():
    return "<p>Products</p>"

if __name__ == '__main__':
    app.run(debug=True)

