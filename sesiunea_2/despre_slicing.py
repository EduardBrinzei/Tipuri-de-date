#  alabalaportocala -> string
# ma folosesc de slicing pentru a putea scoate partea din "cuvant" sau litera de care am nevoi
#slicing = segmentare a unui string

'''
Ultimul caracter din string se ia din string dacă scriem ca poziție de început -1. Exemplu: print(string_text[-1])
Dacă vrem să parcurgem string-ul în reverse, trebuie să scriem -1 în locul step-ului. Exemplu: print(string_text[0:9:-1]
Dacă vrem să parcurgem string-ul de la început, se poate omite poziția de start. Exemplu: print(string_text[:9:1]
Dacă vrem să parcurgem string-ul pana la final se poate omite poziția de final. Exemplu: print(string_text[0::1]
Dacă vrem să parcurgem string-ul consecutiv (fiecare caracter) se poate omite step-ul. Exemplu: print(string_text[0:9]
Dacă le vrem pe toate implicite se pot omite în același timp. Exemplu: print(string_text[::])
'''

stringu1_1 = "alabala portocalax"
#extragerea ultimului
print(stringu1_1[-1])
print(stringu1_1[0])

#functia len() -> ne da lungimea sirului de caractere

#       [                de aici:             pana aici :       pasul                           ]
# inceput slicing       pozitie start:      pozitie final :     cum se parcurge stringul        incheiere slicing

print(len(stringu1_1))
#parcurgerea stringului invers
print(stringu1_1[::-1])  # -> cand vrem sa citim invers, nu dam pozitia start, nu dam pozitia de final, dam doar pasul invers (-1)

# vrem sa oarcurgem tot stringul mai putin pozitia de start
print(stringu1_1[:len(stringu1_)])
