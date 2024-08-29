# import random
#
# cuvinte = ["TELEFON", "CASTI", "MONITOR", "ANIMAL", "ADIDASI", "ENCICLOPEDIE"]
# jocinpornire = True
# cuvantales = random.choice(cuvinte)
# attempts = len(cuvantales) + 4
#
# tabla = [ "_"] * len(cuvantales)
#
# print(" ".join(tabla))
# print(f"Ai {attempts} încercări")
#
# while "_" in tabla and attempts > 0:
#     litera = input("scrie o litera: ").upper()
#
#     if litera in cuvantales:
#         for i, char in enumerate(cuvantales):
#             if char == litera:
#                 tabla[i] = litera
#     else:
#         attempts -= 1
#         print(f"Litera nu este în cuvânt. Îți mai rămân {attempts} încercări.")
#
#     print(" ".join(tabla))
#
# if "_" not in tabla:
#     print(" ai ghicit cuvântul:", cuvantales)
# else:
#     print("Ai rămas fără încercări. Cuvântul era:", cuvantales)


# import random
# import unidecode
#
#
# # Functie pentru a citi si procesa lista de cuvinte
# def citeste_cuvinte(fisier):
#     with open(fisier, 'r', encoding='utf-8') as f:
#         cuvinte = f.readlines()
#
#     # Eliminam spatiile de la inceput si sfarsit si diacriticile
#     cuvinte = [unidecode.unidecode(cuvant.strip()) for cuvant in cuvinte]
#
#     # Filtram cuvintele care contin doar litere si au exact 5 litere
#     cuvinte = [cuvant for cuvant in cuvinte if len(cuvant) >= 5 and cuvant.isalpha()]
#
#     return cuvinte
#
#
# # Functia principala de joc
# def joc_hangman():
#     fisier = r'C:\Users\alber\Documents\listOfWords.txt'
#     # Aici ar trebui sa specifici calea corecta catre fisierul descarcat
#     cuvinte = citeste_cuvinte(fisier)
#
#     if not cuvinte:
#         print("Nu s-au gasit cuvinte valide in fisier.")
#         return
#
#     cuvantales = random.choice(cuvinte).upper()
#     attempts = len(cuvantales) + 4
#
#     tabla = ["_"] * len(cuvantales)
#
#     print(" ".join(tabla))
#     print(f"Ai {attempts} încercări")
#
#     while "_" in tabla and attempts > 0:
#         litera = input("Scrie o litera: ").upper()
#
#         if litera in cuvantales:
#             for i, char in enumerate(cuvantales):
#                 if char == litera:
#                     tabla[i] = litera
#         else:
#             attempts -= 1
#             print(f"Litera nu este în cuvânt. Îți mai rămân {attempts} încercări.")
#
#         print(" ".join(tabla))
#
#     if "_" not in tabla:
#         print("Ai ghicit cuvântul:", cuvantales)
#     else:
#         print("Ai rămas fără încercări. Cuvântul era:", cuvantales)
#
#
# # Pornim jocul
# joc_hangman()


# import random
# import unidecode
# import requests
#
#
# # Functie pentru a citi si procesa lista de cuvinte
# def citeste_cuvinte(fisier):
#     with open(fisier, 'r', encoding='utf-8') as f:
#         cuvinte = f.readlines()
#
#     # Eliminam spatiile de la inceput si sfarsit si diacriticile
#     cuvinte = [unidecode.unidecode(cuvant.strip()) for cuvant in cuvinte]
#
#     # Filtram cuvintele care contin doar litere si au exact 5 litere
#     cuvinte = [cuvant for cuvant in cuvinte if len(cuvant) >= 5 and cuvant.isalpha()]
#
#     return cuvinte
#
#
# # Functie pentru a obtine definitiile unui cuvant de la dexonline
# def obtine_definitii(cuvant, numar_definitii=5):
#     url = f"https://dexonline.ro/definitie/{cuvant}/json"
#     try:
#         response = requests.get(url)
#
#         if response.status_code != 200:
#             return f"Eroare HTTP: {response.status_code}. Nu s-a putut accesa definiția."
#
#         data = response.json()
#
#         # Verificam daca exista definitii in raspunsul JSON
#         if data.get('definitions') and isinstance(data['definitions'], list):
#             definitii = []
#             for i, definitie in enumerate(data['definitions']):
#                 if i >= numar_definitii:
#                     break
#                 definitii.append(definitie.get('internalRep', "Definiție indisponibilă"))
#             return "\n".join(definitii)
#         else:
#             return "Nu s-a găsit nicio definiție."
#
#     except requests.exceptions.RequestException as e:
#         return f"Eroare la accesarea definiției: {str(e)}"
#     except ValueError:
#         return "Eroare la procesarea răspunsului JSON."
#
#
# # Functia principala de joc
# def joc_hangman():
#     fisier = r'C:\Users\alber\Documents\listOfWords.txt'  # Specifica calea corecta catre fisierul tau
#     cuvinte = citeste_cuvinte(fisier)
#
#     if not cuvinte:
#         print("Nu s-au gasit cuvinte valide in fisier.")
#         return
#
#     cuvantales = random.choice(cuvinte).upper()
#     attempts = len(cuvantales) + 4
#
#     tabla = ["_"] * len(cuvantales)
#
#     print(" ".join(tabla))
#     print(f"Ai {attempts} încercări")
#
#     while "_" in tabla and attempts > 0:
#         litera = input("Scrie o litera: ").upper()
#
#         if litera in cuvantales:
#             for i, char in enumerate(cuvantales):
#                 if char == litera:
#                     tabla[i] = litera
#         else:
#             attempts -= 1
#             print(f"Litera nu este în cuvânt. Îți mai rămân {attempts} încercări.")
#
#         print(" ".join(tabla))
#
#     if "_" not in tabla:
#         print("Ai ghicit cuvântul:", cuvantales)
#     else:
#         print("Ai rămas fără încercări. Cuvântul era:", cuvantales)
#
#     # Obtinerea si afisarea definitiilor cuvantului
#     definitii = obtine_definitii(cuvantales.lower())
#     print(f"Definițiile pentru cuvântul {cuvantales} sunt:\n{definitii}")
#
#
#  # Pornim jocul
# joc_hangman()





