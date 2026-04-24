from flask import Flask, render_template

from src.lib.weather import will_it_rain, when_will_it_rain
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():

    current_year = datetime.now().year
    may_eve_rains = will_it_rain(f"{current_year}-04-30")
    may_day_rains = will_it_rain(f"{current_year}-05-01")

    if may_eve_rains is None:
        may_eve_rains = "No data available"
    else:
        may_eve_rains = "sataa" if may_eve_rains else "ei sada"

    if may_day_rains is None:
        may_day_rains = "No data available"
    else:
        may_day_rains = "sataa" if may_day_rains else "ei sada"

    may_eve_rain_times = when_will_it_rain(f"{current_year}-04-30")
    may_day_rain_times = when_will_it_rain(f"{current_year}-05-01")

    return render_template(
        "index.html",
        may_eve_rains=may_eve_rains,
        may_day_rains=may_day_rains,
        may_eve_rain_times=may_eve_rain_times,
        may_day_rain_times=may_day_rain_times,
    )


if __name__ == "__main__":
    app.run(debug=True)
