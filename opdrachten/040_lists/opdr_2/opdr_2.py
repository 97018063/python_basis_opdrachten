# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

# Dictionary met rivieren en de landen waar ze doorheen stromen
rivier_info = { 
    "rijn": ["nederland", "duitsland", "frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

# Lijst met de rivieren
rivieren = list(rivier_info.keys())

# 1e rivier en 2e land
eerste_rivier = rivieren[0]  # 'rijn'
tweede_land_eerste_rivier = rivier_info[eerste_rivier][1]  # 'duitsland'
print(f"De rivier {eerste_rivier.capitalize()} stroomt onder andere door {tweede_land_eerste_rivier.capitalize()}")

# 2e rivier en 1e land
tweede_rivier = rivieren[1]  # 'maas'
eerste_land_tweede_rivier = rivier_info[tweede_rivier][0]  # 'nederland'
print(f"De rivier {tweede_rivier.capitalize()} stroomt onder andere door {eerste_land_tweede_rivier.capitalize()}")

# 3e rivier en 3e land
derde_rivier = rivieren[2]  # 'nijl'
derde_land_derde_rivier = rivier_info[derde_rivier][2]  # 'oeganda'
print(f"De rivier {derde_rivier.capitalize()} stroomt onder andere door {derde_land_derde_rivier.capitalize()}")
