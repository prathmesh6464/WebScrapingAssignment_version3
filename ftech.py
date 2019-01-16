import csv
from textblob import *
from urllib.request import urlopen as ureq
from pandas import *

def connect():
    with open("CriticsReview.csv", "r" or "a+") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = str(csv.writer(csv_file))
        i = 0
        appendFile = open("CriticsReview.csv", "a")
        f1 = open("CriticsReview.csv", "a")
        headers = "'''Name''', '''Critisc Review''' ,'''Critics Review Sentiment Analysis'''\n"
        f1.write(headers)
        appendFile.write("\n")

        for line in csv_reader:
            try:

                if len(line) < 2: break
                column1 = str(line[0])
                column2 = str(line[1])
                sen = (line[1])
                blob = TextBlob(sen)
                data = (blob.sentiment)
                dataa = str(data)
                p=str(dataa)
                print(column1,column2,p)
                appendFile.write(column1.replace(",", "|")+ "," + column2.replace(",", "|") + "," + p + "\n")
            finally:
                pass
        f1.close()
        appendFile.close()

        csv_file.close()

connect()