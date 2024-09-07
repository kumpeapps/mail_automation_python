import sys
import email
import logging
from params import Params
import kumpeapi

# mail_automation_python/main.py ${sender} ${user} ${domain} ${extension}

sender = sys.argv[1]
to = sys.argv[2]
domain = sys.argv[3]
extension = sys.argv[4]

logging.basicConfig(
    filename="/var/vmail/scripts/mail_automation_python/mail_automation_python.log",
    filemode="a",
    format="%(asctime)s: [%(name)s] [%(levelname)s] %(message)s",
    level=Params.log_level(),
)
logger = logging.getLogger("message")

full_msg = ""
for line in sys.stdin:
    full_msg += line

msg = email.message_from_string(full_msg)
subject = msg["subject"]

# make an emty variable for email body
body = ""

# if the message contains attaachments find the body attachment
# if not find the entire emial body
if msg.is_multipart():
    for payload in msg.get_payload():
        # if payload.is_multipart(): …
        body = payload.get_payload()
else:
    body = msg.get_payload()

if domain == "automation.kumpeapps.com":
    kapi = kumpeapi.KAPI(
        apikey=Params.Web.ka_api_key, mysql_creds=Params.SQL.dict(), preprod=False
    )
    logger = logging.getLogger("automation")
    logger.debug("automation.kumpeapps.com")
    if to == "vinelink":
        logger = logging.getLogger("vinelink")
        logger.debug("vinelink")
        if (
            sender == "jakumpe@kumpes.com"
            or sender == "pm_bounces@pm-bounces.globalnotifications.com"
        ):
            logger.debug("sender")
            user_info = kapi.get_user_info(extension)
            user_id = user_info["user_id"]
            if "registered" in body:
                # New Encarceration
                logger.debug(f"New Encarceration for {extension}")
                kapi.add_access(user_id, 216, comment="Added by VineLink Bot")
            elif "released" in body:
                # Released
                logger.debug(f"{extension} Released")
                kapi.expire_access(user_id, 216, comment="Removed by VineLink Bot")
        else:
            logger.error(f"{sender} not allowed")
