import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR,'static')
images_dir = os.path.join(static_dir,'images')
ImageFileName = os.path.join(images_dir,'django.jpeg')


print(ImageFileName)
img_data = open(ImageFileName, 'rb').read()
msg = MIMEMultipart()
msg['Subject'] = 'Attachment Test Email | Dibyalok'
msg['From'] = 'radical2018python@gmail.com'
msg['To'] = 'the.divyalok@gmail.com'
text = MIMEText("test")
msg.attach(text)
image = MIMEImage(img_data, name=os.path.basename(ImageFileName))
msg.attach(image)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login('radical2018python@gmail.com','VERIton_007')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
