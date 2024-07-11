from flask import Flask, redirect, url_for, render_template, request

# WSGI Application
app = Flask(__name__ )


@app.route('/')
def Welcome():
    return render_template('index_if.html')

@app.route('/members')
def members():
    return 'Welcome Members, we have created a separate url for you people'

@app.route('/success/<int:marks>')
def success(marks):
    return "The Student has passed and the mark is " + str(marks)

@app.route('/fail/<int:marks>')
def fail(marks):
    return "The Student has failed and the mark is " + str(marks)

@app.route('/results/<int:marks>')
def results(marks):
    return render_template("results_if.html", result = marks)

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        C = float(request.form['C'])
        Data_science = float(request.form['Data Science'])

        total_score = (science+maths+C+Data_science)/4

    return redirect(url_for('results',marks=total_score))


if __name__ == '__main__':
    app.run(debug=True)