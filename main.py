from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Happy birthday!"

@app.route("/<string:name>",methods=['Get'])
def get(name):
    return "Happy Birthday, "+name+"!!!!"

if __name__ == "__main__":
    app.run(debug=True)
