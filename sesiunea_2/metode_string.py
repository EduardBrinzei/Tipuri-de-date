'''
String methods reprezintă toate metodele (funcții definite într-o clasă - vor fi învățate în detaliu la cursul de OOP) care pot fi folosite împreună cu un string
Ele pot fi accesate prin intermediul string-ului urmat de caracterul “.” care ne oferă toate funcțiile pe care le putem folosi.

Exemple de funcții:

replace(caracter_de_inlocuit, caracter_cu_care_se_inlocuieste, cate_din_caracterele_gasite_sa_inlocuiasca)
upper
lower
split (delimitator_dupa_care_sa_splituiasca_stringul)
index (caracter_cautat)
isLower
capitalize
isDecimal/isDigit/isNumeric
count
len
'''

propozitia = "Cobori incet luceafar bland"

#replace
#vreau sa inlocuiesc litera "c" cu litera "k"
print(propozitia.replace("c","k"))

#split
print(propozitia.split())                            # -> impartire standard se face dupa spatii
print(propozitia.split("o"))                         # -> impartire dupa caracter dat de noi
print(propozitia.split(None, 2))        # -> numarul de impartiri definite de noi
print(propozitia.split("e", 1))         # --> impartire dupa un anume caracter si numar de impartiri

#upper  -> ne transforma in CAPS  #LOWER -> NE TRANSFORMA DIN CAPS in litere mici
print(propozitia.upper())
print(propozitia.lower())

#index -> ne da pozitia unui caracter in cadrul stringului
#vreau sa aflu pe ce pozitie se afla caracterul "t"
print(propozitia.index("t"))

#islower  -> ne returneaza adevarat daca stringul este format in totalitate din litere mici si Fals daca nu
#capitalize
print(propozitia.islower())     # ne face primul caracter cu litera mare si restul cu litere mici


#count -> ne returneaza nr de aparitii a unui caracter in cadrul springului
print(propozitia.count("t"))

#isDecimal/isDigit/isNumeric
prop2 = "2345"
print(prop2.isdigit())     # ne returneaza adevarat daca toate caracterele stringului sunt numere
prop3 = "3.14"
print(prop3.isdecimal()) #ne returneaza adevarat daca stringul este numar cu virgula

prop4 ="XXIII"
print(prop4.isnumeric()) # ne returneaza adevarat daca toate caracterele stringului sunt nummere