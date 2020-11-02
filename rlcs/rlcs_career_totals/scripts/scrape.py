import pandas as pd
import time
from bs4 import BeautifulSoup


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst

if __name__ == "__main__":
    
    soup = BeautifulSoup(open('source.html', 'r'), 'lxml')
        
    tds = []

    for i in range(730):
        tr = soup.find('tr', attrs={'item-index':i})
        for td _all('td'):
            if td.text:
                tds.append(td.text)

        for img in tr.find_all('img'):
            img_name = img.get('src').split('/')[-1]
            flag_name = img_name.split('.')[0]
            tds.append(flag_name)
            
    records = list(chunks(tds, 10))
    
    main_col_header = ['Player', 
                       'GP',
                       'W%',
                       'SCPG', 
                       'GPG', 
                       'APG', 
                       'SAPG', 
                       'SHPG', 
                       'Rating',
                       'Country'] 
    
    main_df = pd.DataFrame(records, columns=main_col_header)
    main_df.applymap(str.strip)
    main_df.to_csv('main_rlcs_stats.csv', index=False)
