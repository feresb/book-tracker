# books.py
books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    rating = input("Rate it (1-5): ")
    books.append({"title": title, "author": author, "rating": rating})
    print(f"Added '{title}'!")

def view_books():
    print("\nYour Books:")
    for book in books:
        print(f"{book['title']} by {book['author']} | Rating: {book['rating']}/5")

while True:
    print("\n1. Add Book\n2. View Books\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        break
