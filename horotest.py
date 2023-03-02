import requests
import datetime

# Username is your own name(first or last)
username = input("Enter your name: ")
day = datetime.datetime.now()

# main function, runs first
def main():
    horoscope_message_ = horoscope_message()
    print(day)
    print()
    with open(f"({day}).txt", 'wb') as file:
        file.write(horoscope_message())

# Returns your horoscope sign name
def horoscope_name():
    name = input("Please enter your horoscope name: ")
    return name

# request code that pulls up your current horoscope message from the website
def horoscope_message():
    url = f'https://www.astrosage.com/horoscope/daily-{horoscope_name()}-horoscope.asp'
    r = requests.get(url)
    return r.json


if __name__=="__main__":
    main() 