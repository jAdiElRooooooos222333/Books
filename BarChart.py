import csv
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


ratings = []
page = []

with open("YA_Books.csv", mode="r") as bookFile:
    books = csv.reader(bookFile)
    next(books)  # skip 1st row/ header

    for book in books:
            
            pages = int(book[5])
            rating = float(book[6])
            ratings.append(rating)
            page.append(pages)

#bottom
x = np.array(ratings)
#side
y = np.array(page)

plt.bar(x,y , width = 0.0225, color = "black")
plt.xlabel("Ratings")
plt.ylabel("Pages")
plt.title("Books Ratings to Pages per book")
plt.xticks(rotation = 45)
plt.show()

