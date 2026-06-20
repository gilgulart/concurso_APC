from exam_validator import exam_validator # importa lista de classificação criada pela valiadação

classification = exam_validator()
classification.sort(key=lambda candidate: candidate[2], reverse=True) # ordena a classificação do maior para o menor

def generate_classification():
    with open('classificacao.txt', 'w', encoding='utf-8') as arquivo: # cria arquivo classificação
        for candidate in classification: # percorre valores da lista classification
            line = ",".join(map(str, candidate)) # transforma a lista em string
            arquivo.write(line + '\n') # escreve cada elemento da lista
        print('Arquivo gerado')
        