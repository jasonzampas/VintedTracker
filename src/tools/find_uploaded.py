import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def find_uploaded_date(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
    
        sidebar_divs = soup.find_all('div', class_='details-list__item-value', itemprop='upload_date')

        if sidebar_divs:
            uploaded = sidebar_divs[0].get_text(strip=True)
            return uploaded
        else:
            return None
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

def find_timestamp(url1):
    uploaded = find_uploaded_date(url=url1)

    if uploaded is not None:
        if uploaded == "Just now":
            time = datetime.now()
            formatted_time = time.strftime("%H:%M:%S")

            return formatted_time

        elif uploaded == "a minute ago":
            current_time = datetime.now()
            new_time = current_time - timedelta(minutes=1)

            formatted_time = new_time.strftime("%H:%M:%S")
            return formatted_time
        
    else:
        return None