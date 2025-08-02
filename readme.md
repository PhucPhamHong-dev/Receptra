# Receptra

**Virtual Receptionist & Patient Guide for Healthcare Facilities**

Receptra is a Flask-based virtual assistant designed to enhance patient interactions in hospitals and clinics. It delivers a warm welcome, handles common inquiries, provides wayfinding assistance, and routes messages to an AI-powered backend for further help.

---

## 📌 Table of Contents

1. [🚀 Features](#-features)  
2. [🏁 Quick Start](#-quick-start)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Configuration](#configuration)  
   - [Running the Application](#running-the-application)  
3. [🗂️ Project Structure](#️-project-structure)  
4. [🔌 API & Webhook Integration](#-api--webhook-integration)  
5. [🛣️ Application Routes](#️-application-routes)  
6. [🤝 Contributing](#-contributing)  
7. [📄 License](#-license)  
8. [📚 References](#-references)

---

## 🚀 Features

- **Warm Welcome & First Contact**  
  Every conversation begins with a polite greeting, setting a tone of trust and clarity about patient needs.

- **Hospital Wayfinding & Navigation Support**  
  Patients receive clear directions to departments, clinics, and essential hospital facilities to minimize confusion.

- **Appointment Booking & Management**  
  Seamless flows for scheduling, rescheduling, or canceling appointments via intuitive prompts.

- **Emergency Guidance Protocol**  
  Detects critical keywords (e.g., *chest pain*, *severe bleeding*) and provides immediate advice to contact emergency services.

- **FAQs & Operational Info**  
  Provides details on opening hours, on-duty physicians, visitor policies, and more in clear, user-friendly language.

- **Inclusive & Sensitive Communication**  
  Uses neutral, culturally aware language designed for accessibility across all patient backgrounds.

---

## 🏁 Quick Start

### Prerequisites

- **Python 3.9 or newer**  
- *(Optional)* Virtual environment to isolate project dependencies

### Installation

```bash
git clone <repository-url>
cd Receptra
python3 -m venv .venv
# Activate the virtual environment:
#   macOS / Linux: source .venv/bin/activate
#   Windows: .venv\Scripts\activate
pip install flask requests python-dotenv markdown
```

### Configuration

Create a `.env` file based on `.env.example` and populate with your FPT AI webhook credentials:

```env
FPT_WEBHOOK_SECRET=...
FPT_APP_TOKEN=...
FPT_WEBHOOK_URL=...
FPT_VERIFY_TOKEN=...
FPT_BROKER_ID=...
FPT_APP_CODE=...
FPT_TENANT_ID=...
```

### Running the Application

```bash
python app.py
```

Access the interface in a browser:

- **Landing page:** `http://localhost:3000/homepage`  
- **Chat interface:** `/chat`

---

## 🗂️ Project Structure

```
Receptra/
├── app.py                 # Flask server & webhook handling
├── .env.example           # Sample environment variable template
├── static/                # Static files (CSS, images, etc.)
│   ├── css/
│   │   ├── body.css
│   │   └── header.css
│   └── img/               # Logos & background assets
└── templates/             # HTML templates
    ├── homepage.html      # Main landing page
    ├── chatbot.html       # Chatbot UI
    ├── services.html      # Overview of services
    ├── about.html         # Project description
    └── ourteam.html       # Team bios
```

---

## 🔌 API & Webhook Integration

- `POST /chat-api`  
  Proxies user messages to the FPT AI webhook, signed with HMAC SHA‑256. Returns a temporary placeholder while awaiting the webhook callback.  
- `GET /indirect-channels/webhook/api`  
  Handles verification requests from FPT AI.  
- `POST /indirect-channels/webhook/api`  
  Receives and processes webhook callbacks, storing the latest bot response retrievable by `GET /latest-reply`.

---

## 🛣️ Application Routes

| Endpoint        | Description                                         |
|------------------|-----------------------------------------------------|
| `/homepage`      | Landing page with navigation links                 |
| `/chat`          | Interactive chatbot UI (with prompt cards)         |
| `/services`      | Overview of hospital services                       |
| `/about`         | Background information about the project            |
| `/ourteam`       | Team member profiles and contact details            |

---

## 🤝 Contributing

We welcome contributions! To get involved:

1. Fork the repository  
2. Create a feature branch: `git checkout -b feature/YourFeature`  
3. Implement your changes and commit them  
4. Push to your fork and open a Pull Request  

---

## 📄 License

© 2025 Receptra Team. All rights reserved.