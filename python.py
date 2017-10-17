from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/', methods = ['GET', 'POST'])
def root():


    return render_template('textbox.html') 

@my_app.route('/greeting', methods = ['POST', 'GET'])
def greeting():
    return render_template('greeting.html',name = request.form['yourname'], methodtype = request.method)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()