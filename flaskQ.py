from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    numbers = []
    for n in range(0,10):
        numbers.append(n)

    dic = {'name': 'みね', 'age': '21', 'address': '茨城県'}

    gender = True

    return render_template('flaskQ.html', numbers=numbers, dic=dic, gender=gender)


if __name__ == '__main__':
    app.run(debug=True, port=8000)