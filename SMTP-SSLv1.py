import getpass
import smtplib
from smtplib import SMTPException
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = input("Please enter your email address: ")
password = getpass.getpass()
smtpServer = "smtp.****.com"
port = 465

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """"
    Return a Template object comprising the contents of the file.
    """
    with open(filename, mode='r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('email.txt')
    message_template = read_template('message.txt')
    smtpObj = smtplib.SMTP_SSL(smtpServer,port)
    smtpObj.login(sender, password)

    for name, email in zip(names, emails):
        msg = MIMEMultipart()
        message = message_template.substitute(PERSON_NAME=name.title())
        print(message)

        msg['From'] = sender
        msg['To'] = email
        msg['Subject'] = "Testing from python"

        msg.attach(MIMEText(message, 'plain'))

        smtpObj.send_message(msg)
        del msg

    smtpObj.timeout = 30000
    smtpObj.quit()
    print("Successfully sent mail")


if __name__ == '__main__':
    main()


#except SMTPException as e:
    #print(e)