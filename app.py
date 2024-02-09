from flask import Flask, request, render_template
import json
import os
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    correct_username = os.environ.get('SUBMISSIONS_USER', 'admin')
    correct_password = os.environ.get('SUBMISSIONS_PASS', 'admin')
    if username == correct_username and password == correct_password:
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def form():
    # Load form fields from JSON file
    with open('data/form_fields.json', 'r') as f:
        form_fields = json.load(f)

    success_message = None
    error_message = None
    if request.method == 'POST':
        # Validate form data
        for field in form_fields:
            if field['required'] and not request.form.get(field['name']):
                error_message = os.environ.get('ERROR_MESSAGE', 'Please fill out all required fields.')
                
        if error_message == None:
            # Save form data to JSON file
            form_data = request.form.to_dict()
            if os.path.exists('./data/form_data.json'):
                with open('./data/form_data.json', 'r') as f:
                    try:
                        data = json.load(f)
                    except Exception as e:
                        data = []
                data.append(form_data)
            else:
                data = [form_data]
            with open('./data/form_data.json', 'w') as f:
                json.dump(data, f, indent=4)
            
            success_message = os.environ.get('SUCCESS_MESSAGE', 'Form submitted successfully!')

    # Render form
    return render_template(
        'form.html', 
        fields=form_fields, 
        title=os.environ.get('FORM_TITLE', 'My Form'), 
        success_message=success_message,
        error_message=error_message, 
        button_text=os.environ.get('BUTTON_TEXT', 'Submit')
    )

@app.route('/submissions')
@auth.login_required
def submissions():
    with open('data/form_data.json', 'r') as f:
        submissions = json.load(f)
    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)