import random
import unidecode
import requests


# Functie pentru a citi si procesa lista de cuvinte
def citeste_cuvinte(fisier):
    with open(fisier, 'r', encoding='utf-8') as f:
        cuvinte = f.readlines()

    # Eliminam spatiile de la inceput si sfarsit si diacriticile
    cuvinte = [unidecode.unidecode(cuvant.strip()) for cuvant in cuvinte]

    # Filtram cuvintele care contin doar litere si au exact 5 litere
    cuvinte = [cuvant for cuvant in cuvinte if len(cuvant) >= 8 and cuvant.isalpha()]

    return cuvinte


# Functie pentru a obtine definitiile unui cuvant de la dexonline
def obtine_definitii(cuvant, numar_definitii=5):
    url = f"https://dexonline.ro/definitie/{cuvant}/json"
    try:
        response = requests.get(url)

        if response.status_code != 200:
            return f"Eroare HTTP: {response.status_code}. Nu s-a putut accesa definiția."

        data = response.json()

        # Verificam daca exista definitii in raspunsul JSON
        if data.get('definitions') and isinstance(data['definitions'], list):
            definitii = []
            for i, definitie in enumerate(data['definitions']):
                if i >= numar_definitii:
                    break
                definitii.append(definitie.get('internalRep', "Definiție indisponibilă"))
            return "\n".join(definitii)
        else:
            return "Nu s-a găsit nicio definiție."

    except requests.exceptions.RequestException as e:
        return f"Eroare la accesarea definiției: {str(e)}"
    except ValueError:
        return "Eroare la procesarea răspunsului JSON."


# Functie pentru a desena spanzuratoarea
def deseneaza_spanzuratoarea(incercari):
    stadii = [
        """
            -----
            |   |
                |
                |
                |
                |
                |
        --------
        """,
        """
            -----
            |   |
            O   |
                |
                |
                |
                |
        --------
        """,
        """
            -----
            |   |
            O   |
            |   |
                |
                |
                |
        --------
        """,
        """
            -----
            |   |
            O   |
           /|   |
                |
                |
                |
        --------
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
                |
                |
                |
        --------
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
                |
        --------
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
                |
                |
        --------
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
          /     |
                |
        --------
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
          /   \\ |
                |
        --------
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
          /   \\ |
         |      |
        --------
        """
    ]
    print(stadii[min(incercari, len(stadii) - 1)])


# Functia principala de joc
def joc_hangman():
    fisier = r'C:\Users\alber\Documents\listOfWords.txt'  # Specifica calea corecta catre fisierul tau
    cuvinte = citeste_cuvinte(fisier)

    if not cuvinte:
        print("Nu s-au gasit cuvinte valide in fisier.")
        return

    cuvantales = random.choice(cuvinte).upper()
    attempts = 10  # Numărul de încercări este fixat la 10

    tabla = ["_"] * len(cuvantales)

    print(" ".join(tabla))
    print(f"Ai {attempts} încercări.")

    incercari_gresite = 0

    while "_" in tabla and incercari_gresite < attempts:
        litera = input("Scrie o litera: ").upper()

        if litera in cuvantales:
            for i, char in enumerate(cuvantales):
                if char == litera:
                    tabla[i] = litera
        else:
            incercari_gresite += 1
            deseneaza_spanzuratoarea(incercari_gresite)
            print(f"Litera nu este în cuvânt. Îți mai rămân {attempts - incercari_gresite} încercări.")

        print(" ".join(tabla))

    if "_" not in tabla:
        print("Ai ghicit cuvântul:", cuvantales)
    else:
        print("Ai rămas fără încercări. Cuvântul era:", cuvantales)

    # Obtinerea si afisarea definitiilor cuvantului
    definitii = obtine_definitii(cuvantales.lower())
    print(f"Definițiile pentru cuvântul {cuvantales} sunt:\n{definitii}")


# Pornim jocul
joc_hangman()



































