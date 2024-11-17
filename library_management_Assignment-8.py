books = []
users = []

def add_book():
    book_id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    status = "Available"
    books.append({"ID": book_id, "Title": title, "Author": author, "Genre": genre, "Status": status})

def view_books():
    for book in books:
        print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")

def search_books():
    search_term = input("Enter search term (title, author, or genre): ")
    for book in books:
        if search_term.lower() in book['Title'].lower() or search_term.lower() in book['Author'].lower() or search_term.lower() in book['Genre'].lower():
            print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")

def borrow_book():
    user_id = int(input("Enter user ID: "))
    book_id = int(input("Enter book ID: "))
    for book in books:
        if book['ID'] == book_id and book['Status'] == "Available":
            book['Status'] = "Checked Out"
            for user in users:
                if user['ID'] == user_id:
                    user['Borrowed Books'].append(book)
            print("Book borrowed successfully.")
            return
    print("Book not found or not available.")

def return_book():
    user_id = int(input("Enter user ID: "))
    book_id = int(input("Enter book ID: "))
    for user in users:
        if user['ID'] == user_id:
            for book in user['Borrowed Books']:
                if book['ID'] == book_id:
                    book['Status'] = "Available"
                    user['Borrowed Books'].remove(book)
                    print("Book returned successfully.")
                    return
    print("Book not found or not borrowed by the user.")

def view_available_books():
    for book in books:
        if book['Status'] == "Available":
            print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}")

def view_checked_out_books():
    for book in books:
        if book['Status'] == "Checked Out":
            print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}")

def add_user():
    user_id = int(input("Enter user ID: "))
    name = input("Enter user name: ")
    users.append({"ID": user_id, "Name": name, "Borrowed Books": []})

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View Available Books")
        print("7. View Checked Out Books")
        print("8. Add User")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            search_books()
        elif choice == 4:
            borrow_book()
        elif choice == 5:
            return_book()
        elif choice == 6:
            view_available_books()
        elif choice == 7:
            view_checked_out_books()
        elif choice == 8:
            add_user()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()