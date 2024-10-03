# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

#gasten = ["Jij", ... ]

# Begin met een lege lijst
gastenlijst = []

# Voeg de gasten toe met behulp van de append() method
gastenlijst.append("Bas")
gastenlijst.append("Paul")
gastenlijst.append("Kees")
gastenlijst.append("Marie")
gastenlijst.append("Hilda")

# Toon de gastenlijst
print("De gastenlijst:", gastenlijst)

# Stel je voor dat er nog een gast komt, voeg deze toe
gastenlijst.append("Jan")
print("Na toevoeging van Jan:", gastenlijst)

# Sorteren van de gastenlijst alfabetisch
gastenlijst.sort()
print("Gesorteerde gastenlijst:", gastenlijst)

# Een gast kan niet komen, verwijder deze met remove()
gastenlijst.remove("Hilda")
print("Na het verwijderen van Hilda:", gastenlijst)

# Controleer het aantal gasten met len()
aantal_gasten = len(gastenlijst)
print("Het aantal gasten is:", aantal_gasten)

# Stel je voor dat een gast afzegt en je wilt de laatste verwijderen
laatste_gast = gastenlijst.pop()
print("Na het verwijderen van de laatste gast:", gastenlijst)
print("Verwijderde gast:", laatste_gast)