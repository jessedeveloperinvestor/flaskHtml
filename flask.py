from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Do something with the form data (e.g. save to database)
        # ...
        # Redirect to a thank-you page
        return render_template('thankyou.html')
    else:
        # Display the form
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)