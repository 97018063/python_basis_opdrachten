# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Begin met de lijst van pizza's
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizzas.sort()
print("Gesorteerde pizza's:", pizzas)

# Voeg naar eigen smaak nog een pizza toe
pizzas.append('yo-favorito')
print("Na toevoeging van een pizza:", pizzas)

# Verwijder de pizza die je het minst lekker vindt
# Stel dat we 'olivio' het minst lekker vinden
pizzas.remove('olivio')
print("Na het verwijderen van een pizza:", pizzas)

# Print de eerste 3 pizza's uit de lijst
eerste_drie = pizzas[:3]
print("Eerste 3 pizza's:", eerste_drie)

# Print alleen de middelste pizza uit de lijst
# Bereken de index van de middelste pizza
middel_index = len(pizzas) // 2
middelste_pizza = pizzas[middel_index:middel_index + 1]
print("Middelste pizza:", middelste_pizza)

# Print de laatste 3 pizza's uit de lijst
laatste_drie = pizzas[-3:]
print("Laatste 3 pizza's:", laatste_drie)
