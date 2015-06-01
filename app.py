import json

from flask import (Flask, render_template, redirect,
                   url_for, request, make_response,
                   flash)

from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'fjfa#BBWY)W)%W%(YQUt53tq4jt1-0ti343fwFJASf"{WL'


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    return render_template('index.html', saves=get_saved_data())


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS
        )


@app.route('/save', methods=['POST'])
def save():
    flash('Alright: That looks awesome!')
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response


app.run(debug=True, host='127.0.0.1', port=8000)

#Response: A response is the data that the server, Flask, sends
#back to the client.

#make_response(): This function generates the entire response object
#that'll be sent back to the client, but lets you store it in a variable
#for further manipulation.

#response.set_cookie(): Sets a cookie on the response object.
#Takes name for the cookie and a value.

#json.dumps(): This method turns a Python data structure
#(list, string, dictionary, etc) into a JSON string.

#json.loads(): This method turns a JSON string into a Python object.
