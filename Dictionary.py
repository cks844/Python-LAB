books={'book1':100,'book2':150,'book3':200}
print("Books:",books)
nb=input("Enter the book to add:")
n=int(input("stocks:"))
books.update({nb:n})
print("Updated books:")
for i in books.items():
    print(i)
d=input("Enter the book to delete : ")
p=books.pop(d)
print(books)
