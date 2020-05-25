from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/echo/<value>')
def echo(value):
    name = value
    return f'Welcome: {name}'

@app.route('/testing/<name>/<place>')
def testing(name, place):
    n = name
    p = place
    return render_template('flasktest.html', name=n, place=p)


@app.route('/more/')
def more():
    kwargs = {}
    kwargs['name'] = request.args.get('name')
    kwargs['place'] = request.args.get('place')
    kwargs['food'] = request.args.get('food') + 's'
    return render_template('flasktest.html', **kwargs)

app.run(port=9999, debug=True)