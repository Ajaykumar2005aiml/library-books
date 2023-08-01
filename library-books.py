class library:
  def __init__(self,books):
    self.lib_books=books
  def show(self):
    for i in range(len(self.lib_books)):
      print(i+1,self.lib_books[i])
  def del_lend(self,requested_book):
    self.lib_books.remove(requested_book)
  def add_book(self,add_bk):
    self.lib_books.append(add_bk)
class customer:
  def __init__(self):
    self.customer_lended_books=[]
  def lend(self):
    self.request=input("enter a book name for lend: ")
    if self.request in lib_obj.lib_books:
      print(self.request,"book is succsessfully installed")
      return self.request
    else:
      print("no books available like that")
      return False
  def add_books(self,requested_book):
    self.customer_lended_books.append(requested_book)
    print("***lended books***")
    print("lended books:",*self.customer_lended_books)
  def book_return(self,return_book):
    if return_book in self.customer_lended_books:
      self.customer_lended_books.remove(return_book)
      print(return_book+" book returnd succsessfully")
      print("remaining lended books:",*self.customer_lended_books)
      return return_book
    else:
      print("there is no book like that you lended")
lib_obj=library(["b1","b2","b3","b4","b5","b6"])
cust_obj=customer()
while True:
  print("****welcome to my library****")
  print("select a numbers below for your convenience:")
  option=int(input("0-for exit\n1-for show the books\n2-for lend a book\n3-for returning the book\n"))
  if option==1:
    print("***Available books***")
    lib_obj.show()
  elif option==2:
    requested_book=cust_obj.lend()
    if requested_book:
      lib_obj.del_lend(requested_book)
      cust_obj.add_books(requested_book)
  elif option == 3:
    retr_book=input("enter returning book name: ")
    add_lib=cust_obj.book_return(retr_book)
    lib_obj.add_book(add_lib)
  elif option==0:
    break
  else:
    print("pls enter a valid number less than 4")
