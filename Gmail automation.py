import smtplib as s                ## import smtp
ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
your_email = input(" Enter your email id..")
your_password = input(" enter your password..")

ob.login(your_email, your_password)

subject = " test Python"
body = " i love python"
msg = " subject:{} \n\n".format(subject, body)

list_add = [" sujeet757464@gmail.com",
           "sujeet5776@gmail.com"]

ob.sendmail(your_email, list_add, msg)

print(" send mail ")

ob.quit()



