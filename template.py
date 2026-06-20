# lista com as respostas corretas
template = [
    "B", "C", "A", "D", "E",
    "D", "B", "C", "E", "E",
    "E", "B", "B", "D", "D",
    "C", "B", "C", "A", "A"
]

# cria arquivo gabarito.txt
with open("gabarito.txt", "w", encoding="utf-8") as arquivo:
    # Escreve as respostas separadas por virgula
    arquivo.write(",".join(template))

print("Arquivo 'gabarito.txt' criado com sucesso!") 