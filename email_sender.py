import smtplib 
from email.message import EmailMessage

email = EmailMessage()
email['froom'] = 'Ayeloja Ibrahim'
email['to'] = '_ayelojahbd01@gmail.io'
email['subject'] = 'You just got employed after passing your interview'

email.set_content('Congratulations to you WOW!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ayelojafrom@gmail.net' , '$%&T^*()%&^*')
    smtp.send_message(email)
    print("went all good!")