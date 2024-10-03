# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

def bereken_derde_zijde(a, b):
    # Bereken de lengte van de derde zijde c met de stelling van Pythagoras
    c = math.sqrt(a**2 + b**2)
    return c

def get_float_input(prompt):
    while True:
        try:
            # Probeer een getal in te voeren
            return float(input(prompt))
        except ValueError:
            # Als er geen getal wordt ingevoerd, geef de foutmelding weer
            print("Voer een getal in")

# Vraag de gebruiker om de lengtes van de zijden a en b in te voeren
a = get_float_input("Voer de lengte van zijde a in: ")
b = get_float_input("Voer de lengte van zijde b in: ")

# Bereken de lengte van zijde c
c = bereken_derde_zijde(a, b)

# Geef het resultaat weer
print(f"De lengte van de derde zijde c is: {c}")