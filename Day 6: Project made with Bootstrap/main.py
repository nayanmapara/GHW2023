from flask import Flask, render_template, request, redirect, url_for
from funcs.custom_random import gen_random_range

app = Flask(__name__,template_folder='static')

@app.route("/") # index page
def index():
    return render_template('index.html')

@app.route("/day1")
def day1():
    return render_template('day1.html')

@app.route("/day2")
def day2():
    return render_template('day2.html')

@app.route("/day3")
def day3():
    return render_template('day3.html')

@app.route("/day4")
def day4():
    return render_template('day4.html')
    
@app.route("/day5", methods=["GET","POST"])
def day5():
    if request.method == "POST":
        req = request.form
        min = req['min']
        max = req['max']
        number = gen_random_range(int(min),int(max))
        return render_template('day5.html',number=number)
    return render_template('day5.html')

@app.route("/day6")
def day6():
    return render_template('day6.html')

@app.route("/day7")
def day7():
    return render_template('day7.html')
  
  
app.run(host='0.0.0.0', port=81)