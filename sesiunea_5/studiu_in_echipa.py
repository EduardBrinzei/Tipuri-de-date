# #Definiti o funcție cu parametri si return care să calculeze și să returneze suma a două numere.
def suma(a, b):
    return a + b
print(suma(3, 4))
# Definiti o funcție care să returneze TRUE dacă un număr este par sau FALSE daca numarul este impar
def este_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
print(este_par(5))

# Definiti o funcție o care returnează numărul total de caractere din numele tău complet (nume, prenume, nume_mijlociu)
def numar_caractere_nume_complet(nume, prenume, nume_mijlociu=""):
    return len(nume) + len(prenume) + len(nume_mijlociu)
print(numar_caractere_nume_complet("Doe", "John", "Smith"))

# Definiti o funcție care returnează aria unui dreptunghi cu laturile primite prin parametru
def aria_dreptunghi(latura1, latura2):
    return latura1 * latura2
print(aria_dreptunghi(5, 4))

# Definiti o funcție care returnează aria unui cerc si o returneaza. Raza va fi primita prin parametru.

# Funcție care returnează TRUE dacă un caracter x se găsește într-un string dat și FALSE in caz contrar.
# Definiti o funcție fără return care primește un string și printează pe ecran:
# Numărul de caractere lower case este x
# Numărul de caractere upper case exte y
# Definiti o funcție care primește ca parametru o LISTĂ de numere și returnează o alta LISTĂ doar cu numerele pozitive
# Definiti o funcție care nu returneaza nimic dar care primește două numere și PRINTEAZĂ
# Primul număr x este mai mare decat al doilea număr y
# Al doilea număr y este mai mare decat primul număr x
# Numerele sunt egale.

#Funcție pentru verificarea dacă un caracter se găsește într-un șir de caractere:

def caracter_in_string(caracter, string):
    return caracter in string
print(caracter_in_string('a', 'Python'))

# Funcție pentru afișarea numărului de caractere lowercase și uppercase dintr-un string:

def afisare_caractere_lowercase_uppercase(string):
    numar_lowercase = sum(1 for caracter in string if caracter.islower())
    numar_uppercase = sum(1 for caracter in string if caracter.isupper())
    print("Numărul de caractere lowercase este", numar_lowercase)
    print("Numărul de caractere uppercase este", numar_uppercase)
afisare_caractere_lowercase_uppercase('Hello World')

# Funcție pentru a filtra numerele pozitive dintr-o listă și returna o altă listă cu numerele pozitive:

def numere_pozitive(lista):
    lista_pozitive = [numar for numar in lista if numar > 0]
    return lista_pozitive
lista_initiala = [-1, 2, -3, 4, -5, 6]
print(numere_pozitive(lista_initiala))

# Funcție pentru a printa un mesaj care compară două numere:

def comparare_numere(x, y):
    if x > y:
        print("Primul număr", x, "este mai mare decât al doilea număr", y)
    elif x < y:
        print("Al doilea număr", y, "este mai mare decât primul număr", x)
    else:
        print("Numerele sunt egale.")
comparare_numere(3, 5)
comparare_numere(5, 3)
comparare_numere(5, 5)

# Funcție pentru adăugarea unui număr într-un set și returnarea unui mesaj corespunzător:

def adauga_in_set(numar, set_numere):
    if numar not in set_numere:
        print("Am adăugat numărul nou în set.")
        set_numere.add(numar)
        return True
    else:
        print("Nu am adăugat numărul în set. Acesta există deja.")
        return False
set_numere = {1, 2, 3}
print(adauga_in_set(4, set_numere))

#  Funcție pentru un calculator care returnează suma, diferența, înmulțirea și împărțirea a două numere:

def calculator(a, b):
    suma = a + b
    diferenta = a - b
    inmultire = a * b
    if b != 0:
        impartire = a / b
    else:
        impartire = None
    return suma, diferenta, inmultire, impartire
print(calculator(10, 5))

#  Funcție pentru a număra aparițiile cifrelor dintr-o listă și a le adăuga într-un dicționar:

def numar_aparitii_cifre(lista):
    dictionar_aparitii = {}
    for cifra in lista:
        if cifra in dictionar_aparitii:
            dictionar_aparitii[cifra] += 1
        else:
            dictionar_aparitii[cifra] = 1
    return dictionar_aparitii
print(numar_aparitii_cifre([1, 2, 3, 2, 1, 3]))

# Funcție pentru a returna valoarea maximă dintre trei numere:

def valoare_maxima(a, b, c):
    return max(a, b, c)
print(valoare_maxima(10, 20, 15))

# Funcție pentru a calcula suma numerelor de la 0 la un anumit număr:

def suma_pana_la(numar):
    return sum(range(numar + 1))
print(suma_pana_la(5))

#  Funcție pentru a găsi numerele comune din două liste:

def numere_comune(lista1, lista2):
    return list(set(lista1) & set(lista2))
print(numere_comune([1, 2, 3, 4], [3, 4, 5, 6]))

#  Funcție pentru aplicarea unei reduceri de preț:

def reducere_pret(pret_initial):
    if pret_initial > 100:
        pret_recalculat = pret_initial * 0.9  # Reducere de 10%
    else:
        pret_recalculat = pret_initial
    return pret_recalculat
print(reducere_pret(120))