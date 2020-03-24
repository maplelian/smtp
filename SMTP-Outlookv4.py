import getpass
import smtplib
from smtplib import SMTPException
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = input("Please enter your email address: ")
password = getpass.getpass()
smtpServer = "smtp.outlook.com"
port = 587

def get_contacts(filename):
    names = []
    emails = []
    models = []
    sns = []
    ids = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split(',')[0])
            emails.append(a_contact.split(',')[1])
            models.append(a_contact.split(',')[2])
            sns.append(a_contact.split(',')[3])
            ids.append(a_contact.split(',')[4])
    return names, emails, models, sns, ids

def main():
    names, emails, models, sns, ids = get_contacts('contacts.txt')
    smtpObj = smtplib.SMTP(smtpServer,port)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(sender, password)

    for name, email, model, sn, id in zip(names, emails, models, sns, ids):
        msg = MIMEMultipart()
        message_template ="""

        Dear {}

        
        Your laptop model: {}
        Laptop Serial Number: {}
        Ali Asset ID: {}

        
        Best Regards,
        
        """.format((name), (model), (sn), (id))
        message = message_template
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