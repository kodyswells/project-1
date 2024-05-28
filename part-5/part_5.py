### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

my_book_list = [{
    "title": "The Eye of the World",
    "author": "Robert Jordan",
    "year": 1990,
    "rating": 4.2,
    "pages": 782
},
{
    "title": "The Way of Kings",
    "author": "Brandon Sanderson",
    "year": 2010,
    "rating": 4.7,
    "pages": 1001
},
{
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},
{
    "title": "Dragonsdale",
    "author": "Salamandra Drake",
    "year": 2007,
    "rating": 4,
    "pages": 272
},
{
    "title": "Mistborn",
    "author": "Brandon Sanderson",
    "year": 2006,
    "rating": 4.5,
    "pages": 647
}
]

def add_new_book3 ():

    title = input("Whats the name of the book you are adding? - ")
    author = input("Who is the author of the book you are adding? - ")

    try:
        year = int(input("What year was the book published? - "))
    except:
        year = int(input("Please type a number for the year."))
    
    try:
        rating = float(input("What is the rating out of 5 stars? - "))
    except:
        rating = float(input("Please enter a number between 0 and 5."))

    try:    
        pages = int(input("What is the page count of your book? - "))
    except:
        pages = int(input("Please enter the page count as a number."))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    print("Book added to dictionary")
    with open("library.txt", "a") as f:
        f.write(f"{book_dictionary["title"]}, {book_dictionary["author"]}, {book_dictionary["year"]}, {book_dictionary["rating"]}, {book_dictionary["pages"]}\n")
    return book_dictionary

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.
def view_book(my_book_list):
    string = f"\nTitle: {my_book_list["title"]}\nAuthor: {my_book_list["author"]}\nYear: {my_book_list["year"]}\nRating: {my_book_list["rating"]}\nPages: {my_book_list["pages"]}\n "
    
    return string

def show_library ():
    with open("library.txt", "r") as f:
        for line in f:
            book_info = line.split(', ')
            book_dictionary = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            }
            print(view_book(book_dictionary))
# show_library()

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

file_path = "library.txt"

def add_new_book3 ():

    title = input("Whats the name of the book you are adding? - ")
    author = input("Who is the author of the book you are adding? - ")

    try:
        year = int(input("What year was the book published? - "))
    except:
        year = int(input("Please type a number for the year."))
    
    try:
        rating = float(input("What is the rating out of 5 stars? - "))
    except:
        rating = float(input("Please enter a number between 0 and 5."))

    try:    
        pages = int(input("What is the page count of your book? - "))
    except:
        pages = int(input("Please enter the page count as a number."))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    print("Book added to dictionary")
    with open(file_path, "a") as f:
        f.write(f"{book_dictionary["title"]}, {book_dictionary["author"]}, {book_dictionary["year"]}, {book_dictionary["rating"]}, {book_dictionary["pages"]}\n")
    return book_dictionary

def view_book(my_book_list):
    string = f"\nTitle: {my_book_list["title"]}\nAuthor: {my_book_list["author"]}\nYear: {my_book_list["year"]}\nRating: {my_book_list["rating"]}\nPages: {my_book_list["pages"]}\n "
    
    return string
def show_library ():
    with open(file_path, "r") as f:
        for line in f:
            book_info = line.split(', ')
            book_dictionary = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            }
            print(view_book(book_dictionary))

def book_search (title):
    with open(file_path, "r") as f:
        for line in f:
            book_info = line.strip().split(', ')
            book = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            }
            if book["title"].strip().lower() == title.strip().lower():
                return book

def author_search (author):
    author_books = []
    with open("library.txt", "r") as f:
        for line in f:
            book_info = line.strip().split(', ')
            book = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            }
            if book["author"].strip().lower() == author.strip().lower():
                author_books.append(book)
        return author_books if author_books else None



def average_rating (file_path):
    total_rating = 0
    count = 0
    with open(file_path, "r") as f:
        for line in f:
            book_info = line.strip().split(', ')
            book = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            }
            total_rating += book["rating"]
            count += 1
    average_rating = total_rating / count if count != 0 else 0
    return round(average_rating, 2)

def delete_book(file_path):

    with open(file_path, "r") as f:
        lines = f.readlines()

    title = input("What is the title of the book you are removing? ").strip().lower()

    updated_lines = []
    for line in lines:
        book_info = line.strip().split(', ')
        book_title = book_info[0].strip().lower()
        if book_title != title:
            updated_lines.append(line)

    print(f"\n{title} has been removed from you library\n")

    with open(file_path, "w") as f:
        f.writelines(updated_lines)

def total_page_count(file_path):
    total_count = 0
    with open(file_path, "r") as f:
        for line in f:
            book_info = line.strip().split(', ')
            book = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            }
            total_count += book["pages"]
    return f"{total_count} pages.\n"

def main_menu ():

    active = True

    while active == True:
        print("")
    
        print("Welcome to your personal home library! Please select the option you would like to proceed with.\nAdd a book to your library. - 1\nRemove a book from your library. - 2\nView your library. - 3\nSearch for a book in your library - 4\nSearch for books by author - 5\nAverage book rating for your library - 6\nTotal page count. - 7\nExit. - 8 \n")

        option = int(input("Please enter the number for the corresponding function you would like to use. - "))

        if option == 1:
            add_new_book3()
            input("Press Enter to continue...")

        elif option == 2:
            delete_book(file_path)
            input("Press Enter to continue...")

        elif option == 3:
            show_library()
            input("Press Enter to continue...")

        elif option == 4:
            search_title = input("Enter the title of the book you are looking for: ")
            found_book = book_search(search_title)

            if found_book:
                print("Book Found:")
                print(view_book(found_book))
            else:
                print("Book not found.")
            input("Press Enter to continue...")

        elif option == 5:
            search_author = input("Enter the author of the books you are searching for: ")
            found_author = author_search(search_author)

            if found_author:
                print("Books by the author found:")
                for books in found_author:
                    print(view_book(books))
            else:
                print("Books by the author not found.")
            input("Press Enter to continue...")

        elif option == 6:
            print("Here is your average rating for all of the books in your library: ")
            print(average_rating(file_path))
            input("Press Enter to continue...")

        elif option == 7:
            print("Here is the total page count for your library")
            print(total_page_count(file_path))
            input("Press Enter to continue...")
        elif option == 8:
            print("Thanks for using your personal library.")
            active = False
        else:
            print("Please select a valid input. - ")

if __name__ == "__main__":
    main_menu()