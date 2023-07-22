from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/home", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        marks = request.form.getlist('marks',type=int)
        credits = request.form.getlist('credits',type=int)
        cgpa = 0
        for i in range(len(marks)):
            if marks[i] >= 90 and marks[i] <= 100:
                cgpa += 10 * credits[i]
            elif marks[i] >= 75 and marks[i] <= 89:
                cgpa += 9 * credits[i]
            elif marks[i] >= 65 and marks[i] <= 74:
                cgpa+=8*credits[i]
            elif marks[i] >= 55 and marks[i] <= 64:
                cgpa += 7 * credits[i]
            elif marks[i] >= 50 and marks[i] <= 54:
                cgpa += 6 * credits[i]
            elif marks[i] >= 45 and marks[i] <= 49:
                cgpa += 5 * credits[i]
            elif marks[i]>=40 and marks[i]<=44:
                cgpa += 4 * credits[i]
        cgpa /= sum(credits)
        return redirect(url_for('cgpa', cgpa=cgpa))
    
    elif request.method == 'GET':
        return render_template('home.html')


@app.route('/home/cgpa/<cgpa>')  
def cgpa(cgpa=0):
    return render_template('res.html', cgpa=cgpa)


if __name__ == "__main__":
    app.run()

















