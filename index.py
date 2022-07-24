from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/report')
def report():

    if request.args.get('password').islower() == True:
        first = "You did not use an upper case letter"
    else:
        first = ""
    if request.args.get('password').isupper() == True:
        second = "You did not use a lower case letter"
    else:
        second = ""
    if request.args.get('password')[-1].isnumeric():
        third = ""
    else:
        third = "You did not use a number at the end"
    if len(request.args.get('password')) < 8:
        fourth = "Your password is not long enough"
    else:
        fourth = ""
    if first == "" and second == "" and third == "" and fourth == "":
        message = "Your Password passed the 3 requirements!"
    else:
        message = ""
    return render_template('report.html', first=first, second=second, third=third, fourth=fourth, message=message)



if __name__ == '__main__':
    app.run(debug=True)
