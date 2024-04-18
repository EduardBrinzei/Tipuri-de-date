'''
Operatorii aritmetici sunt, așa cum le spune și numele, operatori care sunt folosiți pentru efectuarea operațiilor aritmetice.

Mai jos puteți găsi câțiva dintre cei mai cunoscuți operatori aritmetici:

addition (+) -> efectuează operații de adunare: suma = salariu + 100
substraction (-) -> efectuează operații de scădere: suma = salariu - 100
multiplication (*) -> efectuează operații de înmulțire: suma = salariu * 2
division (/) -> efectuează operații de împărțire: suma = salariu / 0.05
modulo (%) -> returnează restul împărțirii dintre un deîmpărțit și un împărțitor: rest = 11 % 2 # returneaza 1
exponential (**) -> efectuează operații de ridicare la putere: power = 2**3 # returneaza 8
floor division (//) -> efectuează operații de împărțire după care taie zecimalele suma = 10 // 3 # returneaza 3
'''

# OPERATORI ARITMETICI (+, -, :, *, /, **, %, // )
# ** -> ridicarea la putere
# % -> modulo si reptrezinta restul
# // -> returneaza catul impartirii

nr1 = 5
nr2 = 2
print(nr1 + nr2)
print(nr1 - nr2)
print(nr2 / nr1)
print(nr2 // nr1)
print(nr1 % nr2)
print(nr1 ** nr2)

#operatorii de comparatie (<, >, <=, >=, ==, !=)
# == operator de comparatie NU INCURCATI CU = care este ATRIBUIRE
# != diferit

nr1 = 5
nr2 = 2
print(nr1 < nr2)
print(nr1 > nr2)
print(nr1 <= nr2)
print(nr1 >= nr2)
print(nr1 == nr2)
print(nr1 != nr2)

#OPERATORI ATRIBUIRE (=, +=,-=, *=, /=)
nr1 = 6     # cu atribuirea putem suprascrie valorile unei variabile
print(nr1)

# += -> in traducere libera este: eu plus ceva
nr1 += 3 #-> nr1 = nr +3
print(nr1)

nr1 -= 8
print(nr1) #-> in traducere libera este: eu minus ceva

# *= inseamnaca eu inmultit cu ceva
nr1 *= 10
print(nr1)

# /= inseamna eu impartit la ceva
nr1 /=2
print(nr1)

#operatorii logici (AND, OR, NOT)
#AND -> si
# OR -> sau
# NOT inseamna opusul si Not nu exista

nr1 = 5
nr2 = 2
print(nr1 < nr2 and nr1 <= nr2)
# intrebam daca nr 1 este mai mic decat nr 2 si in acelasi timp daca nr 1 este mai mic sau egal cu nr2)
# FALS si FALS

nr1 = 5
nr2 = 5
print(nr1 < nr2 and nr1 <= nr2)
#FALS SI TRUE -> FALS  cu AND se cere indeplinirea ambelor conditii, intre un True si un Fals va fi fals

nr1 = 5
nr2 = 5
print(nr1 < nr2 or nr1 <= nr2)
#FALS sau TRUE -> TRUE una din cele 2 conditii este indeplinita TRUE + FAKS = TRUE

nr1 = 8
nr2 = 5
print(nr1 < nr2 or nr1 <= nr2)
#

nr1 = 5
nr2 = 2
print(nr1 > nr2 and nr1 <= nr2)
# True + true -> true

nr1 = 3
nr2 = 4
print(not 3 < 4)
#true -> not true = fals

string324 = "cvl"
print("a" not in "string324")