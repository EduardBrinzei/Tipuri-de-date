
#print(10/0)        -> codul se opreste aici la eroare
#print("am ajuns la final")

try:
    print(10/0) #codul nu se opreste
except:
    print('Impartirea la 0 nu este permisa')
 #el continua
print("am ajuns la final")

suma_numere = 0
caracter_citi = ''  #citim de la tastatura cu functia imput

### varianta fara tratare de exceptie
# while caracter_citi != 0:
    #caracter_citi = int(input("Introduceti un numar si apasati tasta enter:"))
    #suma_numere += caracter_citi
   # print(suma_numere)


    ### varianta cu tratare de exceptie
#while caracter_citi != 0:
   # try:
      #  caracter_citi = int(input("Introduceti un numar si apasati tasta enter:"))
   # except ValueError:
     #   print('Ati introdus un alt tip de data')
   # else:
      #  suma_numere += caracter_citi
    #finally:
       # if caracter_citi != 0:
       #     print('CONTINUAM CALCULUL SUMEI')
       # else:
        #    print(f'Sfarsit, nu mai calcuma nimic, suma este {suma_numere}')

#ridicarea unei exceptii in mod intentionat

#nota_cursant = float(input("Introduceti nota de la examen:"))

#if nota_cursant < 4.5:
   # raise Exception("Ha Ha corigent !")
#print("Codul merge mai departe, bravo stai jos !")


