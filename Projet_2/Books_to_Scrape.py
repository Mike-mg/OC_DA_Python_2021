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
    """
     search all categories
    """
    print("function : category_link > In progress ")

    links = []
    r_url = requests.get(address_site + 'catalogue/category/books_1/index.html')
    bs_page = bs(r_url.text, 'html.parser')

    for list_link in bs_page.find('ul', class_='nav-list')('ul'):
        for category in list_link.find_all('li'):
            link_category = address_site + "catalogue/category/" + category('a')[0]['href'][3:]
            links.append(link_category)

    print("function : category_link > Finished ")
    return links

# ===============================================


def nb_page_by_category(param):
    """
    search the number of pages by category
    """
    print("function : nb_page_by_category > In progress ")

    list_by_page = []

    for x in param:

        url_page = x[0:-10]
        list_by_page.append(x)

        page = requests.get(x)
        bs_page = bs(page.text, 'html.parser')

        while bs_page.find_all('li', class_='next'):
            index_page = bs_page.find_all('li', class_='next')[0]('a')[0]['href']
            url_next_page = url_page + index_page

            list_by_page.append(url_next_page)

            npage_next = requests.get(url_next_page)
            bs_page = bs(npage_next.text, 'html.parser')

    print("function : nb_page_by_category > Finished ")
    return list_by_page

# ===============================================


def book_info(param):
    """
    infos by book
    """
    print("function : book_info > In progress ")

    infos_articles = []

    for x in param:

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

    print("function : book_info > Finished ")
    return infos_articles

# ===============================================


def create_folders_and_pics_by_category(category):
    """
        > [1] Create folder by category
        > [3] Saving images each category
    """
    print("function : create_folders_and_pics_by_category > In progress ")

    for x in category:

        page = requests.get(x)
        page_article = bs(page.text, 'html.parser')

        # [1]
        for link in page_article.find_all('div', class_='page-header action'):
            link_category = link('h1')[0].text

            if os.path.exists(f"{dossier}{link_category}"):
                pass
                print(f'The folder exist : {dossier}{link_category}')
            else:
                os.mkdir(f"{dossier}{link_category}")

            for y in nb_page_by_category([x]):

                page = requests.get(y)
                bs_page = bs(page.text, 'html.parser')

                for x in bs_page.find_all('div', class_='image_container'):
                    image_name = x('a')[0]('img')[0]['src'][-36:]
                    url_image = address_site + x('a')[0]('img')[0]['src'][12:]
                    print(url_image)
                    file_path = f"{dossier}{link_category}/{image_name}"
                    print(file_path)

                    if os.path.isfile(f"{dossier}{link_category}/{image_name}"):
                        print(f"The file already has been saved : {image_name}")
                        pass
                    else:
                        urllib.request.urlretrieve(url_image, file_path)
                        print(f" Image for downloading : {image_name}")

    print("function : create_folders_and_pics_by_category > Finished ")

# ===============================================


def backup_data(info_book):
    """

    """
    print("function : backup_data > In progress ")

    with open('article.csv', 'w', newline='\n') as f:

        article_csv = csv.writer(f)
        article_csv.writerow(['Product_page_url', 'Upc', 'Titre', 'Price_including_tax', 'Price_excluding_tax',
                              'Number_available', 'Product_description', 'Category', 'Review_rating', 'Image_url'])

        for x in info_book:
            article_csv.writerow(x)

    print("function : backup_data > Finished ")

# ===============================================


def main():
    create_folders_and_pics_by_category(category_link())
    all_pages = nb_page_by_category(category_link())
    infos_books = book_info(all_pages)
    backup_data(infos_books)

if __name__ == "__main__":
    main()
