import os
class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.no_books = 0
        self.load_books()
    
    def load_books(self):
        if os.path.isfile("Library_Management.txt"):
            with open("Library_Management.txt", "r") as f:
                lines = f.readlines()
                for line in lines[2:]:
                    # if line.strip() and not line.startswith("You have following books in the system:"):
                        self.books.append(line.strip())
                self.no_books = len(self.books)
                    
    
    def add_books(self):
        
        while True:
            try:
                n = int(input("Number of books to be added: "))
                break
            except ValueError:
                print ("Please only use an integer!")
            
        print ("Enter the books: ")
        for new_books in range(n):
            new_books = input().strip()
            self.books.append(new_books)
        self.no_books = len(self.books)
        
    def show_books(self):
        print (f"Total number of books: {self.no_books}")
        print (f"You have following books in the system:\n")
        for book in self.books:
            print (book)
        
    def save_file(self):
        with open("Library_Management.txt", "w") as f:
            f.write(f"Total number of books: {self.no_books}")
            f.write(f"\nYou have following books in the system:\n")
            for book in self.books:
                f.write(f"{book}\n")
    
    def delete_books(self):
        print ("Current books in the system: ")
        for index, book in enumerate(self.books):
            print (f"{index+1}. {book}")
        
        while True:
            try:
                while True:
                    n = int(input("Enter the index of book to be deleted(or 0 to cancel): "))
                    if n == 0:
                        return
                    elif 1<= n <= len(self.books):
                        del self.books[n-1]                #deletes the index
                        self.no_books = len(self.books)
                        print ("Book deleted successfully!")
                        self.delete_books()
                        break
                    else:
                        print ("Invalid Choice")
                    break
            except ValueError:
                print ("Please only use an integer!")
            
a = LibraryManagementSystem()
def lms():
    while True:
        input("Press Enter to continue...")
        os.system("cls")
        print ("WELCOME TO THE LIBRARY MANAGEMENT SYSTEM")
        print ("1. Add Books")
        print ("2. Show Books")
        print ("3. Delete Books")
        print ("4. Save File")
        print ("5. Exit")
        try:
            choice = int(input())

            if choice == 1:
                a.add_books()
            elif choice == 2:
                a.show_books()
            elif choice == 3:
                a.delete_books()
            elif choice == 4:
                a.save_file()
            elif choice == 5:
                exit()
            else:
                print ("Invalid Choice")
                
        except ValueError:
            print ("Please only use an integer!")
        

lms()
        
        

