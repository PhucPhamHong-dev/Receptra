Receptra

Virtual Receptionist & Patient Guide for Healthcare Facilities

Receptra is a scalable, Flask-based virtual assistant designed to enhance patient experiences at hospitals and clinics. It offers intuitive navigation, appointment handling, and responsive emergency guidance—all through a friendly chat interface.

📋 Table of Contents

Features

Demo

Prerequisites

Installation

Configuration

Running the Application

Project Structure

API & Webhook Endpoints

Available Routes

Contributing

License

Acknowledgements

✨ Features

Warm Welcome & Greeting: Builds rapport by greeting patients and capturing initial context.

Hospital Navigation & Wayfinding: Provides step-by-step directions to departments and services.

Appointment Management: Enables booking, rescheduling, and cancellations via simple commands.

Emergency Response Guidance: Detects critical phrases (e.g., chest pain) and prompts immediate emergency protocols.

Information & FAQs: Answers common queries about hours, physicians, and policies.

Inclusive Communication: Ensures culturally sensitive and accessible dialogue.

🎬 Demo

Coming soon: Link to live demo or screencast.

🔧 Prerequisites

Python: 3.9 or higher

Virtual Environment (optional but recommended): venv or virtualenv

🚀 Installation

Clone repository

git clone <repository-url>
cd Receptra

Create & activate virtual environment

python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.\.venv\Scripts\activate   # Windows

Install dependencies

pip install -r requirements.txt

⚙️ Configuration

Copy example environment file:

cp .env.example .env

Open .env and populate:

FPT_WEBHOOK_SECRET=your_webhook_secret
FPT_APP_TOKEN=your_app_token
FPT_WEBHOOK_URL=your_webhook_url
FPT_VERIFY_TOKEN=your_verify_token
FPT_BROKER_ID=your_broker_id
FPT_APP_CODE=your_app_code
FPT_TENANT_ID=your_tenant_id

▶️ Running the Application

Start the server:

python app.py

Visit http://localhost:3000/homepage in your browser.

🗂️ Project Structure

Receptra/
├── app.py               # Main Flask server
├── requirements.txt     # Dependency list
├── .env.example         # Sample environment variables
├── static/              # Static assets
│   ├── css/             # Stylesheets
│   └── img/             # Logo & backgrounds
└── templates/           # Jinja2 templates
    ├── homepage.html    # Landing page
    ├── chatbot.html     # Chat UI
    ├── services.html    # Services overview
    ├── about.html       # About page
    └── ourteam.html     # Team page

🔗 API & Webhook Endpoints

Method

Endpoint

Description

POST

/chat-api

Forward user messages with HMAC verification

GET

/indirect-channels/webhook/api

Verify webhook challenges

POST

/indirect-channels/webhook/api

Receive & process FPT webhook callbacks

GET

/latest-reply

Fetch the latest bot response from webhook storage

🌐 Available Routes

/homepage  — Landing page

/chat      — Chat interface

/services  — List of hospital services

/about     — Project background

/ourteam   — Team member details

🤝 Contributing

We welcome contributions! Please follow:

Fork the repo

Create branch feature/YourFeature

Commit changes: git commit -m "Add feature"

Push & open a PR

Refer to CONTRIBUTING.md for guidelines.

📜 License

© 2025 Receptra Team. All rights reserved.

🙏 Acknowledgements

Built with Flask

Powered by FPT AI services