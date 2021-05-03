#Download regex with help comand "pip install regex"
#Write all words in book
import regex
#we translate a .txt file or book in .txt format into the same folder where and python file
def split_into_sentences():
  handle = open('The Burning Secret.txt')#Choosing a book and writing it in quotes ('name.txt')
  data = handle.read()#open book in python
  words = re.sub('\W', ' ', data).split()
  print(words)
  handle.close()#close file
split_into_sentences()