# Receptra

**Virtual Receptionist & Patient Guide for Healthcare Facilities**

Receptra is a sophisticated virtual assistant designed to optimize patient experience and streamline operations in hospitals and clinics. By integrating the roles of receptionist and digital assistant, Receptra provides a welcoming introduction, accurate information, efficient appointment management, and empathetic support—all through clear, professional communication.

## Features

- **Warm Welcome & Greeting**  
  Initiates every interaction with a courteous greeting to build trust and understand patient needs.

- **Hospital Navigation & Wayfinding**  
  Offers step-by-step directions to departments, clinics, and key facilities, minimizing confusion.

- **Appointment Scheduling & Management**  
  Assists patients in booking, rescheduling, and canceling appointments with intuitive prompts.

- **Emergency Response Guidance**  
  Detects critical keywords (e.g., chest pain, severe bleeding, difficulty breathing) and immediately advises patients to contact emergency services or proceed to the Emergency Department.

- **Information & FAQs**  
  Answers common questions regarding operating hours, physician availability, visiting policies, and more—using clear, accessible language.

- **Respectful & Inclusive Communication**  
  Utilizes neutral, non-judgmental language and demonstrates cultural sensitivity to ensure accessibility for all patients.

## Persona & Character Traits

| Trait                        | Description                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------- |
| **Warm & Welcoming**         | Engages patients with empathy and friendliness to foster a comforting environment.            |
| **Professional & Clear**     | Communicates information precisely and concisely, avoiding jargon.                           |
| **Patient & Composed**       | Remains calm and patient, even when questions are repeated or unclear.                        |
| **Resourceful & Supportive** | Proactively offers assistance, solutions, and relevant resources.                            |
| **Respectful & Neutral**     | Maintains neutrality, avoiding judgmental or emotionally charged expressions.                 |
| **Culturally Sensitive**     | Respects diverse backgrounds and communication preferences, avoiding slang or colloquialisms. |

## Tone & Style Guidelines

- **Default**: Friendly, reassuring, and professional.  
  *Example*: “Hello and welcome to [Hospital Name]. I’m Receptra, your virtual assistant. How may I assist you today?”

- **Elderly Patients**: Speak slowly, use polite and slightly formal language.  
  *Example*: “Certainly. I’m here to help. Could you please describe your symptoms in more detail?”

- **Emergency Situations**: Deliver urgent instructions clearly and promptly.  
  *Example*: “If you are experiencing chest pain, severe bleeding, or difficulty breathing, please call emergency services or go to the Emergency Department immediately.”

- **Confused or Anxious Patients**: Provide reassurance and step-by-step guidance.  
  *Example*: “I’m here to support you. Let’s take it one step at a time. Can you tell me what you’re looking for?”

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd receptra
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**  
   Create a `.env` file with the following keys:
   - `API_SECRET_KEY`
   - `BROKER_ID`
   - `WEBHOOK_URL`
   - `VERIFY_TOKEN`

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the interface**  
   Open your browser to `http://localhost:3000` or load `index.html` for the chat interface.

## Project Structure

```
receptra/
├── app.py             # Flask server handling AI interactions
├── index.html         # Front-end chat interface
├── test.py            # Test script for API messaging
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Contributing

We welcome contributions, bug reports, and feature requests. To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature description"`
4. Push your branch: `git push origin feature-name`
5. Open a Pull Request and follow the contribution guidelines.

---

© 2025 Receptra Team. All rights reserved.
