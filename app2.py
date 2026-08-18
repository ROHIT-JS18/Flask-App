from flask import Flask, request, render_template , redirect , url_for ,flash 

app = Flask(__name__)

app.secret_key = "supersecret"


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        message = request.form.get("message")

        return render_template(
            "thankyou.html",
            user=name,
            message=message
        )

    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)