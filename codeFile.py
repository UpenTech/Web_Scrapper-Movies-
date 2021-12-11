from bs4 import BeautifulSoup
import requests

#Here's the URL to the page whose data is to be scrapped
movie_url = "https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc"

#Make a Http request to the page
page_html = requests.get(movie_url, headers= {"Accept-Language": "en-US"})

#Parsing the response
movie_soup = BeautifulSoup(page_html.content, 'html.parser')

#Collect all the div tags classified as "lister-item mode-advanced"
filter_name = movie_soup.find_all('div', {"class": "lister-item mode-advanced"})

#Run through the retrived data to find contents in h3 tag
for every in filter_name:

    title = every.find('h3')
    name = title.find('a').text
    year = title.find('span', {"class": "lister-item-year text-muted unbold"}).text

    rating_data = every.find('div', {"class": "ratings-bar"})
    rating = rating_data.find('strong').text

    print("%-70s Rating: %s" %(name, rating))