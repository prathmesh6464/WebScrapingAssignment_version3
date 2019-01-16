from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

myurl="https://www.rottentomatoes.com/m/interstellar_2014/reviews/"
uclient = ureq(myurl)
pagehtml=uclient.read()
uclient.close()
pagesoup=soup(pagehtml,"html.parser")
page=pagesoup.findAll("div",{"class":"row review_table_row"})
#c1=page.findAll("a",{"class":"unstyled bold articleLink"})
filename="CriticsReview.csv"
f=open(filename,"a")
headers="Critics Name,Critics Review,Critics Review Sentiment Analysis\n"
#f.write(headers)
for col in page:
    col1=col.div.a["href"]

    views = col.findAll('div',{"class": "the_review"})
    review = views[0].text
    print(col1.replace(",", "|") + "," + review + ","+"\n")
    f.write(col1.replace(",", "|") + "," + review +","+"\n")
f.close()