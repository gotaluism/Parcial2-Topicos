from flask import Flask

app = Flask(__name__)

def proceso(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * proceso(n-1)

@app.route('/factorial/<string:number>')
def factorial(number):
    number=int(number)
    if number < 0:
        return 'No se puede por ser número negativo'
    else:
        result = proceso(number)
        return 'El resultado es (' + str(result) + ')   Hecho por Luis Miguel'

if __name__ == '__main__':
    app.run(debug=True)
