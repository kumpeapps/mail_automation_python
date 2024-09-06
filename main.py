import sys
import email
import logging
from params import Params

logging.basicConfig(
    filename="/var/vmail/scripts/mail_automation_python/mail_automation_python.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)
logger = logging.getLogger("message")
full_msg = sys.stdin.readlines()
# logger.debug(full_msg)

msg = email.message_from_string(full_msg.join())

to = msg['to']
from_email = msg['from']
subject = msg['subject']
body = msg['body']



logger.debug(f"To: {to}\nFrom: {from_email}\nSubject: {subject}\nBody:\n{body}")