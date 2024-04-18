#structura assert

#cuvant cheie       expected result       comparatia      actual result       mesa de eroare (optional)
# assert            ce ar treui sa fie      ==            ce am obtinut.      EROOR

# cu operatorul egal

expected_result = 5
actual_result = 5

assert expected_result == actual_result, "FATAL ERROR"

print(expected_result+actual_result)

# cu operatorul mai mic

expected_result = 8
actual_result = 5

assert expected_result > actual_result, f"FATAL ERROR {expected_result} to be smaller than actual {actual_result}"

print(expected_result+actual_result)

# ne asteptam ca rezultatul sa fie mai mare ca 20

expected_result = 20
actual_result =  21

assert expected_result < actual_result, "ERROR"

print(expected_result)