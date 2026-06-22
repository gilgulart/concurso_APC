import webbrowser # importa biblioteca webbrowser
from generate_answers import generate_answers #importa função generate_answers
from exam_validator import exam_validator #importa função exam_validator
from generate_classification import generate_classification # importa função generate_classification

def menu(): # cria menu de navegação
    print('1 - Exibir candidados')
    print('2 - Exibir Gabarito')
    print('3 - Exibir Classificação')
    print('4 - Sair \n')

while True: # inicia loop do programa
    try:
        menu() # chama menu a cada laço
        option = int(input(">>> ")) # chama input a cada laço
        # define ações para respostas no input
        if option == 1: 
            generate_answers() # gera dados aleatórios
            webbrowser.open('candidatos.txt') # abre arquivo candidatos.txt
        
        elif option == 2:
            webbrowser.open('gabarito.txt') # abre arquivo gabarito.txt
            
        elif option == 3:
            exam_validator() # faz verificação das notas
            generate_classification() # gera arquivo de classificação
            webbrowser.open('classificacao.txt') # abre arquivo de classificação
            
        elif option == 4:
            exit() # fecha programa
            
    except ValueError:     
     print("Digite apenas números")
    
        