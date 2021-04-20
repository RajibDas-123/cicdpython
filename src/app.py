from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, You're seeing the modified code"

if __name__ == "__main__":
	app.run()
