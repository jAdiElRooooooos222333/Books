import csv
import matplotlib.pyplot as plt
import numpy as np

# comma separated value

with open("YA_Books.csv", mode="r") as bookfile:
    # mode "r" means read
    # mode "w" means write/edit

    books = csv.reader(bookfile)
    next(books)
    worst_rating = 5.0
    most_recent_published = 99999
    

    best_rating = 0.0
    most_pages = 0

    for book in books:
        author = (book[1])
        rating = float(book[6])
        year = int(book[2])
        #print all authors that start with letter "M":
        # if author.startswith("M"):
        #     print(author)

        # get mot recently published boook
        # if year > most_recent_published:
        #     most_recent_published = year
        #     most_recent_book = book

        # print(f"Most recently published: {most_recent_book}")
         #print book with worst rating

        # if rating < worst_rating:
           # worst_rating = rating
            # worst_rated_book = book

        # print (f"Book with worst rating{worst_rated_book}")
        # pages = int(book[5])
        # if year <= 2000:
            # if pages > most_pages:
                # most_pages = pages
                # most_pages_book = book

        # if rating > best_rating:
            # best_rating = rating
            # best_rated_book = book

        # print(f"Highest rated book is {best_rated_book}")
        # print (f"Book with worst rating{worst_rated_book}")
        # print(f"Book with most pages is {most_pages_book}")