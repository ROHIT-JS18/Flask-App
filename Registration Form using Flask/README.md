# Flask User Registration Form

A simple Flask web application with a user registration form (name, city, phone number)
that submits data to the server and displays it back on a confirmation page.

## Folder Structure
```
FlaskForm-YourName/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    ├── form.html
    └── confirmation.html
```

## Setup & Run

1. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## How It Works
- `GET /` → Renders `form.html`, the registration form.
- `POST /submit` → Reads `name`, `city`, and `phone` from the submitted form
  and renders `confirmation.html` with the entered details.
