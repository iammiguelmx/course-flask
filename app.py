from flask import Flask
from flask import render_template

import forms

app = Flask(__name__)

@app.route('/')
def index():
    commennt_form = forms.ComentForm()
    title = "Curso Flask"
    return render_template('index.html', title = title)
    
if __name__ == '__main__':
    app.run(debug = True, port = 5000)