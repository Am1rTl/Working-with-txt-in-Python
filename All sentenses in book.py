def counter(book,mass):
  string = ''
  chot = 1
  g = 0
  for i in range(len(book)): 
    string += book[i]
    if book[i] == '.' or book[i] == '!' or book[i] == '?' :
      mass.append(string)
      chot += 1
      string = ''

  return book , mass 
handle = open('The Burning Secret.txt', mode='r', encoding='utf-8-sig')
data = handle.read()
book_in_mass = []
counter(data,book_in_mass)
print(book_in_mass)
