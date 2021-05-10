import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

html = urlopen('http://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxMainPrint.do?idx_cd=1495&board_cd=INDX_001')
soup = BeautifulSoup(html, 'lxml')

list_year=[]
table = soup.find_all('th',{'class':'tc'})
for content in table:
    list_year.append(content.get_text())

list_employment = []
table = soup.find_all('tr', {'data-id':'tr_149501_6'})
for content in table:
    j = content.get_text()

for i in range(10):
    list_employment.append(j[5+5*i:9+5*i])

matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family ='Malgun Gothic')

x = np.arange(10)
y2 = list_employment

fig, ax1 = plt.subplots()

plt.xticks(x, list_year)
ax1.bar(x, y2, color='blue', label='고용률', alpha=0.7, width=0.7)
ax1.set_ylim(35, 50)
ax1.set_xlabel('청년고용동향(고용률 및 실업률)')
ax1.set_ylabel('고용률(%)')
ax1.tick_params(axis='y', direction='in')

ax1.legend(loc='upper left')

plt.show()