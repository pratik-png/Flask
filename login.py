from flask import Flask, render_template, request , url_for , redirect

app = Flask(__name__)

@app.route('/home', methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'reshu' and password == 'reshu':
            return redirect(url_for("name"))
        else:
            return "Login failed"
    return render_template("login_1.html")  # Display the login form initially for GET requests

@app.route("/name")
def name():
    return "Login Sucessfull"
if __name__ == '__main__':
    app.run(debug=True)
