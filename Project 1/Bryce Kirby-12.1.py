# DSC 510
# Week 12
#Programming Assignment Week 12
# Author Bryce Kirby
# 11/18/2023

import requests

# If user requests info by city
def by_city():
    city = input('Please enter city name: ')
    # where to request from- my API key
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=23caf59a438de59d16d366601b1a9918&units=imperial'.format(
        city)
    res = requests.get(url)
    ## transferring data to Json to be readable
    data = res.json()
    show_info(data)

    # If the user wants try the program again?
    question = input('Would you like to do another search? Type Yes or No: ').lower()
    if question == 'yes':
        main()
    if question == 'no':
        print("Thank you for using this program. Have a great day!")
        exit()


# If user requests info by zip code
def by_zip():
    zip_code = int(input('Please enter zip code: '))
    ## where to request from- my API key
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=23caf59a438de59d16d366601b1a9918'.format(
        zip_code)
    res = requests.get(url)
    # transferring data to Json to be readable
    data = res.json()
    show_info(data)

    # If the user wants try this program again?
    question = input('Would you like to do another search? Type Yes or No: ').lower()
    if question == 'yes':
        main()
    if question == 'no':
        print("Thank you for using this program. Have a nice day!")
        exit()


# This will show data based on the user's request.
def show_info(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    press = data['main']['pressure']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature is : {} degrees fahrenheit'.format(temp))
    print('High Temperature is : {} degrees fahrenheit'.format(hightemp))
    print('Low Temperature is : {} degrees fahrenheit'.format(lowtemp))
    print('Pressure is : {} hPa'.format(press))
    print('Humidity is : {} %'.format(humid))
    print('Description is : {}'.format(description))


# Main function
def main():
    print("Welcome to the weather program")
    print("Hope you enjoy the program ")

    while True:
        answer = input(
            "Bellow are the following options: \nChose 1 to get weather information by city.\nChose 2 to get weather information by zip code.\n")
        if answer == '1':
            try:
                by_city()

            except Exception:
                print("Not the right choice. Try again")
                by_city()
        if answer == '2':
            try:
                by_zip()

            except Exception:
                print("Not the right choice. Try again")
                by_zip()
        else:
            print("This is not an option. Please try again.")


if __name__ == "__main__":
    main()