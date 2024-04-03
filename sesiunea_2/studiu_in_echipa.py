#O variabilă este un container care poate stoca și manipula date sau valori în cadrul unui program. Aceste valori pot fi de diferite tipuri și pot fi folosite pentru a păstra informații necesare pentru executarea codului.

# Declara și inițializează variabilele
int_var = 10
string_var = "Hello, world!"
float_var = 3.14
bool_var = True
# Verifică tipurile de date ale variabilelor
print(type(int_var))
print(type(string_var))
print(type(float_var))
print(type(bool_var))

# Rotunjește variabila 'float' și verifică tipul de date
float_var = round(float_var)
print(type(float_var))


# Încercare de conversie a variabilei string în int folosind type casting
string_var2 = "7"
converted_int = int(string_var2)
print(converted_int)
print(type(converted_int))

# Încercare de conversie a variabilei boolean la int folosind type casting
converted_bool = int(bool_var)
print(converted_bool)
print(type(converted_bool))

# Schimbă valoarea variabilei boolean și reia conversia la int
bool_var = not bool_var
converted_bool = int(bool_var)
print(converted_bool)
print(type(converted_bool))

# Exemplu 1 - Rezolvarea nepotrivirilor de tip

# Variabilele
int_var = 42
string_var = "3.14"
float_var = "2.718"
bool_var = "True"

# Convertirea variabilelor la tipurile corecte
int_var = int(int_var)
string_var = float(string_var)
float_var = float(float_var)
bool_var = bool(bool_var)

# Printarea valorilor
print(int_var)
print(string_var)
print(float_var)
print(bool_var)

# Exemplu 2 - Citirea numelui și prenumelui de la tastatură și calcularea numărului de caractere

# Citirea numelui și prenumelui de la tastatură și calcularea numărului de caractere
nume = input("Introduceti numele: ")
prenume = input("Introduceti prenumele: ")
nume_complet = nume  + prenume
lungime_nume_complet = len(nume_complet)
print(f"Numele complet are {lungime_nume_complet} caractere.")

# Citirea lungimii și lățimii dreptunghiului de la tastatură
lungime = float(input("Introduceți lungimea dreptunghiului: "))
latime = float(input("Introduceți lățimea dreptunghiului: "))

# Calcularea ariei dreptunghiului
aria = lungime * latime

# Afișarea ariei dreptunghiului
print(f"Aria dreptunghiului este {aria}.")

# Stringul dat
sir = 'Coral is either the stupidest animal or the smartest rock'

# Numărul de apariții al cuvântului 'the'
aparitii_the = sir.count('the')

# Afisarea numarului de aparitii
print(f"Cuvântul 'the' apare de {aparitii_the} ori în string.")

# Stringul dat
sir = 'Coral is either the stupidest animal or the smartest rock'

# Înlocuirea tuturor aparițiilor lui 'the' cu 'THE'
sir_modificat = sir.replace('the', 'THE')

# Afisarea rezultatului
print(sir_modificat)

# Stringul dat
sir = 'Coral is either the stupidest animal or the smartest rock'

# Verificarea dacă stringul conține doar numere
assert all(caracter.isdigit() or caracter.isspace() for caracter in sir), "Stringul nu conține doar numere."
assert sir.isdigit()

# Afisarea unui mesaj de confirmare
print("Stringul conține doar numere sau spații.")