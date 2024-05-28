my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374,
    "read" : True
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def library (dictionary):
    book_string = f"{dictionary["title"]} was written by {dictionary["author"]} in the year {dictionary["year"]}. It has an average rating of {dictionary["rating"]} and is {dictionary["pages"]} pages long."
    return book_string
print(library(my_book))
# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

def title (dictionary):
    title_string = f"Book: {dictionary["title"]}"
    return title_string

def author (dictionary):
    author_string = f"Author: {dictionary["author"]}"
    return author_string

def year (dictionary):
    year_string = f"Year: {dictionary["year"]}"
    return year_string

def rating (dictionary):
    rating_string = f"Rating: {dictionary["rating"]}"
    return rating_string

def pages (dictionary):
    pages_string = f"Pages: {dictionary["pages"]}"
    return pages_string

print(title(my_book))
print(author(my_book))
print(year(my_book))
print(rating(my_book))
print(pages(my_book))
# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def read (dictionary):
    read_string = f"Read: {dictionary["read"]}"
    return read_string

