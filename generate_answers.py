# script gerado com o chat gpt para gerar candidatos e respostas automaticamente

import random # importa a biblioteca random

def generate_answers():
    
  
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

    with open('gabarito.txt', 'r', encoding='utf8') as arquivo:
        template = arquivo.read().strip().split(',')
    
          
    with open("candidatos.txt", "w", encoding="utf-8") as arquivo: # cria arquivo candidatos.txt
        
        
        for i in range(100): # laço de repetição para gerar 100 linhas de dados
        
            id_candidate = random.randint(10000, 99999)   # gera um id aleatório de 5 números
            name = names[i] # variável name recebe valores dos índices da lista names
            skill = random.choice([0.3, 0.5, 0.7, 0.9])  # cria níveis de habilidade para gerar dados mais próximos a realidade
            answers = [] # inicia lista de respostas
    
            for correct_answer in template: #percorre respostas do gabarito
                if random.random() < skill: # se habilidade for maior que a escolha aleatoria
                    answers.append(correct_answer) # adiciona a resposta correta a lista de respostas
                else: # se não
                    answers.append(random.choice(alternatives)) # adiciona uma alternativa aleatoria a lista de respostas
        
            line = f"{id_candidate},{name}," + ",".join(answers) # formata a disposição dos dados no arquivo
            
            arquivo.write(line + "\n") # escreve as 100 linhas formatas (quebrando linha)

    print("Arquivo 'candidatos.txt' criado com sucesso!")

# =============================================================================
