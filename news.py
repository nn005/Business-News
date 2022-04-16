import requests
import bs4
import pandas as pd
import datetime


class scrape_obj():
    
    def __init__(self,url,name):
        
        self.url = url
        self.name = name
     
    
    def simple_scrape(self):
        
        res = requests.get(self.url)
        return bs4.BeautifulSoup(res.text,'lxml')
        
    
    def complete_scrape(self,lenght):
        
        soup = self.simple_scrape()
        
        for story in soup.find_all('a',href=True,):
        
            if len(story.getText()) > lenght:
                news['Headline'].append(story.getText())
                news['Date/Link'].append(story['href'])
                news['Source'].append(f'{self.name}')
        
        




if __name__ == "__main__":

    news = {'Headline':[], 'Date/Link':[], 'Source':[]}


    #CBC 
        
    cbc = scrape_obj("https://www.cbc.ca/news/business",'CBC News')
    
    soup = cbc.simple_scrape()
    
    headlines = soup.select('.headline')
    
    times = soup.select('.timeStamp')

    for i in range(len(headlines)):
        news['Headline'].append(headlines[i].getText())
        news['Date/Link'].append(times[i].getText())
        news['Source'].append(f'{cbc.name}')




    #CTV 

    ctv = scrape_obj("https://www.ctvnews.ca/business",'CTV News')
    
    soup = ctv.simple_scrape()

    for story in soup.find_all('a',{'class':'c-list__item__image'},href=True,title=True):
        news['Headline'].append(story['title'])
        news['Date/Link'].append(story['href'])
        news['Source'].append(f'{ctv.name}')


    #Financial Post
    
    
    fp = scrape_obj("https://financialpost.com",'Financial Post')

    soup = fp.simple_scrape()

    for story in soup.find_all('a',{'class':'article-card__link'},href=True,):
        news['Headline'].append(story['aria-label'])
        news['Date/Link'].append('https://financialpost.com'+story['href'])
        news['Source'].append(f'{fp.name}')


    #CNN
    
    cnn = scrape_obj("https://www.cnn.com/business",'CNN')
    
    soup = cnn.simple_scrape()
    
    story = soup.select('.cd__headline')
    
    for i in story:
        news['Headline'].append(i.select('.cd__headline-text.vid-left-enabled')[0].getText())
        news['Date/Link'].append(i.find('a',href=True)['href'])
        news['Source'].append(f'{cnn.name}')
        
        
        
    #CNBC
    
    cnbc = scrape_obj("https://www.cnbc.com",'CNBC')
    
    soup = cnbc.simple_scrape()
    
    for story in soup.find_all('a',title=True,href=True,):
        news['Headline'].append(story['title'])
        news['Date/Link'].append(story['href'])
        news['Source'].append(f'{cnbc.name}')
    
    
    #Yahoo Finance
    
    yahoo_finance = scrape_obj("https://ca.finance.yahoo.com/topic/news/",'Yahoo Finance')
    
    yahoo_finance.complete_scrape(20)
            
            
    #BNN Bloomberg
    
    bnn_bloomberg = scrape_obj("https://www.bnnbloomberg.ca",'BNN Bloomberg')
    
    bnn_bloomberg.complete_scrape(20)
    
    
    #The Economist
    
    the_economist = scrape_obj("https://www.economist.com",'The Economist')
    
    the_economist.complete_scrape(20)
    
            
    #Wall Street Journal
    
    wsj = scrape_obj("https://www.wsj.com/?mod=nav_top_section",'Wall Street Journal')
    
    wsj.complete_scrape(30)
    
    
    #Market Watch
    
    market_watch = scrape_obj("https://www.marketwatch.com",'Market Watch')
    
    market_watch.complete_scrape(40)
    
    
    #Dictionary to Pandas Dataframe and Excel naming file with current date

    pd.options.display.max_rows = 4000
    
    news_df = pd.DataFrame(news)
    
    display(news_df)
    
    news_df.to_excel(f'{datetime.datetime.now()}' + 'news.xlsx')