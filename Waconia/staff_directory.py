import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def crawl_page(url):

	data_dict = {"school_name":[],"address":[],"state":[],"zip":[],"first_name":[],"last_name":[],"title":[],"phone":[],"email":[]}

	response = requests.request("GET", url, headers=headers)

	status_code = response.status_code
	if status_code != 200:
		pass
	soup = BeautifulSoup(response.text,"html.parser")
	try:
		school_name = soup.find("h1").find("a").get_text().strip()
	except:
		school_name = "NA"

	school_address = soup.find("p",{"class":"address"}).get_text().strip()
	address_1 = school_address.split("\n")
	address = address_1[0]
	state = address_1[1].split(",")[0].strip()
	pincode = address_1[1].split(",")[-1].strip()


	all_details = soup.find_all("div",{"class":"views-row"})

	for one_detail in all_details:


		first_group = one_detail.find("div",{"class":"first group"})
		name = first_group.find("h2").get_text().strip()
		first_name = name.split(",")[0]
		last_name = name.split(",")[-1]
		title = first_group.find("div",{"class":"field job-title"}).get_text().strip()
		phone = one_detail.find("div",{"class":"last group"}).find("div",{"class":"field phone"}).get_text().strip()
		email = one_detail.find("div",{"class":"last group"}).find("div",{"class":"field email"}).get_text().strip()

		data_dict["address"].append(address)
		data_dict["state"].append(state)
		data_dict["zip"].append(pincode)
		data_dict["school_name"].append(school_name)
		data_dict["first_name"].append(first_name)
		data_dict["last_name"].append(last_name)
		data_dict["title"].append(title)
		data_dict["phone"].append(phone)
		data_dict["email"].append(email)

	df = pd.DataFrame(data_dict)
	df.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)
	try:
		next_page = soup.find("li",{"class":"item next"}).find("a").get("href")
		url = url + next_page
		crawl_page(url)
	except:
		pass


output_path = "staff_directory.csv"
url = "https://isd110.org/our-schools/laketown-elementary/staff-directory"#?s=&page=1
headers = {
  'authority': 'isd110.org',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
crawl_page(url)