def exam_validator():
    with open('gabarito.txt', 'r', encoding='utf-8') as arquivo: # lê arquivo gerado para o gabarito
        
        for line in arquivo: # percorre arquivo
            template =  line.strip().split(",") # quebra a string lida no arquivo tranformando-a em lista


    candidates = [] # inicia lista candidates

    with open('candidatos.txt' , 'r' , encoding='utf-8') as arquivo: # lê arquivo gerado de candidatos
        
        for line in arquivo: # percorre arquivo
            candidates.append(line.strip().split(",")) # transforma as linhas do arquivo em lista ignorando espaços

    classification = [] # inicia lista classsification

    for candidate in candidates: # percorre valores da lista candidates
        
        id_candidate = candidate[0] # recebe o id de cada candidato
        name = candidate[1] # recebe o nome de cada candidato
        answers = candidate[2:] # fatia a lista deixando apenas as respostas
        score = 0 # inicia nota em 0
        
        for correct, answer in zip(template, answers): # percorre valores do gabarito e respostas de cada candidato
            if correct == answer: # verifica se os valores obtidos nas listas são estritamente iguais
                score += 1 # a cada questão acertada acrescenta 1 ponto a nota
                
        classification.append([id_candidate, name, score]) # cria lista composta com todos os candidatos e as respectivas notas
    
    return classification
exam_validator()