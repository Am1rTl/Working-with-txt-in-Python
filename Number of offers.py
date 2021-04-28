#we translate a .txt file or book in .txt format into the same folder where and python file
class readbook():
  def __init__(self, book_name):  # heading
    self.handle = open('The Burning Secret.txt')#Choosing a book and writing it in quotes ('name.txt')
    self.data = self.handle.read()#wrine number
    self.co = 0
    self.words = []
    self.kolwords = []
    self.lenght = 0
  def counter(self):
    for i in range(0,len(self.data)):
      if self.data[i] == '.' or self.data[i] == '!' or self.data[i] == '?' :
        self.co = self.co+1

  def print(self):
    print(self.co)

  def close(self):
    self.handle.close()
book = readbook('The Burning Secret.txt')
book.counter()
book.close()
book.print()