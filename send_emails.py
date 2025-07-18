import os
import smtplib
import json
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_template():
    """Load email template from text file"""
    with open("message.txt", "r") as f:
        content = f.read()
    
    # Extract subject and body
    if content.startswith("Subject:"):
        subject_line, body = content.split("\n", 1)
        subject = subject_line.replace("Subject:", "").strip()
    else:
        subject = "Auto-generated Message"
        body = content
    
    return subject, body.strip()

def send_emails():
    """Send emails to all recipients"""
    # Load SMTP credentials
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT"))
    smtp_user = os.getenv("SMTP_USERNAME")
    smtp_pass = os.getenv("SMTP_PASSWORD")
    
    # Load recipients
    with open("recipients.json", "r") as f:
        recipients = json.load(f)
    
    # Load email template
    subject, body = load_template()
    
    # Connect to SMTP server
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            
            # Send to each recipient
            for email in recipients:
                msg = EmailMessage()
                msg["From"] = smtp_user
                msg["To"] = email
                msg["Subject"] = subject
                msg.set_content(body)
                
                server.send_message(msg)
                print(f"✉️ Sent to {email}")
                
            print("✅ All emails sent successfully!")
            
    except Exception as e:
        print(f"❌ SMTP Error: {str(e)}")

if __name__ == "__main__":
    send_emails()