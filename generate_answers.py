# script gerado com o chat gpt para gerar candidatos e respostas automaticamente

import random # importa a biblioteca random


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
] # lista nomes possíves


alternatives = ["A", "B", "C", "D", "E"] # lista alternativas possíveis

 
with open("candidatos.txt", "w", encoding="utf-8") as arquivo: # cria arquivo candidatos.txt
    
    
    for i in range(100): # laço de repetição para gerar 100 linhas de dados
      
        id_candidate = random.randint(10000, 99999)   # gera um id aleatório de 5 números
        name = names[i] # variável name recebe valores dos índices da lista names
        answers = [random.choice(alternatives) for _ in range(20)] # list comprehension - cria lista com 20 elementos (respostas) escolhendo uma das alternativas a cada laço
        line = f"{id_candidate},{name}," + ",".join(answers) # formata a disposição dos dados no arquivo
        
        arquivo.write(line + "\n") # escreve as 100 linhas formatas (quebrando linha)

print("Arquivo 'candidatos.txt' criado com sucesso!")

# =============================================================================