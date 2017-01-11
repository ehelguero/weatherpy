import requests

def get_emails():

    emails = {}
    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:

            (email, name) = line.split(',')

            emails[email] = name.strip()

    except FileNotFoundError as err:

        print(err)

    return(emails)


def get_schedule():

    try:
        schedule_file = open('schedule.txt', 'r')

        schedule = schedule_file.read()

    except FileNotFoundError as err:

        print(err)

    return(schedule)


def get_weather_forecast():
    api_key = 'ba8ef5ff2050ddec43f2f7a53d944c9b'
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

    print(get_weather_forecast())


main()
