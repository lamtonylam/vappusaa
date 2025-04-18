from flask import Flask, render_template

from src.lib.weather import will_it_rain
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():

    current_year = datetime.now().year
    may_eve_rains = will_it_rain(f"{current_year}-04-30")
    may_day_rains = will_it_rain(f"{2026}-05-01")

    if may_eve_rains == None:
        may_eve_rains = "No data available"
    elif may_day_rains == None:
        may_day_rains = "No data available"

    return render_template(
        "index.html", may_eve_rains=may_eve_rains, may_day_rains=may_day_rains
    )


if __name__ == "__main__":
    app.run(debug=True)
