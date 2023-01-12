# IMPORTING LIBRARIES

from ast import Try
from logging import exception
from unicodedata import numeric
from lxml import html
from pip import main
import requests

# Function to crawl the website and look for that version using the Xpath
def oracle_v():
    
    try: 
        page = requests.get("https://www.oracle.com/database/technologies/oracle-database-software-downloads.html#19c")
        res = html.fromstring(page.content)
        version = res.xpath("/html/body/div[3]/section[3]/div/p[2]/strong/text()")
        # version_string = version.ToString()
        str = ""
        str = str.join(version[0])
        # print(type(str))
        # print(str)

        str1 = ""

        for i in str:
            if i.isnumeric() or i == ("."):

                str1 = str1 + i

        print("Oracle:" + str1)
    except:
        print("Oracle didnt get crawled. Check Manually.")

def phpmyadmin_v():
    
    try: 
        page = requests.get("https://www.phpmyadmin.net/news/")
        res = html.fromstring(page.content)
        version = res.xpath("/html/body/content/div/div[1]/h2/a/text()")
        # version_string = version.ToString()
        str = ""
        str = str.join(version[0])
        # print(type(str))
        # print(str)

        str1 = ""

        for i in str:
            if i.isnumeric() or i == ("."):

                str1 = str1 + i

        print("PhpMyAdmin:" + str1)
    except:
        print("Sqlite didnt get crawled")


def sqlite_v():

    try: 
        page = requests.get("https://www.sqlite.org/index.html")
        res = html.fromstring(page.content)
        version = res.xpath("/html/body/a[1]/text()")
        # version_string = version.ToString()
        str = ""
        str = str.join(version[0])
        # print(type(str))
        # print(str)

        str1 = ""

        for i in str:
            if i.isnumeric() or i == ("."):

                str1 = str1 + i

        print("Sqlite:" + str1)
    
    except:
        print("Sqlite didnt get crawled")


def microsoftsqlserver_v():
    try:

        page = requests.get(
            "https://www.microsoft.com/en-ie/sql-server/sql-server-downloads"
        )
        res = html.fromstring(page.content)
        version = res.xpath("/html/body/section/div[2]/div[4]/div/div/div/h2/text()")
        # version_string = version.ToString()
        str = ""
        str = str.join(version[0])
        # print(type(str))

        str1 = ""

        for i in str:
            if i.isnumeric() or i == ("."):

                str1 = str1 + i

        print("Microsoft SQL Server:" + str1)

    except:
        print("Microsoft SQL Server didnt get crawled")

def mongodb_v():

    try:

        page = requests.get(
            "https://www.mongodb.com/docs/manual/release-notes/"
        )
        res = html.fromstring(page.content)
        version = res.xpath("/html/body/div[1]/div[1]/div/div[2]/div/div[1]/main/div/section/section[2]/p[2]/a/text()")
        # version_string = version.ToString()
        str = ""
        str = str.join(version[0])

        str1 = ""

        for i in str:
            if i.isnumeric() or i == ("."):

                str1 = str1 + i

        print("MongoDB:" + str1)

    except:
        print("MongoDb didnt get crawled")


def mongodb_v1():

    try:
        page = requests.get(
        "https://www.mongodb.com/docs/v5.2/release-notes/5.2/"
        )
        res = html.fromstring(page.content)
        version = res.xpath("/html/body/div[1]/div[1]/div/div[2]/div/div[1]/main/div/section/h1/text()")
        # version_string = version.ToString()
        str = ""
        str = str.join(version[0])

        str1 = ""

        for i in str:
            if i.isnumeric() or i == ("."):

                str1 = str1 + i

        print("MongoDb:" + str1)
    except:
        print("MongoDb didnt get crawled")


def postgre_v():

    try:
        page = requests.get(
        "https://www.postgresql.org/docs/14/release-14-3.html"
        )
        res = html.fromstring(page.content)
        version = res.xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div/div/h2/text()")
        # version_string = version.ToString()
        str = ""
        str = str.join(version[0])

        str1 = ""

        for i in str:
            if i.isnumeric() or i == ("."):

                str1 = str1 + i

        print("Postgre:" + str1)
    except:
        print("Postgre didnt get crawled")

def mysql_v():
    
    try: 
        page = requests.get("https://dev.mysql.com/doc/")
        res = html.fromstring(page.content)
        version = res.xpath("/html/body/div/div/div/div[1]/div/div[4]/a[2]/span/text()")
        # version_string = version.ToString()
        str = ""
        str = str.join(version[0])
        # print(type(str))
        # print(str)

        str1 = ""

        for i in str:
            if i.isnumeric() or i == ("."):

                str1 = str1 + i

        print("MySql:" + str1)
    except:
        print("MySql didnt get crawled. Check Manually.")


# Main Function that calls every other function in the program.
def main():
    oracle = oracle_v()
    php = phpmyadmin_v()
    sqlite = sqlite_v()
    microsoftsqlserver = microsoftsqlserver_v()
    mongodb = mongodb_v()
    mongodb1 = mongodb_v1()
    postgre = postgre_v()
    mysql = mysql_v()
    



if __name__ == "__main__":

    # calling main function
    main()
