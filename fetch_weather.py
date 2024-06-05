import os
import csv
from bs4 import BeautifulSoup
import requests
import os

def fetch_weather_data(url):
    """
    Fetches weather data from a given URL.
    """

    headers = headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    
    # Example parsing (assumes structure of the weather website)
    temperature = soup.find("span", class_='DailyContent--temp--1s3a7').text[0:-1]
    humidity = soup.find("span", class_="DetailsTable--value--2YD0-").text
    
    return {"temperature" : temperature, "humidity" : humidity}

def write_to_csv(data, output_file):
    """
    Writes weather data to a CSV file.
    """
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['temperature', 'humidity'])
        writer.writeheader()
        writer.writerow(data)

def append_to_csv(data, output_file):
    """
    appends weather data to a CSV file.
    """
    with open(output_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['temperature', 'humidity'])
        writer.writerow(data)

if __name__ == "__main__":
    # Example usage
    url = "https://weather.com/pt-BR/clima/10dias/l/63e18eea74a484c42c3921cf52a8fec98113dbb13f6deb7c477b2f453c95b837"
    output_file = './weather_data.csv'
    weather_data = fetch_weather_data(url)

    if (not os.path.exists(output_file)):
        write_to_csv(weather_data, output_file)
    else:
        append_to_csv(weather_data, output_file)

    
    print("Weather data fetched and saved successfully.")