import sys
import email
import logging
from params import Params

# mail_automation_python/main.py ${sender} ${user} ${domain} ${extension}

sender = sys.argv[1]
user = sys.argv[2]
domain = sys.argv[3]
extension = sys.argv[4]

logging.basicConfig(
    filename="/var/vmail/scripts/mail_automation_python/mail_automation_python.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)
logger = logging.getLogger("message")

full_msg = ''
for line in sys.stdin:
    full_msg += line

msg = email.message_from_string(full_msg)
logger.debug(msg)

to = msg['to']
from_email = msg['from']
subject = msg['subject']

#make an emty variable for email body
body = ""

#if the message contains attaachments find the body attachment
#if not find the entire emial body
if msg.is_multipart():
    for payload in msg.get_payload():
    # if payload.is_multipart(): …
        body = payload.get_payload()
else:
    body = msg.get_payload()



logger.debug(f"To: {user}\nFrom: {sender}\nDomain: {domain}\nExt: {extension}\nSubject: {subject}\nBody:\n{body}")