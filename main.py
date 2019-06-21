from flask import Flask 
from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method ="Post">
        <label>Rotate by:</label>
        <input type="text" name="rot" value ="{1}" />
        <textarea name="text">{0}</textarea>
        <input type ="Submit"/>
      </form>

    </body>
</html>"""
@app.route("/", methods =['POST'])
def encrypted():
    text = rotate_string(request.form.get('text'),int(request.form.get('rot')))
    rot = request.form.get('rot')
    return form.format(text,rot)

@app.route("/", methods =['GET'])
def index():
    return form.format("","0")


app.run()