#!/usr/bin/env python3

import os, sys
import emails

def send_email(file):
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(os.environ.get("USER")),
        "subject": "Upload Completed - Online Fruit Store",
        "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "attachment": file,
    }
    message = emails.generate_email(**content)
    emails.send_email(message)

def main(argv):
    send_email(argv[1])

if __name__ == "__main__":
    main(sys.argv)