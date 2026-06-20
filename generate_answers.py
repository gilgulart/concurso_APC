# script gerado com o chat gpt para gerar candidatos e respostas automaticamente

# importa a biblioteca random
import random

# lista nomes possíves
names = [
    "Ana", "Bruno", "Carlos", "Daniel", "Eduardo", "Fernanda", "Gabriel",
    "Helena", "Igor", "Juliana", "Kaique", "Larissa", "Marcos", "Natália",
    "Otávio", "Patrícia", "Rafael", "Sabrina", "Tiago", "Vanessa",
    "William", "Yasmin", "André", "Beatriz", "Caio", "Débora", "Enzo",
    "Felipe", "Giovana", "Hugo", "Isabela", "João", "Karen", "Leonardo",
    "Melissa", "Nicolas", "Olívia", "Paulo", "Renata", "Samuel",
    "Tatiane", "Vinícius", "Alisson", "Bianca", "Cristina", "Diego",
    "Elaine", "Fábio", "Gustavo", "Henrique", "Aline", "Breno", "Camila",
    "Douglas", "Elisa", "Flávia", "Geovana", "Heitor", "Ivan", "Jéssica",
    "Kevin", "Luan", "Michele", "Noemi", "Orlando", "Priscila", "Rodrigo",
    "Silvia", "Tomás", "Valéria", "Wesley", "Zilda", "Arthur", "Cecília",
    "Davi", "Esther", "Francisco", "Guilherme", "Isaac", "Lívia",
    "Mateus", "Nicole", "Pietro", "Raissa", "Sofia", "Theo", "Vitor",
    "Amanda", "Bárbara", "Cauã", "Denise", "Emanuel", "Fabiana",
    "Gisele", "Henri", "Júlio", "Lorena", "Murilo", "Pedro","Kaiky"
]

# lista alternativas possíveis
alternatives = ["A", "B", "C", "D", "E"]

# cria arquivo candidatos.txt 
with open("candidatos.txt", "w", encoding="utf-8") as arquivo:
    
    # laço de repetição para gerar 100 linhas de dados
    for i in range(100):
        
        # gera um id aleatório de 5 números
        id_candidate = random.randint(10000, 99999)

        # variável name recebe valores dos índices da lista names
        name = names[i]

        # list comprehension - cria lista com 20 elementos (respostas)
        # escolhendo uma das alternativas a cada laço
        answers = [random.choice(alternatives) for _ in range(20)]

        # formata a disposição dos dados no arquivo
        line = f"{id_candidate},{name}," + ",".join(answers)

        # escreve as 100 linhas formatas (quebrando linha)
        arquivo.write(line + "\n")

print("Arquivo 'candidatos.txt' criado com sucesso!")

# =============================================================================