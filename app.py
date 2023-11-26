from flask import Flask, render_template
from subprocess import call

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

#-----------------cardio---------------->

@app.route('/cardio_details')
def cardio_details():
    return render_template('cardio_details.html')

@app.route('/cardio_details1')
def cardio_details1():
    return render_template('cardio_details1.html')

@app.route('/cardio_details2')
def cardio_details2():
    return render_template('cardio_details2.html')

@app.route('/cardio_details3')
def cardio_details3():
    return render_template('cardio_details3.html')

@app.route('/cardio_details4')
def cardio_details4():
    return render_template('cardio_details4.html')

#----------------------product---------------->

@app.route('/product_details')
def product_details():
    return render_template('product_details.html')

@app.route('/product_details1')
def product_details1():
    return render_template('product_details1.html')

@app.route('/product_details2')
def product_details2():
    return render_template('product_details2.html')

@app.route('/product_details3')
def product_details3():
    return render_template('product_details3.html')

@app.route('/product_details4')
def product_details4():
    return render_template('product_details4.html')

#--------------------weight-lifting-------------->

@app.route('/wt_details')
def wt_details():
    return render_template('wt_details.html')

@app.route('/wt_details1')
def wt_details1():
    return render_template('wt_details1.html')

@app.route('/wt_details2')
def wt_details2():
    return render_template('wt_details2.html')

@app.route('/wt_details3')
def wt_details3():
    return render_template('wt_details3.html')

@app.route('/wt_details4')
def wt_details4():
    return render_template('wt_details4.html')

#--------------------yoga-------------->

@app.route('/yoga_details')
def yoga_details():
    return render_template('yoga_details.html')

@app.route('/yoga_details1')
def yoga_details1():
    return render_template('yoga_details1.html')

@app.route('/yoga_details2')
def yoga_details2():
    return render_template('yoga_details2.html')

@app.route('/yoga_details3')
def yoga_details3():
    return render_template('yoga_details3.html')

@app.route('/yoga_details4')
def yoga_details4():
    return render_template('yoga_details4.html')

#--------------------------------------->

import subprocess

@app.route('/execute')
def execute():
    subprocess.call(['python', 'AITrainerProject.py'])
    return "Python file executed successfully!"

@app.route('/execute1')
def execute1():
    subprocess.call(['python', 'AITrainerProject1.py'])
    return "Python file executed successfully!"

@app.route('/execute2')
def execute2():
    subprocess.call(['python', 'AITrainerProject2.py'])
    return "Python file executed successfully!"

if __name__ == '__main_pyth_':
    app.run()
    