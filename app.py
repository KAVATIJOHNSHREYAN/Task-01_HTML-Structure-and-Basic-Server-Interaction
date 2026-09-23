import json
import os
import re
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
# Secret key for session management and flash messages
app.secret_key = 'smart_contact_portal_super_secret_key_cognifyz'

# File storage configuration (Use /tmp on Vercel read-only serverless environment)
if os.environ.get('VERCEL'):
    DATA_DIR = '/tmp/data'
else:
    DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

DATA_FILE = os.path.join(DATA_DIR, 'submissions.json')


def ensure_data_file_exists():
    """Ensure the data directory and submissions.json file exist."""
    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR, exist_ok=True)
        
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=4)
    except Exception as e:
        print(f"Warning: File system write restricted: {e}")


def load_submissions():
    """Load all submissions from the JSON file safely."""
    ensure_data_file_exists()
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, PermissionError):
        return []


def save_submission(submission_data):
    """Append a new submission entry to the JSON file safely."""
    submissions = load_submissions()
    submissions.append(submission_data)
    try:
        ensure_data_file_exists()
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(submissions, f, indent=4)
    except Exception as e:
        print(f"File save bypassed on read-only serverless environment: {e}")


def validate_form(data):
    """
    Perform server-side validation on submitted form data.
    Returns a tuple: (is_valid, error_message)
    """
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    # 1. Empty field checks
    if not name or not email or not phone or not subject or not message:
        return False, "All fields are required. Please fill out every field."

    # 2. Full Name validation (at least 2 characters)
    if len(name) < 2:
        return False, "Full Name must be at least 2 characters long."

    # 3. Email format regex validation
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_pattern, email):
        return False, "Please enter a valid email address (e.g., user@example.com)."

    # 4. Phone number validation (digits with optional leading +, spaces, or dashes, 7-15 digits total)
    clean_phone = re.sub(r'[\s\-()]', '', phone)
    phone_pattern = r'^\+?[0-9]{7,15}$'
    if not re.match(phone_pattern, clean_phone):
        return False, "Please enter a valid phone number (7 to 15 digits)."

    # 5. Subject length validation
    if len(subject) < 3:
        return False, "Subject must be at least 3 characters long."

    # 6. Message length validation
    if len(message) < 10:
        return False, "Message must be at least 10 characters long."

    return True, ""


@app.context_processor
def inject_year():
    """Inject current year dynamically into templates for footer copyright."""
    return {'current_year': datetime.now().year}


@app.route('/', methods=['GET'])
def home():
    """Renders the landing home page with contact form."""
    form_data = session.pop('form_data', None)
    return render_template('index.html', form_data=form_data)


@app.route('/contact', methods=['POST'])
def contact():
    """Handles contact form submission, performs server validation, saves to JSON, and redirects."""
    form_data = {
        'name': request.form.get('name', '').strip(),
        'email': request.form.get('email', '').strip(),
        'phone': request.form.get('phone', '').strip(),
        'subject': request.form.get('subject', '').strip(),
        'message': request.form.get('message', '').strip()
    }

    # Validate form input server-side
    is_valid, error_msg = validate_form(form_data)
    if not is_valid:
        flash(error_msg, 'danger')
        session['form_data'] = form_data
        return redirect(url_for('home', _anchor='contact'))

    # Prepare submission object with unique ID & timestamp
    submission_entry = {
        'id': f"SUB-{uuid.uuid4().hex[:8].upper()}",
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'name': form_data['name'],
        'email': form_data['email'],
        'phone': form_data['phone'],
        'subject': form_data['subject'],
        'message': form_data['message']
    }

    # Persist to JSON storage (/tmp on Vercel)
    save_submission(submission_entry)

    # Store submission details in session for success display
    session['latest_submission'] = submission_entry
    flash('Your message has been submitted successfully!', 'success')

    return redirect(url_for('success'))


@app.route('/success', methods=['GET'])
def success():
    """Renders the success confirmation page displaying submitted details."""
    submission = session.get('latest_submission', None)
    return render_template('success.html', submission=submission)


if __name__ == '__main__':
    ensure_data_file_exists()
    print("==================================================")
    print("[*] Smart Contact Portal Server is starting...")
    print("[*] Access Application: http://127.0.0.1:5000")
    print("==================================================")
    app.run(debug=True, host='127.0.0.1', port=5000)
