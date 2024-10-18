from flask import Flask
from app import views

app = Flask(__name__)

app.add_url_rule(rule = '/', endpoint = 'app', view_func = views.app)
app.add_url_rule(rule = '/diabetic/', endpoint = 'diabeticapp', view_func = views.diabeticApp, methods = ['GET','POST'])

if __name__ == '__main__':
    app.run(debug=True)