# Energiekostenrechner

def energiekosten_berechnen(art, kosten_einheit, anzahl_mitarbeiter, laufzeit_jahre):
    """Berechnet die jährliche und gesamte Ersparnis."""

    anzahl_kw = 42

    if art == "verbrenner":
        ersparnis_pro_kw = 3
        jaehrliche_ersparnis = (
            kosten_einheit
            * anzahl_kw
            * anzahl_mitarbeiter
            * ersparnis_pro_kw
        )

    elif art == "elektro":
        ersparnis_pro_kwh = 8
        jaehrliche_ersparnis = (
            kosten_einheit
            * anzahl_kw
            * anzahl_mitarbeiter
            * ersparnis_pro_kwh
        )

    else:
        raise ValueError("Ungültige Art: bitte 'verbrenner' oder 'elektro' verwenden.")

    gesamtersparnis = jaehrliche_ersparnis * laufzeit_jahre

    return {
        "jaehrlich": jaehrliche_ersparnis,
        "gesamt": gesamtersparnis,
    }


if __name__ == "__main__":
    print("Energiekostenrechner")
    print("--------------------")
    art = input("Möchten Sie die Berechnung für Verbrenner oder Elektro durchführen? ").lower()
    kosten = float(input("Kosten pro Einheit (Liter oder kWh) in Euro: "))
    mitarbeiter = int(input("Anzahl der Mitarbeiter? "))
    laufzeit = int(input("Laufzeit in Jahren? "))
    ergebnis = energiekosten_berechnen(art, kosten, mitarbeiter, laufzeit)
    print(f"Jährlich: {ergebnis['jaehrlich']} Euro")
    print(f"Gesamt: {ergebnis['gesamt']} Euro")
