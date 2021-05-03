#Download regex with help comand "pip install regex"
#Write all words in book with capital letter
import regex
#we translate a .txt file or book in .txt format into the same folder where and python file
def split_into_sentences():
  output = []
  handle = open('The Burning Secret.txt')#Choosing a book and writing it in quotes ('name.txt')
  data = handle.read()#open book in python
  words = re.sub('\W', ' ', data).split()
  for i in words:
    if i[0] == i[0].upper():
        output.append(i)
  print(output)
  handle.close()#close file
split_into_sentences()