import requests
import bs4
import pandas as pd
import datetime

def scrape(url):

    res = requests.get(url)

    return bs4.BeautifulSoup(res.text,'lxml')




if __name__ == "__main__":

    news = {'Headline':[], 'Date/Link':[], 'Source':[]}


    #CBC Section

    soup = scrape("https://www.cbc.ca/news/business")

    headlines = soup.select('.headline')

    times = soup.select('.timeStamp')

    for i in range(len(headlines)):
        news['Headline'].append(headlines[i].getText())
        news['Date/Link'].append(times[i].getText())
        news['Source'].append('CBC News')




    #CTV Section

    soup = scrape("https://www.ctvnews.ca/business")

    for story in soup.find_all('a',{'class':'c-list__item__image'},href=True,title=True):
        news['Headline'].append(story['title'])
        news['Date/Link'].append(story['href'])
        news['Source'].append('CTV News')


    #Financial Post

    soup = scrape("https://financialpost.com")

    for story in soup.find_all('a',{'class':'article-card__link'},href=True,):
        news['Headline'].append(story['aria-label'])
        news['Date/Link'].append('https://financialpost.com'+story['href'])
        news['Source'].append('Financial Post')


    #Yahoo Finance
    
    soup = scrape("https://ca.finance.yahoo.com/topic/news/")
        
    for story in soup.find_all('a',href=True,):
        
        if len(story.getText()) > 20:
            news['Headline'].append(story.getText())
            news['Date/Link'].append(story['href'])
            news['Source'].append('Yahoo Finance')
            
            
    #BNN Bloomberg
    
    soup = scrape("https://www.bnnbloomberg.ca")
        
    for story in soup.find_all('a',href=True):
        
        if len(story.getText()) > 20:
            news['Headline'].append(story.getText())
            news['Date/Link'].append(story['href'])
            news['Source'].append('BNN Bloomberg')
    
    #The Economist
    
    soup = scrape("https://www.economist.com")
    
    for story in soup.find_all('a',href=True):
        
        if len(story.getText()) > 20:
            news['Headline'].append(story.getText())
            news['Date/Link'].append(story['href'])
            news['Source'].append('The Economist')
            
    #Wall Street Journal
        
    soup_b = scrape("https://www.wsj.com/?mod=nav_top_section")
    
    
    for story in soup_b.find_all('a',href=True):
        
        if len(story.getText()) > 30:
            news['Headline'].append(story.getText())
            news['Date/Link'].append(story['href'])
            news['Source'].append('Wall Street Journal')
            
    
    #Market Watch
            
    soup_b = scrape("https://www.marketwatch.com")
    
    
    for story in soup_b.find_all('a',{'class':'link'},href=True):
        
        if len(story.getText()) > 30:
            news['Headline'].append(story.getText())
            news['Date/Link'].append(story['href'])
            news['Source'].append('Market Watch')
        



    #PDictionary to Pandas Dataframe to export to excel

    news_df = pd.DataFrame(news)

    print(news_df)

    news_df.to_excel(f'{datetime.datetime.now()}' + 'news.xlsx')








