from flask import Flask, render_template, send_file
app = Flask('app')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/clubhouse')

def clubhouse():
  return render_template("clubhouse.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def server_overloaded(e):
    return render_template('500.html'), 500

app.run(host='0.0.0.0', port=8080)