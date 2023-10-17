# Pengkondisian
benua = 'Eropa'
if(benua == 'Asia'):
    print('Indonesia, Malaysia, Philipina')
elif(benua == 'Eropa'):
    print('Spanyol, Italia, Francis')
elif(benua == 'Amerika'):
    print('Canada, USA, Mexico')
else:
    print('Unknown')
print('\n')



# Pengulangan
books = ['Belajar WEB', 'Bahasa Inggris', 'Panduan Developer']
for index, book in enumerate(books):
    print(f'{index + 1} - {book}')
print('\n')


# Number
import math
PI = math.pi
pembulatan = round(math.pi)
pecahan = float(pembulatan)
numbers = (6,3,8,2,4)
print(PI) # 3.14.........
print(pembulatan) # 3
print(max(numbers)) # 8
print(min(numbers)) # 2
print('\n')


# String
firstName = "muhammad"
lastName = 'friza'
print(firstName.capitalize() + ' ' + lastName.capitalize())