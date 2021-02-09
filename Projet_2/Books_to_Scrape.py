#! /usr/bin/env python3
# coding:utf-8

import requests
from bs4 import BeautifulSoup as bs
import csv
import wget


# # ===============================================

# page_1a50_du_site_books_to_scrape = []
#
#
# def recupere_page_1a50_du_site_books_to_scrape():
#     for i in range(1, 51):
#         url = f"http://books.toscrape.com/catalogue/category/books_1/page-{str(i)}.html"
#         page_1a50_du_site_books_to_scrape.append(url)
#
# # ===============================================

liste_lien_par_categorie = []
def recuperation_lien_par_categorie():

    adresse_site = "http://books.toscrape.com/"

    url = 'http://books.toscrape.com/index.html'
    r_url = requests.get(url)
    bs_page = bs(r_url.text, 'html.parser')

    for liste_lien in bs_page.find('ul', class_='nav-list')('ul'):
        for categorie in liste_lien.find_all('li'):
            lien_par_categorie = adresse_site + categorie('a')[0]['href']
            liste_lien_par_categorie.append(lien_par_categorie)
    print("recuperation liste_lien_par_categorie terminée")

# ===============================================

tous_les_livres_par_page = []
def recupere_les_urls_livres_par_categorie(param):
    adresse_books_catalogue = "http://books.toscrape.com/catalogue/"
    for adresse in param:
        page = requests.get(adresse)
        page_article = bs(page.text, 'html.parser')

        for lien in page_article.find_all('h3'):
            page_livre = adresse_books_catalogue + lien.find('a')['href'][6:]
            tous_les_livres_par_page.append(page_livre)
    print("recuperation tous_les_livres_par_page terminée")


# ===============================================

info_article = []
def info_livre(param):

    adresse_books_img = "http://books.toscrape.com/"

    for i in param:

        dictionnaire = []

        # dossier = "/home/mike/OC_DA_Python/Projet_2/Books_to_Scrape_Images"
        product_page_url = i
        dictionnaire.append(product_page_url)

        page = requests.get(i)
        page_article = bs(page.text, 'html.parser')

        for info in page_article.find_all('div', class_='content'):
            upc = info.find('table', class_='table table-striped')('tr')[0]('td')[0].text
            dictionnaire.append(upc)
            titre = info.find('h1').text
            dictionnaire.append(titre)
            price_including_tax = info.find_all('tr')[3]('td')[0].text[1:]
            dictionnaire.append(price_including_tax)
            price_excluding_tax = info.find_all('tr')[2]('td')[0].text[1:]
            dictionnaire.append(price_excluding_tax)
            number_available = info.find_all('tr')[5]('td')[0].text
            dictionnaire.append(number_available)
            product_description = info.find('h2').find_next('p').text
            dictionnaire.append(product_description)

        for info in page_article.find_all('ul', class_='breadcrumb'):
            categorie = info.find_all('li')[2].text.strip()
            dictionnaire.append(categorie)

        for info in page_article.find_all('div', class_='content'):
            review_rating = info.find('p', class_='star-rating')['class'][1]
            dictionnaire.append(review_rating)
            image_url = adresse_books_img + info.find('img')['src'][6:]
            dictionnaire.append(image_url)
            # wget.download(image_url,out=dossier)


        info_article.append(dictionnaire)

def donnees_sauvegardees():
    with open('article.csv', 'w', newline='\n') as f:

        article_csv = csv.writer(f)
        article_csv.writerow(['Product_page_url', 'Upc', 'Titre', 'Price_including_tax', 'Price_excluding_tax',
                              'Number_available', 'Product_description', 'Category', 'Review_rating', 'Image_url'])
        for i in info_article:
            article_csv.writerow(i)

def main():
    recuperation_lien_par_categorie()
    recupere_les_urls_livres_par_categorie(liste_lien_par_categorie)
    info_livre(tous_les_livres_par_page)
    donnees_sauvegardees()

main()






