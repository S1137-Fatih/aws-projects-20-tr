from flask import Flask 
app = Flask(__name__)
@app.route('/')
def head():
     return 'marabalar'

@app.route('/secondpage')
def second():
     return 'This is second page'

@app.route('/third')
def third():
     return 'This is third page'

@app.route('/fourth/<string:id>')
def fourth(id):
     return f'This is fourth page is {id}'

if __name__ == '__main__':

     #app.run(debug=True,port=3000)
     app.run(host= '0.0.0.0', port=80)