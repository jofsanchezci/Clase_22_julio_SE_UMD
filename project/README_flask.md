
# Sistema Experto de Diagnóstico Médico

Este proyecto es una implementación de un sistema experto de diagnóstico médico utilizando Flask. Permite a los usuarios seleccionar síntomas y recibir un diagnóstico basado en reglas predefinidas.

## Requisitos

- Python 3.7 o superior
- Flask

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/sistema-experto-diagnostico-medico.git
   cd sistema-experto-diagnostico-medico
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. Instala las dependencias requeridas:

   ```bash
   pip install flask
   ```

## Estructura del Proyecto

```
sistema-experto-diagnostico-medico/
├── app.py
└── templates/
    └── index.html
```

- **app.py**: Archivo principal de la aplicación Flask.
- **templates/index.html**: Plantilla HTML para la interfaz de usuario.

## Uso

1. Ejecuta la aplicación:

   ```bash
   python app.py
   ```

2. Abre tu navegador y navega a `http://127.0.0.1:5000/` para acceder a la interfaz de usuario.

3. Selecciona los síntomas que presenta el paciente y haz clic en "Diagnosticar" para recibir un diagnóstico.

## Código de la Aplicación

### app.py

```python
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
```

### templates/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Experto de Diagnóstico Médico</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 50%;
            margin: 50px auto;
            background: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-bottom: 10px;
        }
        input[type="checkbox"] {
            margin-right: 10px;
        }
        button {
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sistema Experto de Diagnóstico Médico</h1>
        <form method="POST">
            <label><input type="checkbox" name="sintomas" value="fiebre"> Fiebre</label>
            <label><input type="checkbox" name="sintomas" value="tos"> Tos</label>
            <label><input type="checkbox" name="sintomas" value="dolor de cabeza"> Dolor de cabeza</label>
            <label><input type="checkbox" name="sintomas" value="dolor muscular"> Dolor muscular</label>
            <label><input type="checkbox" name="sintomas" value="rigidez en el cuello"> Rigidez en el cuello</label>
            <label><input type="checkbox" name="sintomas" value="dolor abdominal"> Dolor abdominal</label>
            <label><input type="checkbox" name="sintomas" value="náuseas"> Náuseas</label>
            <label><input type="checkbox" name="sintomas" value="dificultad para respirar"> Dificultad para respirar</label>
            <label><input type="checkbox" name="sintomas" value="dolor en el pecho"> Dolor en el pecho</label>
            <label><input type="checkbox" name="sintomas" value="fatiga"> Fatiga</label>
            <label><input type="checkbox" name="sintomas" value="pérdida de apetito"> Pérdida de apetito</label>
            <label><input type="checkbox" name="sintomas" value="ictericia"> Ictericia</label>
            <button type="submit">Diagnosticar</button>
        </form>
        {% if diagnostico %}
        <div class="result">
            <strong>Diagnóstico:</strong> {{ diagnostico }}
        </div>
        {% endif %}
    </div>
</body>
</html>
```

## Contribuciones

Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
