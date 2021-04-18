#we translate a .txt file or book in .txt format into the same folder where and python file
def split_into_sentences():
  a = int(input())#enter the number of characters that we want to be removed from the book
  handle = open('The Burning Secret.txt')#Choosing a book and writing it in quotes ('name.txt')
  data = handle.read(a)#wrine number
  print(data)#print these characters from the book
  handle.close()#close file
split_into_sentences()