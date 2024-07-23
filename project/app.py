from flask import Flask, render_template, request

app = Flask(__name__)

# Base de conocimiento (reglas)
def diagnosticar(sintomas):
    if 'fiebre' in sintomas and 'tos' in sintomas and 'dolor muscular' in sintomas:
        return "El paciente podría tener gripe."
    elif 'fiebre' in sintomas and 'dolor de cabeza' in sintomas and 'rigidez en el cuello' in sintomas:
        return "El paciente podría tener meningitis."
    elif 'fiebre' in sintomas and 'dolor abdominal' in sintomas and 'náuseas' in sintomas:
        return "El paciente podría tener apendicitis."
    elif 'tos' in sintomas and 'dificultad para respirar' in sintomas and 'dolor en el pecho' in sintomas:
        return "El paciente podría tener neumonía."
    elif 'fatiga' in sintomas and 'pérdida de apetito' in sintomas and 'ictericia' in sintomas:
        return "El paciente podría tener hepatitis."
    else:
        return "Los síntomas no coinciden con ninguna enfermedad conocida."

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnostico = ""
    if request.method == 'POST':
        sintomas = request.form.getlist('sintomas')
        diagnostico = diagnosticar(sintomas)
    return render_template('index.html', diagnostico=diagnostico)

if __name__ == '__main__':
    app.run(debug=True)
