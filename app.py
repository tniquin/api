from flask import Flask,flash
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!/ Olá Mundo!'

@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/soma/<int:num1>+<int:num2>')
def soma(num1, num2):
    try:
        if num1 and num2 == int:
            soma = f'{num1} + {num2} = {num1 + num2}'

            return soma
        else:
            return f'Ocorreu um erro'
    except TypeError:
        return f'Tipo Inválido!'
    except ValueError:
        return f'Houve um erro'

@app.route('/subtrair/<int:num1>-<int:num2>')
def subtrair(num1, num2):
    try:
        if num1 and num2 == int:
            return f'{num1} - {num2}  = {num1 - num2}'
        else:
            return f'Ocorreu um erro'
    except TypeError:
        return f'Tipo Inválido!'
    except ValueError:
        return f'Houve um erro'

@app.route('/multiplicar/<int:num1>*<int:num2>')
def multiplicar(num1, num2):
    try:
        if num1 and num2 == int:
            return f'{num1} x {num2}  = {num1 * num2}'
        else:
            return f'Ocorreu um erro'
    except TypeError:
        return f'Tipo Inválido!'
    except ValueError:
        return f'Houve um erro'

@app.route('/dividir/<int:num1>/<int:num2>')
def dividir(num1, num2):
    try:
        if num1 and num2 == int:
            return f'{num1} / {num2}  = {num1 / num2}'
        else:
            return f'Ocorreu um erro'
    except TypeError:
        return f'Tipo Inválido!'
    except ValueError:
        return f'Houve um erro'
@app.route('/parouímpar/<int:num>')
def par_impar(num):
    try:
        if num == int:
            if num % 2 == 0:
                return f'{num} é par!'
            elif num == 0:
                return f'{num} é neutro!'
            else:
                return f'{num} é ímpar!'
    except TypeError:
        return f'Tipo Inválido!'
    except ValueError:
        return f'Houve um erro'

if __name__ == '__main__':
    app.run(debug=True)