# Structua Alternativa IF -> daca conditia este adevarata se ruleaa o bucata de cod, daca este falsa o alta bucata de cod

nr1 = 9
nr2 = 6

if nr1 <= nr2:      #daca conditia este adevarata face adunarea
    print(nr1+nr2)
print(nr1)      # este rulat oricum

if nr1 <= nr2:          #daca conditia este adevarata face adunarea
    print(nr1+nr2)
else:                       #daca conditia este falsa face scaderea
    print(nr1-nr2)
print(nr1)                  # este rulat oricum

nr1 = 9
nr2 = 6
if nr1< nr2:
    print(nr1 + nr2)
elif nr1 == nr2:
    print("AAAAAAAAAAAAAAAAAAAaUUUUU")
else:
    print(nr1 - nr2)
    print(nr1)