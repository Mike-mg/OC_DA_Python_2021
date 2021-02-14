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


def title_category():
    """
    Search all category titles
    """

    title_category = []
    r_url = requests.get(address_site + 'catalogue/category/books_1/index.html')
    bs_page = bs(r_url.text, 'html.parser')

    for list_link in bs_page.find('ul', class_='nav-list')('ul'):
        for category in list_link.find_all('li'):
            title_category.append(category('a')[0].text.strip())

    print("> Function : title_category > Finished ")
    return title_category

# ===============================================


def category_link():
    """
     search all categories
    """

    links = []
    r_url = requests.get(address_site + 'catalogue/category/books_1/index.html')
    bs_page = bs(r_url.text, 'html.parser')

    for list_link in bs_page.find('ul', class_='nav-list')('ul'):
        for category in list_link.find_all('li'):
            link_category = address_site + "catalogue/category/" + category('a')[0]['href'][3:]
            links.append(link_category)

    print("> Function : category_link > Finished ")
    return links

# ===============================================


def nb_page_by_category(param):
    """
    search the number of pages by category
    """

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

    print("> Function : nb_page_by_category > Finished ")
    return list_by_page

# ===============================================


def book_info(param):
    """
    infos by book
    """

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

    print("> Function : book_info > Finished ")
    return infos_articles

# ===============================================


def create_folders_and_pics_by_category(category):
    """

    """

    for x in category:

        page = requests.get(x)
        page_article = bs(page.text, 'html.parser')

        # [1]
        for link in page_article.find_all('div', class_='page-header action'):
            link_category = link('h1')[0].text

            print('\n===========================================================')
            print(f'Downloading of Images and creation of the category folder : {link_category}')
            print('---------------------')

            if os.path.exists(f"{dossier}{link_category}"):
                pass
                print(f'> The folder exist : {dossier}{link_category}')
            else:
                os.mkdir(f"{dossier}{link_category}")

            for y in nb_page_by_category([x]):

                page = requests.get(y)
                bs_page = bs(page.text, 'html.parser')

                for x in bs_page.find_all('div', class_='image_container'):
                    image_name = x('a')[0]('img')[0]['src'][-36:]
                    url_image = address_site + x('a')[0]('img')[0]['src'][12:]
                    print(f"> Url image : {url_image}")
                    file_path = f"{dossier}{link_category}/{image_name}"
                    print(f"> Path : {file_path}")

                    if os.path.isfile(f"{dossier}{link_category}/{image_name}"):
                        print(f"> The file already has been saved : {image_name}")
                        print()

                    else:
                        urllib.request.urlretrieve(url_image, file_path)
                        print(f"> Image for downloading : {image_name}")

    print("> Function : create_folders_and_pics_by_category > Finished ")

# ===============================================


def backup_data(info_book):
    """

    """

    print('===========================================')
    choice_name_file = input('> Enter the filename : ')
    print('===========================================')

    with open(f'{choice_name_file}.csv', 'w', newline='\n') as f:

        file_csv = csv.writer(f)
        file_csv.writerow(['Product_page_url', 'Upc', 'Titre', 'Price_including_tax', 'Price_excluding_tax',
                           'Number_available', 'Product_description', 'Category', 'Review_rating', 'Image_url'])

        for x in info_book:
            file_csv.writerow(x)

    print("> Function : backup_data > Finished ")
    print('Finnish')

# ===============================================


def main():

    while True:

        for k, v in enumerate(title_category()):
            print(k, v)

        print("50 All categories")

        print('\n===============================')
        choice = input('Select a category [ 0 to 50 ] : ')
        print('---------------------')

        try:
            choice = int(choice)

        except TypeError:
            os.system('clear')
            continue

        except ValueError:
            os.system('clear')
            continue

        if choice >= 0 and choice <= 49:

            titre = title_category()[choice].lower()

            for i in category_link():
                if titre in i:
                    create_folders_and_pics_by_category([category_link()[choice]])
                    all_pages = nb_page_by_category([i])
                    infos_books = book_info(all_pages)
                    backup_data(infos_books)

        elif choice == 50:
            create_folders_and_pics_by_category(category_link())
            all_pages = nb_page_by_category(category_link())
            infos_books = book_info(all_pages)
            backup_data(infos_books)

        else:
            continue

        return False


if __name__ == "__main__":
    main()
