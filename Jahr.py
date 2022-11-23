# Schreibe ein Programm, dass ermittelt, ob ein Jahr ein Schaltjahr ist.
# 1. Jahr muss durch 4 teilbar sein. 
# 2. Ist das Jahr durch 100 teilbar, ist es kein Schaltjahr.
# 3. Ist das Jahr 400 teilbar, ist es trotzdem ein Schaltjahr.



while True:
    jahr = int(input("Geben sie das Jahr an: "))      
    if (jahr % 4 == 0) and (jahr % 100 != 0) or (jahr % 400 == 0):
        print(jahr , " ist ein Schaltjahr")
    else:
        print(jahr , " ist kein Schaltjahr")