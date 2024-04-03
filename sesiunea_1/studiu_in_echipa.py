
#Ex_1 - Definiți o adresă de memorie care să salveze data curentă. Va fi o variabilă sau o constantă?
from datetime import date
today = date.today()
print(today)

#Ex_2 - Identificați tipul de dată pe care îl are variabila pe care ați definit-o folosind una din funcțiile învățate la curs
print(type(today))

#Ex_3 - Definiți alte câteva variabile care să stocheze cursul la care sunteți, ce zi este și la ce sesiune de curs sunteți.

nume_curs = input(f'introduceti numele cursului: ')
data_de_azi = input ('introduceti data: ')
sesiune_curs = input(f'introduceti sesiunea de curs: ')
print("nume_curs +" "+ data_de_azi +" "+ sesiune_curs" )

# Ex_4 - Salvați fiecare cuvânt din propoziția: “Ana s-a nascut in anul 1990” în câte o adresă de memorie.
word1 = "Ana"  # Variabilă pentru primul cuvânt
word2 = "s-a"  # Variabilă pentru al doilea cuvânt
word3 = "născut"  # Variabilă pentru al treilea cuvânt
word4 = "în"  # Variabilă pentru al patrulea cuvânt
word5 = "anul"  # Variabilă pentru al cincilea cuvânt
word6 = "1990"  # Variabilă pentru al șaselea cuvânt
print(word1, word2, word3, word4, word5, word6)

#Ex_5 - Printați propoziția de mai sus folosind trei tipuri diferite de printuri.
print(f"{word1} {word2} {word3} {word4} {word5} {word6}")

#Ex_6 - Declarați câteva alte adrese de memorie la alegere și inițializați-le folosind funcția input.
# Variabilă pentru input de la utilizator
user_input2 = input("Introduceți al doilea input: ")