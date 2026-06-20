template = [ 
    "B", "C", "A", "D", "E",
    "D", "B", "C", "E", "E",
    "E", "B", "B", "D", "D",
    "C", "B", "C", "A", "A"
] # lista com as respostas corretas


with open("gabarito.txt", "w", encoding="utf-8") as arquivo: # cria arquivo gabarito.txt
    arquivo.write(",".join(template)) # Escreve as respostas separadas por virgula

print("Arquivo 'gabarito.txt' criado com sucesso!")