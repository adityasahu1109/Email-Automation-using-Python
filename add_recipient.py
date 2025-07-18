import json
import os

RECIPIENTS_FILE = "recipients.json"

def add_email(new_email):
    try:
        # Initialize email list
        emails = []
        
        # Check if file exists and is not empty
        if os.path.exists(RECIPIENTS_FILE) and os.path.getsize(RECIPIENTS_FILE) > 0:
            with open(RECIPIENTS_FILE, "r") as f:
                try:
                    emails = json.load(f)
                except json.JSONDecodeError:
                    print("⚠️ Recipients file is corrupted. Starting new list.")
                    emails = []
        
        # Check if email already exists
        if new_email in emails:
            print(f"⚠️ {new_email} already exists in the list")
            return False
        
        # Add new email
        emails.append(new_email)
        
        # Save updated list
        with open(RECIPIENTS_FILE, "w") as f:
            json.dump(emails, f, indent=2)
        
        print(f"✅ Added {new_email} successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    print("\n📧 Email Address Adder")
    print("----------------------")
    
    while True:
        # Get email from user
        email = input("\nEnter email address to add: ").strip()
        
        # Basic email validation
        if "@" not in email or "." not in email.split("@")[-1]:
            print("❌ Invalid email format. Please try again.")
            continue
        
        # Add the email
        add_email(email)
        
        # Ask if user wants to add more
        while True:
            choice = input("\nAdd another email? (y/n): ").strip().lower()
            if choice in ['y', 'n', 'yes', 'no']:
                break
            print("❌ Please enter 'y' or 'n'")
        
        if choice.startswith('n'):
            print("\n✅ Finished adding email addresses!")
            break

if __name__ == "__main__":
    main()