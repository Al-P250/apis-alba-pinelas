import random
import requests

url="https://thesimpsonsquoteapi.glitch.me/quotes"

webContent=requests.get(f"{url}")

personaje=webContent.json()

valores=list(personaje[0].values())
nombre=f"{valores[1]}"
adivinar=list("")
continuar=True
for j in range(len(nombre)):
        if nombre[j]==" ":
            adivinar+=nombre[j]
        else:
            adivinar+="_"
fallos=0
letras=len(nombre)/4
while continuar:
    print(f"{valores[0]}")
    print(str(adivinar))
    respuesta=input("¿Que personaje dijo esto? ")
    if respuesta==nombre:
        print("Enhorabuena")
        continuar=False
    if fallos<2:
        for i in range (int(letras)):
            ran=random.randint(0,len(nombre)-1)
            while adivinar[ran]!="_":
                ran = random.randint(0, len(nombre)-1)
            adivinar[ran]= nombre[ran]
        fallos+=1
    elif fallos>=2 and respuesta!=nombre:
        print(f"Has fallado, el personaje era: {nombre}")
        continuar=False