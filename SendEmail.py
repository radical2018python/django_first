import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('radical2018python@gmail.com','VERIton_007')
smtpObj.sendmail('radical2018python@gmail.com','the.divyalok@gmail.com','Subject: So long.\nDear Dibyalok, so long and thanks for all the fish, Sincelery Dibyalok')
{}
smtpObj.quit()
