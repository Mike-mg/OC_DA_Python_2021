#! /usr/bin/env python3
# coding:utf-8


# ===============================================

import requests
from bs4 import BeautifulSoup as bs
import csv
import os
import urllib.request

# ===============================================

address_site = "http://books.toscrape.com/"
dossier = "/home/mike/OC_DA_Python/Projet_2/Books_to_Scrape_Images/"

# ===============================================


def category_link():

    links = []
    r_url = requests.get(address_site + 'catalogue/category/books_1/index.html')
    bs_page = bs(r_url.text, 'html.parser')

    for list_link in bs_page.find('ul', class_='nav-list')('ul'):
        for category in list_link.find_all('li'):
            link_category = address_site + "catalogue/category/" + category('a')[0]['href'][3:]
            links.append(link_category)


    print('category_link fini')
    return links


# ===============================================


def create_folders_and_pics_by_category(param):
    """
        > [1] Create folder by category
        > [2] nb page by category
        > [3] Saving images each category
    """

    list_category = param

    for list in list_category:

        list_by_page = [list]
        page = requests.get(list)
        page_article = bs(page.text, 'html.parser')

        # [1]
        for link in page_article.find_all('div',class_='page-header action'):
            category = link('h1')[0].text
            if not os.path.exists(f"{dossier}{category}"):
                os.mkdir(f"{dossier}{category}")

        # [2]
        url_page = list[0:-10]
        while page_article.find_all('li', class_='next'):

            for all_page in page_article.find_all('li', class_='next'):

                num_page = all_page('a')[0]['href']
                next_page = url_page + num_page

                page = requests.get(next_page)
                page_article = bs(page.text, 'html.parser')

                list_by_page.append(next_page)

        # [3]
        for book_image_folder in list_by_page:
            page = requests.get(book_image_folder)
            page_article = bs(page.text, 'html.parser')

            for link in page_article.find_all('div', class_='image_container'):
                link_img = address_site + link('a')[0]('img')[0]['src'][12:]
                image = f"{dossier}{category}{link_img[43:]}"

                if os.path.isfile(f"{dossier}{category}{link_img[43:]}"):
                    pass
                    # print(f"The file already has been saved : {image}")
                else:
                    urllib.request.urlretrieve(link_img, image)
                    # print(f" Image for downloading : {image}")

    print('create_folders_and_pics_by_category fini')
    return list_by_page


# ===============================================


def book_info(param):

    book_url = param

    infos_articles = []

    for x in book_url:

        page = requests.get(x)
        article = bs(page.text, 'html.parser')

        for url_article in article.find_all('div', class_="image_container"):
            product_page_url = address_site + "catalogue" + url_article.find_all('a')[0]['href'][8:]

            info = requests.get(product_page_url)
            page_article = bs(info.text, 'html.parser')

            info_article = []
            for info in page_article.find_all('article', class_="product_page"):
                upc = info.find_all('tr')[0]('td')[0].text
                titre = info.find('h1').text
                price_including_tax = info.find_all('tr')[3]('td')[0].text[1:]
                price_excluding_tax = info.find_all('tr')[2]('td')[0].text[1:]
                number_available = info.find_all('tr')[5]('td')[0].text
                product_description = info.find('h2').find_next('p').text
                url_image = address_site + info.find_all('img')[0]['src'][6:]

            for info in page_article.find_all('ul', class_='breadcrumb'):
                categorie = info.find_all('li')[2].text.strip()

            for info in page_article.find_all('div', class_='content'):
                review_rating = info.find('p', class_='star-rating')['class'][1]

                info_article.append(product_page_url)
                info_article.append(upc)
                info_article.append(titre)
                info_article.append(price_including_tax)
                info_article.append(price_excluding_tax)
                info_article.append(number_available)
                info_article.append(product_description)
                info_article.append(categorie)
                info_article.append(review_rating)
                info_article.append(url_image)


            infos_articles.append(info_article)

    print('book_info fini')
    return infos_articles


# ===============================================


def donnees_sauvegardees(info_article):
    with open('article.csv', 'w', newline='\n') as f:

        article_csv = csv.writer(f)
        article_csv.writerow(['Product_page_url', 'Upc', 'Titre', 'Price_including_tax', 'Price_excluding_tax',
                              'Number_available', 'Product_description', 'Category', 'Review_rating', 'Image_url'])

        for x in info_article:
            article_csv.writerow(x)


# ===============================================


def main():


if __name__ == "__main__":
    main()
