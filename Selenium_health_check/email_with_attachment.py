import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

_USER = ""
_PWD = b''
_SMTP_SERVER = "smtp.office365.com"
_SENT_TO_LIST = ['']


def email_with_attachment(flag='Success'):
    try:
        msg = MIMEMultipart()
        ok_subject = "SUCCESS: Production running fine"
        err_subject = "ERROR: Check UMG Production"
        ok_body = "Application seems to be fine"
        err_body = "Got a SAML error! It often happens and doesnt necessarily mean system is down, please check manually"
        img_data = open('screenshot.png', 'rb').read()

        if flag == 'Success':
            msg.attach(MIMEText(ok_body, 'plain'))
            msg['Subject'] = ok_subject
        else:
            msg.attach(MIMEText(err_body, 'plain'))
            msg['Subject'] = err_subject
        msg.attach(MIMEImage(img_data))
        sendto = _SENT_TO_LIST
        user = _USER
        password = base64.b64decode(_PWD).decode("utf-8")
        smtpsrv = _SMTP_SERVER
        smtpserver = smtplib.SMTP(smtpsrv, 587)

        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(user, password)

        smtpserver.sendmail(user, sendto, msg.as_string())
        print('email sent')

    except:
        pass
    finally:
        smtpserver.close()


if __name__ == '__main__':
    email_with_attachment()
