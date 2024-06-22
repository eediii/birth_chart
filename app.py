from flask import Flask, render_template, request # type: ignore
from kerykeion import AstrologicalSubject # type: ignore

app = Flask(__name__)

class Report:
    def __init__(self, instance: AstrologicalSubject):
        self.instance = instance

    def get_planets_table(self):
        planets_data = [
            [planet.name, planet.sign] for planet in self.instance.planets_list
        ]
        return planets_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    name = request.form['name']
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    hour = int(request.form['hour'])
    minute = int(request.form['minute'])
    city = request.form['city']
    nation = request.form['nation']

    subject = AstrologicalSubject(name, year, month, day, hour, minute, city, nation)
    report = Report(subject)
    planets_table = report.get_planets_table()

    return render_template('report.html', planets_table=planets_table)

if __name__ == "__main__":
    app.run(debug=True)
