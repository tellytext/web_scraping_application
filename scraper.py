#!/usr/bin/python3
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import requests
import user_agents
import datetime
import time
from pprint import pprint

unix = time.time()
date_time = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

results = []

# return search page html
# if error throw response code in exception
class form_search_results:
    def get_search_results(query_str, device="desktop"):
        query_string = {"q": query_str}
        query_string = urllib.parse.urlencode(query_string)
        url = "https://www.google.com/search?adtest=on&" + query_string
        print(url)

        user_agent = user_agents.user_agent(device.lower())
        headers = {'User-Agent': user_agent}

        try:
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            html = resp.read()
            soup = BeautifulSoup(html, 'html.parser')

            r = requests.get(url, headers=headers)
            print(r.status_code)
            if not r.status_code == requests.codes.ok:
                print("HTTP response error. Error code:", r.status_code)

            return soup

        except Exception as e:
            print("Error retrieving HTML:", e)
            pass


    def parse_desktop_search_results(query_str, soup):
        global results
        try:
            tagged_values = soup.find_all('div', {'id': 'tvcap'})
            if not tagged_values:
                print("No Div Tag found")
                pass

            position = 0

            for x in tagged_values:
                headline_class = x.find_all('div', {'class': 'ad_cclk'})
                visual_url_class = x.find_all('div', {'class': 'ads-visurl'})
                description_class = x.find_all('div', {'class': 'ellip ads-creative'})

                if not headline_class or not visual_url_class or not description_class:
                    print("Div Tag found but no headline, url or description")
                    pass

                values = zip(headline_class, visual_url_class, description_class)

                for headline, vis_url, desc in values:
                    try:
                        position += 1
                        advert = [query_str, headline.text, desc.text, vis_url.text, position, date_time]
                        results.append(advert)

                    except Exception as e:
                        print("Error pushing desktop results to list:", e)
                        pass

                return results

        except Exception as e:
            print("Error pushing desktop results to list:", e)
            pass



# print(form_search_results.parse_desktop_search_results("bet365", form_search_results.get_search_results("bet365")))