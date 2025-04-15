from flask import Flask

from src.lib.weather import will_it_rain
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():

    current_year = datetime.now().year
    may_eve_rains = will_it_rain(f"{current_year}-04-30")
    may_day_rains = will_it_rain(f"{current_year}-05-01")

    return "<p>Sataako vappuna?</p> <p>Vappuaattona: {may_eve_rains}</p> <p>Vappupäivänä: {may_day_rains}</p>".format(
        may_eve_rains=may_eve_rains, may_day_rains=may_day_rains
    )


if __name__ == "__main__":
    app.run(debug=True)
