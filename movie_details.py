import requests
from bs4 import BeautifulSoup
import urllib


class Scrape():
    
    def geturl(self,movie):
        url1 = "http://www.imdb.com/find?ref_=nv_sr_fn&q="
        search_url = url1+movie
        return search_url

      

    def connect(self,url):
        link_dict = {}
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)
        table = soup.find('table', attrs={'class' : 'findList'})
        for row in table.findAll('tr'):
            cells = row.findAll('td')
            list1 = cells[1].contents
            year = list1[2]
            name = cells[1].find('a')
            nameWithYear = name.get_text() + year
            link_dict.update({nameWithYear:name['href']})
        return link_dict



    def get_search_link(self,url):
        link_for_selected_movie = "http://www.imdb.com" + url
        return link_for_selected_movie



    def connect_search_link(self,url):
        details = {}
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)
        element = soup.find('div', attrs={'class' : 'minPosterWithPlotSummaryHeight'})

        if element:
            image_link = element.findAll('img')[0].get('src')
            details.update({'poster': image_link})


        else:
            img_ele = soup.find('div',attrs={'class' : 'poster'})
            image_link = img_ele.findAll('img')[0].get('src')
            details.update({'poster': image_link})
            element = soup.find('div', attrs={'class' : 'plot_summary_wrapper'})
        

        summary = element.find('div', attrs={'class' : 'summary_text'}).contents
        details.update({'summary_text': summary})

        director = element.find('span', attrs={'itemprop' : 'director'}).text
        details.update({'director': director})

        writers = element.findAll('span', attrs={'itemprop' : 'creator'})
        creators = ""
        for writer in writers:
            creator = writer.find('span', attrs={'class' : 'itemprop'}).text
            creators = creator + ", " + creators 
        details.update({'writer': creators})

            
        stars = element.findAll('span', attrs={'itemprop' : 'actors'})
        actors = ""
        for star in stars:
            actor = star.find('span', attrs={'class' : 'itemprop'}).text
            actors = actor + ", "+ actors  
        details.update({'actors': actors})
        return details






        




                    

# def main():
#     obj = Scrape()
#     url = obj.geturl()
#     link_dict = obj.connect(url)
#     # obj.get_search_link(link_dict)

# main()



    

