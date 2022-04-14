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


    #PDictionary to Pandas Dataframe to export to excel

    news_df = pd.DataFrame(news)

    print(news_df)

    news_df.to_excel(f'{datetime.datetime.now()}' + 'news.xlsx')








