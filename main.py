from flask import Flask,jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dev')
def dev():
    return 'This is Dev Env'

@app.route('/stage')
def stage():
    return 'This is Staging Env'

@app.route('/num/<int:n>')
def number(n):
    if n%2 == 0:
        result = {
            "Number":n,
            "OddOrEven":"Even"
        }
    else:
        result = {
            "Number":n,
            "OddOrEven":"Odd"
        }
    return jsonify(result)


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)