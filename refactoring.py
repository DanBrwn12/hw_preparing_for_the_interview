import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class WorkingWithMail:
    def __init__(self, login, password, subject, recipients, message, header=None, smtp_server="smtp.gmail.com",
        imap_server="imap.gmail.com"):
        self.smtp_server = smtp_server
        self.imap_server = imap_server
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header

    def send_message(self):
        msg = MIMEMultipart()
        msg["From"] = self.login
        msg["To"] = ", ".join(self.recipients)
        msg["Subject"] = self.subject
        msg.attach(MIMEText(self.message))


        ms = smtplib.SMTP(self.smtp_server, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, msg.as_string())

        ms.quit()

    def receive_message(self):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")

        criterion = f"(HEADER Subject '{self.header}')" if self.header else "ALL"
        result, data = mail.uid("search", None, criterion)

        assert data[0], "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid("fetch", latest_email_uid, "(RFC822)")

        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)

        mail.logout()
        return email_message


if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    wwm = WorkingWithMail(login, password, subject, recipients, message)
    wwm.send_message()