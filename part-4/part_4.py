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

### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

def add_new_book ():

    title = input("Whats the name of the book you are adding? - ")
    author = input("Who is the author of the book you are adding? - ")
    year = input("What year was the book published? - ")
    rating = input("What is the rating out of 5 stars? - ")
    pages = input("What is the page count of your book? - ")

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary
# print(add_new_book())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

def add_new_book2 ():

    title = input("Whats the name of the book you are adding? - ")
    author = input("Who is the author of the book you are adding? - ")
    year = int(input("What year was the book published? - "))
    rating = float(input("What is the rating out of 5 stars? - "))
    pages = int(input("What is the page count of your book? - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    my_book_list.append(book_dictionary)
    return book_dictionary

# print(add_new_book2())



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

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
    return my_book_list.append(book_dictionary)
# print(add_new_book3())




### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

def view_book(my_book_list):
    string = f"\nTitle: {my_book_list["title"]}\nAuthor: {my_book_list["author"]}\nYear: {my_book_list["year"]}\nRating: {my_book_list["rating"]}\nPages: {my_book_list["pages"]}\n "
    
    return string

def book_search (title):
    for book in my_book_list:
        if book["title"].strip().lower() == title.strip().lower():
            return book
    return None

def author_search (author):
    author_books = []
    for book in my_book_list:
        if book["author"].strip().lower() == author.strip().lower():
            author_books.append(book)
    return author_books if author_books else None

def home_library ():
    print("Welcome to your personal home library!\nPlease select the option you would like to procedd with.\nAdd a book to your library. - 1\nView the books in your library. - 2\nSearch for a book in your library - 3\nSearch for books by author - 4")

    option = int(input("Please enter the number for the corrosponding function you would like to use. - "))

    # print(option)

    if option == 1:
        add_new_book3()
    elif option == 2:
        for book in my_book_list:
            print(view_book(book))
    elif option == 3:
        search_title = input("Enter the title of the book you are looking for: ")
        found_book = book_search(search_title)

        if found_book:
            print("Book Found:")
            print(view_book(found_book))
        else:
            print("Book not found.")
    elif option == 4:
        search_author = input("Enter the author of the books you are searching for: ")
        found_author = author_search(search_author)

        if found_author:
            print("Books by the author found:")
            for books in found_author:
                print(view_book(books))
        else:
            print("Books by the author not found.")
    else:
        print("Please select a valid input. - ")

# home_library()

# view_books()
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

def main_menu ():

    active = True

    while active == True:
    
        print("Welcome to your personal home library!\nPlease select the option you would like to procedd with.\nAdd a book to your library. - 1\nView the books in your library. - 2\nSearch for a book in your library - 3\nSearch for books by author - 4\nExit - 5")

        option = int(input("Please enter the number for the corrosponding function you would like to use. - "))

        if option == 1:
            add_new_book3()
        elif option == 2:
            for book in my_book_list:
                print(view_book(book))
        elif option == 3:
            search_title = input("Enter the title of the book you are looking for: ")
            found_book = book_search(search_title)

            if found_book:
                print("Book Found:")
                print(view_book(found_book))
            else:
                print("Book not found.")
        elif option == 4:
            search_author = input("Enter the author of the books you are searching for: ")
            found_author = author_search(search_author)

            if found_author:
                print("Books by the author found:")
                for books in found_author:
                    print(view_book(books))
            else:
                print("Books by the author not found.")
        elif option == 5:
            print("Thanks for using your persoanl library.")
            active = False
        else:
            print("Please select a valid input. - ")

main_menu()
