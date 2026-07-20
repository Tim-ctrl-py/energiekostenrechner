from flask import Flask, render_template, request
from rechner import energiekosten_berechnen


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def start():

    ergebnis = None

    if request.method == "POST":

        art = request.form["art"]

        kosten = float(request.form["kosten"])

        mitarbeiter = int(request.form["mitarbeiter"])

        laufzeit = int(request.form["laufzeit"])


        ergebnis = energiekosten_berechnen(
            art,
            kosten,
            mitarbeiter,
            laufzeit
        )


    return render_template(
        "index.html",
        ergebnis=ergebnis
    )


if __name__ == "__main__":
    app.run(debug=True)