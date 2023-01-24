import re
from datetime import datetime
from bs4 import BeautifulSoup
import requests


def get_collection_dates(uprn:str, post_code:str):
    session = requests.Session()
    token_response = session.get("https://www.oxford.gov.uk/mybinday")
    soup = BeautifulSoup(token_response.text, "html.parser")
    token = soup.find('input', {'name': '__token'}).attrs['value']
    if not token:
        raise ValueError("Could not parse CSRF Token from initial response. Won't be able to proceed.")

    form_data = {
        "__token": token,
        "page": "355",
        "locale": "en_GB",
        "q6ad4e3bf432c83230a0347a6eea6c805c672efeb_0_0": post_code,
        "q6ad4e3bf432c83230a0347a6eea6c805c672efeb_1_0": uprn,
        "next": "Next"
    }

    collection_response = session.post("https://www.oxford.gov.uk/xfp/form/52", data=form_data)
    collection_soup = BeautifulSoup(collection_response.text, "html.parser")
    for paragraph in collection_soup.find("div", class_="editor").find_all("p"):

        matches = re.match(r"^(\w+) Next Collection: (.*)", paragraph.text)
        if matches:
            collection_type, date_string = matches.groups()
            date = datetime.strptime(date_string, "%A %d %B %Y").date()
            print(collection_type)
            print(date)
            print()


if __name__ == '__main__':
    # Get UPRN from here: https://www.findmyaddress.co.uk/search
    # Randomly chosen address:
    get_collection_dates("100120827594", "OX4 1RB")
