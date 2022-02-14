#!/usr/bin/env python3
import os, psutil, shutil, socket, sys
import emails

max_cpu_usage = 80
max_disk_avail = 20
max_mem_avail = 500
localhost_ip = "127.0.0.1"

def check_cpu_usage():
    usage = int(psutil.cpu_percent(interval=3))
    return usage > max_cpu_usage

def check_disk_usage():
    du = shutil.disk_usage('/')
    free = (du.free / du.total) * 100
    return free < max_disk_avail

def check_memory_usage():
    one_mb = 2 ** 20
    max_mem = one_mb * max_mem_avail
    mem_avail = psutil.virtual_memory().available
    return mem_avail < max_mem

def check_network():
    ip = socket.gethostbyname("localhost")
    return localhost_ip != ip

def generate_alert():
    alert = ''
    if check_cpu_usage():
        alert = 'Error - CPU usage is over 80%'
        send_email_alert(alert)
    if check_disk_usage():
        alert = 'Error - Available disk space is less than 20%'
        send_email_alert(alert)
    if check_memory_usage():
        alert = 'Error - Available memory is less than 500MB'
        send_email_alert(alert)
    if check_network():
        alert = 'Error - localhost cannot be resolved to 127.0.0.1'
        send_email_alert(alert)
    return alert

def send_email_alert(alert):
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(os.environ.get("USER")),
        "subject": alert,
        "body": "Please check your system and resolve the issue as soon as possible.",
        "attachment": None,
    }
    message = emails.generate_email(**content)
    emails.send_email(message)

def main(argv):
    alert = generate_alert()
    print(alert)

if __name__ == '__main__':
    main(sys.argv)