class Bookcollection:
    def __init__(self):
        self.collection={}

    def add_books(self,title,quantity):
        if title in self.collection:
            self.collection[title]+=quantity
        else:
            self.collection[title]=quantity

    def remove_book(self,title,quantity):
        if title in self.collection:
            self.collection[title]-=quantity
            if self.collection[title]<=0:
                print("Book Not Available")
        else:
            print(f"Book{title} not in collection")

    def Book_collection(self):
        if not self.collection:
            print("No Books")
        else:
            for title,quantity in self.collection.items():
                print(f"title {title},Quantity {quantity}")

    def Total_books(self):
        return sum(self.collection.values())

v=Bookcollection()
v.add_books("Bheem",5)
v.add_books("Maharaj",2)
v.Book_collection()

v.remove_book("Bheem",2)
v.Book_collection()

v.remove_book("Bheem",3)
v.Book_collection()

v.Book_collection()
v.add_books("Bheem",5)
v.add_books("Django",10)
v.Book_collection()