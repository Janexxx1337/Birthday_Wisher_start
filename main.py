import pandas
import random
import smtplib
import datetime as dt

#
#
# my_email = 'krahs123@gmail.com'
# my_password = 'jvcmypmwsyorapfw'
#
# with smtplib.SMTP('smtp.gmail.com') as  connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs='krahs123@mail.ru',
#                         msg='Subject:Priviet\n\nThis is the body of my email')
#     connection.close()


motivation_msg = pandas.read_csv('quotes.txt').to_dict(orient="records")
random_message = random.choice(motivation_msg)


now = dt.datetime.now()
message_date_hours = 16
message_date_minutes = 23

current_hour = now.hour
current_minute = now.minute
print(current_minute)

if message_date_hours == current_hour and message_date_minutes == current_minute:
    my_email = 'krahs123@gmail.com'
    my_password = 'jvcmypmwsyorapfw'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs='krahs123@mail.ru',
                            msg=f'Subject:Priviet\n\n{random_message}')
        connection.close()



# now = dt.datetime.now()
# year = now.year
# day = now.day
# month = now.month
# day_of_the_week = now.weekday()
#
# print(hour)

