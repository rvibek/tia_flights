import datetime
import requests


urls = {'flight_detail':'https://www.tiairport.com.np/flight_details', 
	 'flight_details_2': 'https://www.tiairport.com.np/flight_details_2'}


for url in urls:
	
	response = requests.get(urls[url])

	date = datetime.datetime.now().strftime("%Y_%m_%d")
	open(f"flight_details/{url}_{date}.json", "wb").write(response.content)

