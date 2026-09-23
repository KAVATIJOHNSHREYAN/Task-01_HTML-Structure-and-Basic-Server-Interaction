# Smart Contact Portal 🌐

> **Cognifyz Tech Internship — Task 1: HTML Structure and Basic Server Interaction**

A complete, production-ready, and beginner-friendly web application built using **Python, Flask, Jinja2 Templates, HTML5, and vanilla CSS3**.

---

## 📌 Project Overview

The **Smart Contact Portal** demonstrates full-stack server-side web development fundamentals. It features a responsive landing page, interactive inquiry forms, strict server-side input validation, persistent local JSON storage, and a user-friendly submission confirmation workflow.

---

## ✨ Features

- **2026 Futuristic SaaS UI System**: Dark-space glassmorphic theme inspired by Linear, Vercel, and Stripe with backdrop blurs, glow accents, floating cards, Poppins + Inter typography, and Lucide icons.
- **Fixed Ambient Background**: Global high-resolution background with custom dark-space gradient overlay for visual depth and perfect text contrast across every route.
- **Interactive Contact Form**: Custom form fields for Full Name, Email, Phone Number, Subject, and Message with Lucide input prefixes.
- **Server-Side Rendering (SSR)**: Dynamic page generation using Jinja2 templates extending a single shared `base.html` layout.
- **Robust Backend Validation**:
  - Empty field check
  - Full Name minimum length validation
  - Standard regex Email address validation
  - Phone number digit length check
  - Message minimum length verification
- **JSON File Storage**: Automatically appends sanitized form submissions to `data/submissions.json` with unique submission IDs (`SUB-XXXXXX`) and timestamps.
- **Session-Based Success Page**: Confirms submitted data upon POST completion and redirects securely using the PRG (Post/Redirect/Get) pattern.

---

## 📁 Folder Structure

```text
Task-01_HTML-Structure-and-Basic-Server-Interaction/
│
├── app.py                  # Main Flask application & routes controller
├── requirements.txt        # Python dependency list
├── README.md               # Project documentation
│
├── templates/              # Jinja2 HTML Templates
│   ├── base.html           # Main layout boilerplate with floating glass navbar & footer
│   ├── index.html          # Landing page & glass contact form
│   └── success.html        # Submission confirmation page
│
├── static/                 # Static Assets
│   ├── style.css           # 2026 SaaS Glassmorphism CSS Design System
│   └── images/
│       └── bg-hero.jpg     # Global fixed dark-space background image
│
└── data/                   # Persistent Data Storage
    └── submissions.json    # JSON file storing form submissions
```

---

## 🛠️ Routes

| Route | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Renders the home landing page and contact form |
| `/contact` | `POST` | Validates submitted form data, saves to JSON, and redirects |
| `/success` | `GET` | Displays submission summary confirmation page |

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.8+ installed on your system.

### 2. Install Dependencies
Open your terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

To launch the Flask development server, execute:

```bash
python app.py
```

After starting, open your browser and navigate to:

👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 🌐 Live Production Deployment
👉 **[https://task-01-html-structure-server.vercel.app](https://task-01-html-structure-server.vercel.app)**


---

## 📷 Screenshots

### 1. Homepage & Contact Form
*(Insert screenshot of homepage hero and form here)*

### 2. Validation Error Notification
*(Insert screenshot of form error alert here)*

### 3. Submission Confirmation Page
*(Insert screenshot of success summary card here)*

---

## 🔮 Future Improvements

- **Database Integration**: Migrate JSON storage to SQLite or PostgreSQL via SQLAlchemy.
- **Email Notifications**: Send automated SMTP email receipts to users upon form submission.
- **Admin Dashboard**: Build a password-protected route to view and export submitted messages.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](file:///C:/Users/johns/Documents/A%20COGNIFYZ%20PROJECTS/Task-01_HTML-Structure-and-Basic-Server-Interaction/LICENSE) file for details.

This project is created for educational purposes as part of the Cognifyz Technologies Internship Program by **Kavati John Shreyan**.

