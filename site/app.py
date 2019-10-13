from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():'
    user = {'username': 'Luna'}
    return '''
<html>
<head><title>Flask Playground</title></head>
<body>
    <h1>Welcome, ''' + user['username'] + '''</h1>
</body></html>




