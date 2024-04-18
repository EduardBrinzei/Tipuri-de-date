# FUNCTI SIMPPLE

#definirea unei functii simple
def printarea_propozitiei_hello_world():
    print("hello world !")
    print("prima mea functie")
    print("ieeei python is life")

#apelarea/infocarea functiei
printarea_propozitiei_hello_world()

def suma_a_doua_numere():
    a = 2
    b = 3
    print(f' suma numerelor {a} si {b} este {a+b}')

#apelarea/infocarea functiei
suma_a_doua_numere()

#definirea unei functii cu parametri

def suma_a_doua_numere_cu_parametrii(a,b):
    print(f'suma numerelor {a} si {b} este {a+b}')

#apelarea functiei cu parametrii
suma_a_doua_numere_cu_parametrii(6,20)
suma_a_doua_numere_cu_parametrii(5,12)

#suma_a_doua_numere_cu_parametrii(3,4,5)
#suma_a_doua_numere_cu_parametrii(3)
#suma_a_doua_numere_cu_parametrii()

#definirea unei functii cu parametru implicit (varsta pensionare)
def calcul_cat_mai_am_pana_la_pensionare(anul_nasterii, varsta_pensionare = 65):
    varsta_curenta = 2024-anul_nasterii
    print(f' Mai am {varsta_pensionare-varsta_curenta} ani pana l apensie')

calcul_cat_mai_am_pana_la_pensionare(2000, 50)
calcul_cat_mai_am_pana_la_pensionare(2000)

def care_este_par_care_este_impar(inceput_interval, sfarsit_interval, pasul=1):
    for i in range(inceput_interval, sfarsit_interval, pasul):
        if i%2 == 0:
            print(f'Numarul {i} este numar par')
        else:
            print(f'Numarul {i} este impar')

care_este_par_care_este_impar(50, 70)



# functiile fara return -> executa o actiune
# functiile cu return -> ele au o valoare

#functie simpla cu return
def returnare_text():
    return "Ma numesc Tutuca Petre"
returnare_text()

textul_meu = returnare_text()
print(textul_meu)

#functie cu return si parametri
def suma_laturilor_dreptunghiului(latime, lungime):
    return 2*latime + 2 * lungime

#am nevoie sa aflu perimetrul, jumatatea perimetrului si sfertul perimetrului
perimetru = suma_laturilor_dreptunghiului(2,4)
print(f'Perimetrul dreptunghiului esre: {perimetru}')
print(f'Jumatatea perimetrului este: {perimetru/2}')
print(f'Sfertul perimetrului este: {perimetru/4}')

#def calculator_sume(*numere) == def calculator_sume(*args)

#in momentul in care folosim *args ca si parametru al functiei , argumentele date la apelarea acesteia devin tuplu\
# * (steluta) ajuta la despachetarea tuplului

def calculator_sume(*args):
    suma = 0
    for numar in args:
        suma += numar
    return suma

print(f' Suma numerelor este: {calculator_sume(1)}')
print(f' Suma numerelor este: {calculator_sume(1,6,5)}')
print(f' Suma numerelor este: {calculator_sume(1,10000,2000,123,14,15,12,5343)}')

def suma_a_doua_numere(a:int, b:int) -> int:
    return a+b

#functii cu **kwargs -> se folosesc la functii care primesc ca argumente dictionare
# def afiseaza_fotbalisti(**kwargs):
# for key_echipa, value_echipa in kwargs.items():
# for key_jucator, value_jucator in value_echipa.items():
# print(f"La echipa {key_echipa} joaca jucatorul:")
# for key_detalii_jucator, value_detalii_jucator in value_jucator.items():
# print("Detalii jucator", f"{key_detalii_jucator}:{value_detalii_jucator}", sep=" - ", end=",")
# print("\n--------------------------------")
#
# dictionarul_meu = fotbalisti_pe_echipe={
#     "Barcelona":{
#         "Dica":{
#             "Nume complet":"Nicolae Dica",
#             "Varsta":45,
#             "Numar Tricou":10
#         },
#         "Banel":{
#             "Nume complet":"Banel Nicolita",
#             "Varsta":47,
#             "Numar Tricou":3
#         },
#         "Dukadam":{
#         "Nume complet":"Helmut Dukadam",
#         "Varsta":65,
#         "Numar Tricou":7
#         }
#     }
# }
#
# afiseaza_fotbalisti(**dictionarul_meu)




