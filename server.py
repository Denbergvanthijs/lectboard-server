import socket
from io import BytesIO

from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)
port = 5000
hostname = socket.gethostbyname(socket.gethostname())


@app.route("/")
@app.route("/index")
def show_index():
    return render_template("/index.html")


@app.route("/image", methods=["POST"])
def post_image():
    Image.open(BytesIO(request.data)).save("./static/result.png")


@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.cache_control.max_age = 0

    return response


@app.route("/hostname", methods=["GET"])
def get_host_ip() -> str:
    return {"hostname": hostname, "port": port}


if __name__ == "__main__":
    app.run(debug=True, port=port, host="0.0.0.0")
