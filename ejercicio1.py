lista_cervezas = [
	"Heiniken",
	"Aguila",
	"Corona",
	"Reds",
	"Gato",
	"Heiniken",
	"Aguila",
	"Corona",
	"Reds",
	"Gato",
	"Heiniken",
	"Aguila",
	"Corona",
	"Reds",
	"Gato",
	"Heiniken",
	"Aguila",
	"Corona",
	"Reds",
	"Gato",
]

# Crea un script (programa) que recorra la lista anterior y muestra con un print
#cuantas veces aparece cada cerveza en la lista
# el texto que deba imprimir seria:
"""
	Resltado de conteo de la lista:

	Heiniken : 4
	Aguila: 4
	Corona: 4
	R0eds: 4
	Gato: 4 
    .
"""


Heiniken = 0
Aguila = 0
Corona = 0
Reds = 0
Gato = 0

for ceverza in lista_cervezas:

    if ceverza == "Heiniken":
        Heiniken +=1
    elif ceverza == "Aguila":
        Aguila +=1
    elif ceverza == "Corona":
        Corona +=1
    elif ceverza == "Reds":
        Reds +=1
    elif ceverza == "Gato":
        Gato +=1

print(f"""
Heiniken = {Heiniken}
Aguila = {Aguila}
Corona = {Corona}
Reds = {Reds}
Gato= {Gato}
""")