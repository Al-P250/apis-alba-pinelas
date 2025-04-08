import random
import requests

url="http://rickandmortyapi.com/api/character/"
pAl=random.randint(1,826)

webContent=requests.get(f"{url}{pAl}")

personaje=webContent.json()

claves = list(personaje.keys())
valores =list(personaje.values())
continuar=True
fallos=0
localizacion=valores[6]
while continuar:
    print(personaje["name"])
    nombre=input("¿Cómo se llama el personaje?\n")
    if nombre==personaje["name"]:
        continuar=False
        print("Enhorabuena")
    elif fallos==0:
        print(f"The character is: {personaje["gender"]}")
        fallos+=1
    elif fallos==1:
        print(f"The character is: {valores[2]}")
        fallos+=1
    elif fallos==2:
        print(f"The character is a: {valores[3]}")
        fallos+=1
    elif fallos==3:
        print(f"The character comes from {localizacion["name"]}")
        fallos+=1
    else:
        print(f"Has fallado, el personaje era {personaje["name"]}" )
        continuar=False