import random
import string
import smtplib




def otp(size):
    generate_otp = ''.join(random.choice(string.digits) for n in range(size))
    return generate_otp

OTP=otp(4)

emailsender = input("Enter the Sender:")
emailreciver = input("Enter the reviver:")
password = input("Enter the pass:")

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(emailsender,password)
msg = 'Hello,Your OTP is '+str(OTP)
server.sendmail(emailsender, emailreciver, msg)
server.quit()
print(OTP)
print(msg)
print(server)