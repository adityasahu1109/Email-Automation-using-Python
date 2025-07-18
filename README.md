


# Email Automation System

A simple yet powerful Python-based email automation system that allows you to send personalized emails to multiple recipients using SMTP.

## Features

- **Bulk Email Sending**: Send emails to multiple recipients automatically 
- **Template-based Emails**: Load email content from template files with subject and body separation 
- **Recipient Management**: Add and manage email recipients with duplicate prevention  
- **Environment-based Configuration**: Secure SMTP credentials using environment variables 
- **Error Handling**: Comprehensive error handling for SMTP operations and file operations 
- **Email Validation**: Basic email format validation before adding to recipient list  

## Prerequisites

- Python 3.6 or higher
- SMTP server access (Gmail, Outlook, etc.)
- Required Python packages: `smtplib`, `json`, `python-dotenv`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/adityasahu1109/Email-Automation-using-Python.git
cd Email-Automation-using-Python
```

2. Install required dependencies:
```bash
pip install python-dotenv
```

3. Create a `.env` file in the root directory with your SMTP configuration:
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

## Configuration

### Environment Variables
Create a `.env` file with the following variables: 

- `SMTP_HOST`: Your SMTP server hostname
- `SMTP_PORT`: SMTP server port (typically 587 for TLS)
- `SMTP_USERNAME`: Your email address
- `SMTP_PASSWORD`: Your email password or app-specific password

### Email Template
Create a `message.txt` file with your email template: 

```
Subject: Your Email Subject Here

Your email body content goes here.
You can include multiple lines and formatting.
```

## Usage

### Adding Recipients

You can run the script in IDE directly or (in terminal) Run the recipient management script to add email addresses: 
```bash
python add_recipient.py
```

This script will:
- Prompt you to enter email addresses
- Validate email format
- Store recipients in `recipients.json`
- Prevent duplicate entries

### Sending Emails

Once you've added recipients and created your email template, send emails using:  

```bash
python send_emails.py
```

The script will:
- Load SMTP credentials from environment variables
- Read recipients from `recipients.json`
- Load email template from `message.txt`
- Send personalized emails to all recipients
- Provide status updates for each email sent

## File Structure

```
Email-Automation-using-Python/
├── send_emails.py          # Main email sending script
├── add_recipient.py        # Recipient management script
├── .env                    # Environment variables (create this)
├── message.txt            # Email template (create this)
├── recipients.json        # Recipients list (auto-generated)
└── README.md             # This file
```

## Required Files

You need to create these files:

1. **`.env`**: SMTP configuration 
2. **`message.txt`**: Email template with subject and body  
3. **`recipients.json`**: Will be auto-generated when you add recipients 

## Error Handling

The system includes robust error handling for:
- SMTP connection issues 
- Corrupted recipient files 
- Invalid email formats 
- General file operations

## Security Notes

- Use app-specific passwords for Gmail and other providers
- Keep your `.env` file secure and never commit it to version control
- Consider using OAuth2 for enhanced security in production environments

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.

## License

This project is open source and available under the MIT License.

## Notes

This is a straightforward email automation system built with Python's built-in libraries and minimal dependencies. The system uses SMTP with TLS encryption for secure email transmission and provides a simple interface for managing recipients and email templates. The code includes comprehensive error handling and user-friendly console output to guide users through the process.
