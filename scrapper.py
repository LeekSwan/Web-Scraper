from bs4 import BeautifulSoup as bs
import requests


def get_page_data(req_url):
  src = requests.get(req_url,verify=False)
  if src.status_code != 200:
    return None
  soup = bs(src.text, 'html.parser')

  # get details Header
  details_header = soup.find_all('div', class_="detailsHeader")
  for i in details_header:
    line1 = i.find('h1').text.split(';')
    subdivision = line1[0]
    unit = line1[1]
    line2 = i.find('h2').text.split(' ')
    pin = line2[1]
    tms = line2[4]

  # # get owner info
  ownerInfo = soup.find_all('div', class_="ownerInfo")
  for i in ownerInfo:
    name = i.find('h2').text
    address = i.find('h3').get_text(separator="<br/>").strip().split('<br/>')
    street = address[0]
    city = address[1]
  return ([name, street,city, unit, subdivision, pin, tms])


# get_page_data('https://horrycounty.org/apps/LandRecords/PropertyCard/42415030067')