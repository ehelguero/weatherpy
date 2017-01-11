import requests
import smtplib

def get_emails():

    emails = {}
    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:

            (email, name) = line.split(',')

            emails[email] = name.strip()

    except FileNotFoundError as err:

        print(err)

    return emails


def get_schedule():

    try:
        schedule_file = open('schedule.txt', 'r')

        schedule = schedule_file.read()

    except FileNotFoundError as err:

        print(err)

    return schedule


def send_emails(emails, schedule, forecast):
    email_from = 'xxx@gmail.com'
    email_to = 'email@test.es'
    # connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    # Start TLS encryption
    server.starttls()

    password = input('Whats your password')
    server.login(email_from, password)

    server.sendmail(email_from, email_to, 'Test Message')
    server.quit()


def get_weather_forecast():
    api_key = '--'
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid='
    url += api_key
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    return weather_json['weather'][0]['description']


def main():

    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    forecast = get_weather_forecast()

    send_emails(emails,schedule,forecast)

main()
