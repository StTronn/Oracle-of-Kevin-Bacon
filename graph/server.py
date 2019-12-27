from flask import Flask
import queries
app = Flask(__name__)

@app.route("/api/<actor_name>")
def show_path(actor_name):
    ret=queries.get_path(actor_name)
    return {
        "path":ret,
    }    