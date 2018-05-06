import pandas as pd
import requests as req
from bs4 import BeautifulSoup

def getLocation(cntr):
    base_url ='http://www.espncricinfo.com/series/8048/game/'
    soup = BeautifulSoup(req.get(base_url+str(cntr)).content, 'lxml')
    return soup.find("div", {"class": "stadium-details"}).get_text()

def getDetails():
    base_url = 'http://www.espncricinfo.com/series/8048/scorecard/'
    counter = 1136560
    col = ['Bowling', 'O', 'M', 'R', 'W', 'Econ',
           '0s', '4s', '6s', 'WD', 'NB', 'location']
    df = pd.DataFrame(columns = col)
    df.to_csv('bowl.csv', index=0)
    while counter < 1136591:
        counter += 1
        url = base_url+str(counter)
        print(base_url+str(counter))
        dflist = pd.read_html(url)
        dfa = dflist[0].drop(['Unnamed: 1', 'Unnamed: 12'], axis=1)
        dfa['location'] = getLocation(counter)
        # dfa.to_csv('data/' +
        #     str(counter)+'a.csv', index=0)
        dfa.to_csv('bowl.csv',mode='a', header=False, index=0)
        dfb = dflist[1].drop(['Unnamed: 1', 'Unnamed: 12'], axis=1)
        dfb['location'] = getLocation(counter)
        dfb.to_csv('bowl.csv', mode='a', header=False, index=0)
        # dfb.to_csv('data/'+
        #     str(counter)+'b.csv', index=0)


if __name__ == '__main__':
    getDetails()
