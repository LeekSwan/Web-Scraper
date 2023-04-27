from datetime import date
import csv

import scrapper

# print(get_page_data('https://horrycounty.org/apps/LandRecords/PropertyCard/42415030067'))

def run_scrapper():
    # user_input_start = input('Enter ending PIN')
    # user_input_end = input('Enter staring PIN')

    user_input_start = 42415030066
    user_input_end = 42415030298

    date_last_retrieved = [str(date.today())] * 10

    headers = ['name', 'address', 'unit', 'subdivision', 'pin', 'tms']
    with open("horry_county_records.csv", "w+", newline='') as my_csv:
        writer = csv.writer(my_csv)
        writer.writerow(headers)
        for i in range(int(user_input_start), int(user_input_end) + 1):
            scraper_data = scrapper.get_page_data('https://horrycounty.org/apps/LandRecords/PropertyCard/' + str(i))
            if scraper_data:
                writer.writerow(scraper_data)
            # time.sleep(random.randint(1, 2))  # controls scrape rate so we dont flood the site with requests

run_scrapper()