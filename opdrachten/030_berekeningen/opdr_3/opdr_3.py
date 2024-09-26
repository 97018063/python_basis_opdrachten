# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

# Hier komt je code...
# Definieer de variabelen a en b
a = 4
b = -2

# Functie om y te berekenen
def calculate_y(x):
    y = (a * (x ** 3)) + (b * (x ** 2)) - 1
    return y

# Test met x = 1
x = 1
uitkomst = calculate_y(x)
print(f'De uitkomst is: {uitkomst}')

