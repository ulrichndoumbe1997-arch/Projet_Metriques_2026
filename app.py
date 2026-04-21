@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route("/contact")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.get("/paris")
def api_paris():
    # ... ton code API météo ...
    return jsonify(result)

@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")
