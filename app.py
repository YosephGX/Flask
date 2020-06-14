from flask import Flask, render_template, request, url_for, redirect, flash
from flaskext.mysql import MySQL

app = Flask(__name__)
#CONFIGURAR BASE DE DATOS
app.config["MYSQL_DATABASE_HOST"] = "https://databases.000webhost.com/?_ga=2.1091313.1147072601.1592121241-1320264451.1591285083"
app.config["MYSQL_DATABASE_USER"] = "id14085261_rootbus"
app.config["MYSQL_DATABASE_PASSWORD"] = "IHue2<5CYQP&bIvO"
app.config["MYSQL_DATABASE_DB"] = "id14085261_busistem"
SQL = MySQL(app)

#SESION
app.secret_key = "mysecretkey"

@app.route("/")
def Index():
	Cursor = SQL.get_db().cursor()
	Cursor.execute("SELECT * FROM test")
	Data = Cursor.fetchall()
	return render_template("index.html", info = Data)

@app.route("/add_contact", methods=["POST"])
def Add():
	if request.method == "POST":
		name = request.form["name"]
		email = request.form["email"]
		print(name, email)
		Cursor = SQL.get_db().cursor()
		Cursor.execute("INSERT INTO test (name, email) VALUES (%s, %s)", (name, email))
		SQL.get_db().commit()
		flash("Informacion Agregada Correctamente")
		return redirect(url_for("Index"))

@app.route("/edit/<string:id>")
def Get(id):
	Cursor = SQL.get_db().cursor()
	Cursor.execute("SELECT * FROM test WHERE id = {0}".format(id))
	Data = Cursor.fetchall()
	return render_template("edit.html", Info = Data[0])

@app.route("/update/<string:id>", methods=["POST"])
def Update(id):
	if request.method == "POST":
		name = request.form["name"]
		email = request.form["email"]
	Cursor = SQL.get_db().cursor()
	Cursor.execute("UPDATE test SET name = %s, email = %s WHERE id = %s", (name, email, id))
	SQL.get_db().commit()
	flash("Informacion Actualizada Correctamente")
	return redirect(url_for("Index"))

@app.route("/delete/<string:id>")
def Delete(id):
	Cursor = SQL.get_db().cursor()
	Cursor.execute("DELETE FROM test WHERE id = {0}".format(id))
	SQL.get_db().commit()
	flash("Informacion Eliminada Correctamente")
	return redirect(url_for("Index"))

if __name__ == "__main__":
	app.run(port = 3000, debug = True)
