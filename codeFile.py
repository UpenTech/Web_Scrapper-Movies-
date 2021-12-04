from bs4 import BeautifulSoup
import requests

movie_url = "https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc"

page_html = requests.get(movie_url, headers= {"Accept-Language": "en-US"})

movie_soup = BeautifulSoup(page_html.content, 'html.parser')

filter_name = movie_soup.find_all('div', {"class": "lister-item mode-advanced"})

for every in filter_name:
    title = every.find('h3')
    name = title.find('a').text
    year = title.find('span', {"class": "lister-item-year text-muted unbold"}).text

    rating_data = every.find('div', {"class": "ratings-bar"})
    rating = rating_data.find('strong').text

    description = every.find("p" , {"class": "text-muted"})
    genre = description.find("span", {"class": "genre"}).text

    print("%-70s Rating: %s" %(name, rating))