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


def book_by_category():

    print("Function : link_by_category in progress")

    links = []

    r_url = requests.get(address_site + 'catalogue/category/books_1/index.html')
    bs_page = bs(r_url.text, 'html.parser')

    for list_link in bs_page.find('ul', class_='nav-list')('ul'):
        for category in list_link.find_all('li'):
            link_category = address_site + "catalogue/category/" + category('a')[0]['href'][3:]
            links.append(link_category)

    print("Function : link_by_category finished")
    return links

# ===============================================

def create_folders_and_pics(param):

    print("Function : urls_book_by_catagory in progress")

    list_urls = [param]
    url_page = param[0:-10]

    page = requests.get(param)
    page_article = bs(page.text, 'html.parser')

    while page_article.find_all('li', class_='next'):

        for all_page in page_article.find_all('li', class_='next'):
            num_page = all_page('a')[0]['href']
            next_page = url_page + num_page
            print(next_page)
            list_urls.append(next_page)
            page = requests.get(next_page)
            page_article = bs(page.text, 'html.parser')

            for book_image_folder in list_urls:
                page = requests.get(book_image_folder)
                page_article = bs(page.text, 'html.parser')

                for link in page_article.find_all('div', class_="col-sm-8 col-md-9"):
                    category = link.find('div',class_='page-header action')('h1')[0].text

                    if not os.path.exists(f"{dossier}{category}"):
                        os.mkdir(f"{dossier}{category}")

                for link in link.find_all('div', class_='image_container'):
                    link_img = address_site + link('a')[0]('img')[0]['src'][12:]
                    urllib.request.urlretrieve(link_img, dossier + category + link_img[43:])

    print("Function : urls_book_by_catagory finished")



# # ===============================================
#
# info_article = []
# def info_livre(param):
#
#     adresse_books_img = "http://books.toscrape.com/"
#
#     for i in param:
#
#         dictionnaire = []
#
#         # dossier = "/home/mike/OC_DA_Python/Projet_2/Books_to_Scrape_Images"
#         product_page_url = i
#         dictionnaire.append(product_page_url)
#
#         page = requests.get(i)
#         page_article = bs(page.text, 'html.parser')
#
#         for info in page_article.find_all('div', class_='content'):
#             upc = info.find('table', class_='table table-striped')('tr')[0]('td')[0].text
#             dictionnaire.append(upc)
#             titre = info.find('h1').text
#             dictionnaire.append(titre)
#             price_including_tax = info.find_all('tr')[3]('td')[0].text[1:]
#             dictionnaire.append(price_including_tax)
#             price_excluding_tax = info.find_all('tr')[2]('td')[0].text[1:]
#             dictionnaire.append(price_excluding_tax)
#             number_available = info.find_all('tr')[5]('td')[0].text
#             dictionnaire.append(number_available)
#             product_description = info.find('h2').find_next('p').text
#             dictionnaire.append(product_description)
#
#         for info in page_article.find_all('ul', class_='breadcrumb'):
#             categorie = info.find_all('li')[2].text.strip()
#             dictionnaire.append(categorie)
#
#         for info in page_article.find_all('div', class_='content'):
#             review_rating = info.find('p', class_='star-rating')['class'][1]
#             dictionnaire.append(review_rating)
#             image_url = adresse_books_img + info.find('img')['src'][6:]
#             dictionnaire.append(image_url)
#             # wget.download(image_url,out=dossier)
#
#
#         info_article.append(dictionnaire)
#
# def donnees_sauvegardees():
#     with open('article.csv', 'w', newline='\n') as f:
#
#         article_csv = csv.writer(f)
#         article_csv.writerow(['Product_page_url', 'Upc', 'Titre', 'Price_including_tax', 'Price_excluding_tax',
#                               'Number_available', 'Product_description', 'Category', 'Review_rating', 'Image_url'])
#         for i in info_article:
#             article_csv.writerow(i)
#
# def main():
#     recuperation_lien_par_categorie()
#     recupere_les_urls_livres_par_categorie(liste_lien_par_categorie)
#     info_livre(tous_les_livres_par_page)
#     donnees_sauvegardees()


def main():
    book_by_category()
    create_folders_and_pics('http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html')



if __name__ == "__main__":
    main()
