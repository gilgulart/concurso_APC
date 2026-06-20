from exam_validator import classification # importa lista de classificação criada pela valiadação

classification.sort(key=lambda candidate: candidate[2], reverse=True) # ordena a classificação do maior para o menor

with open('classificacao.txt', 'w', encoding='utf-8') as arquivo: # cria arquivo classificação
    for candidate in classification: # percorre valores da lista classification
        line = ",".join(map(str, candidate)) # transforma a lista em string
        arquivo.write(line + '\n') # escreve cada elemento da lista
    print('Arquivo gerado')