# -*- coding: utf-8 -*-

"""

    use flask to debug the page
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :Created: 2016/10/26
    :Copyright: (c) 2016<chenbo@nsfocus.com>

"""


from flask import Flask, render_template


app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
