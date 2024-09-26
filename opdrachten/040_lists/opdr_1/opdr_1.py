# Opdracht 1 lists
# Naam student:
# Groep:

# Maak een lege lijst aan
personen_lijst = []

# Maak 4 dictionaries voor de gegevens van personen
persoon1 = { "id": 0, "voornaam": "Jan", "achternaam": "Jansen" }
persoon2 = { "id": 1, "voornaam": "Piet", "achternaam": "Peters" }
persoon3 = { "id": 2, "voornaam": "Karin", "achternaam": "Kramer" }
persoon4 = { "id": 3, "voornaam": "Sophie", "achternaam": "Smit" }

# Voeg de dictionaries toe aan de lijst
personen_lijst.append(persoon1)
personen_lijst.append(persoon2)
personen_lijst.append(persoon3)
personen_lijst.append(persoon4)

# Print de volledige naam van de 2e persoon
print(personen_lijst[1]["voornaam"], personen_lijst[1]["achternaam"])
