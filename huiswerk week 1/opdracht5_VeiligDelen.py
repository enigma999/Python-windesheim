getal1 = int(input("wat is getal 1?"))
getal2 = int(input("wat is getal 2?"))
resultaatPlus = getal1 + getal2
resultaatMin = getal1 - getal2
resultaatVermenigvuldigen = getal1 * getal2
if getal2 != 0:
    resultaatDelendoor = getal1 / getal2
print(str(getal1) + " + " + str(getal2) + " = " + str(resultaatPlus))
print(str(getal1) + " - " + str(getal2) + " = " + str(resultaatMin))
print(str(getal1) + " * " + str(getal2) + " = " + str(resultaatVermenigvuldigen))
if getal2 != 0:
    resultaatDelendoor = getal1 / getal2
    print(str(getal1) + " / " + str(getal2) + " = " + str(resultaatDelendoor))
if getal2 == 0:
    print(str(getal1) + " / " + str(getal2) + " = ? (delen door 0 kan niet)")
