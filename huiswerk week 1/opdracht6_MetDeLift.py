van = int(input("op welke etage ben je nu? "))
naar = int(input("naar welke etage ga je toe? "))

if van > naar:
    print("je gaat naar beneden van " + str(van) + " naar " + str(naar))
if van < naar:
    print("je gaat naar boven van " + str(van) + " naar " + str(naar))
if van == naar:
    print("je gaat blijft op etage " + str(naar))

if van + 1 == naar:
    print("ga liever met de trap")
