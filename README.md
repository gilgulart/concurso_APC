# concurso_APC
 
Trabalho da disciplina de Algoritmos da faculdade. O projeto simula a correção de um concurso com **100 candidatos**, gerando dados fictícios, comparando as respostas de cada candidato com um gabarito e produzindo a classificação final ordenada por nota.

## 📋 Funcionalidades
 
- Geração automática de um **gabarito** com as respostas corretas de 20 questões.
- Geração automática de **100 candidatos fictícios**, cada um com um ID, nome e respostas (com diferentes níveis de "habilidade" para simular notas variadas).
- **Validação das notas**: compara as respostas de cada candidato com o gabarito e calcula a pontuação.
- Geração do arquivo de **classificação final**, ordenado do candidato com maior nota para o de menor nota.
- Menu interativo no terminal para executar cada etapa do processo.

## 🗂️ Estrutura do projeto
 
```
concurso_APC/
├── main.py                      # Menu principal (ponto de entrada do programa)
├── generate_template.py         # Gera o gabarito (gabarito.txt)
├── generate_answers.py          # Gera os 100 candidatos fictícios (candidatos.txt)
├── exam_validator.py            # Valida as respostas e calcula as notas
├── generate_classification.py   # Ordena e gera a classificação final (classificacao.txt)
├── gabarito.txt                 # Respostas corretas, separadas por vírgula
├── candidatos.txt                # Dados dos candidatos: id, nome, respostas
└── classificacao.txt            # Resultado final: id, nome, nota (ordenado)
```

## ⚙️ Como funciona
 
1. **`generate_template.py`** cria o `gabarito.txt` com as respostas corretas das 20 questões (alternativas de A a E).
2. **`generate_answers.py`** lê o gabarito e gera `candidatos.txt` com 100 candidatos aleatórios. Cada candidato tem um nível de "habilidade" (30%, 50%, 70% ou 90%) que define a chance de acertar cada questão, simulando notas mais realistas.
3. **`exam_validator.py`** lê o gabarito e os candidatos, compara as respostas questão a questão e calcula a nota de cada um.
4. **`generate_classification.py`** ordena os candidatos pela nota (do maior para o menor) e gera o `classificacao.txt` com o resultado final.
5. **`main.py`** reúne tudo isso em um menu simples no terminal.

## ▶️ Como executar
 
Pré-requisito: ter o **Python 3** instalado.
 
```bash
git clone https://github.com/gilgulart/concurso_APC.git
cd concurso_APC
python main.py
```
 
Ao executar, o menu exibirá as opções:
 
```
1 - Exibir candidatos
2 - Exibir Gabarito
3 - Exibir Classificação
4 - Sair
```
 
- **Opção 1**: gera novos candidatos aleatórios e abre `candidatos.txt`.
- **Opção 2**: abre o `gabarito.txt` com as respostas corretas.
- **Opção 3**: valida as notas, gera a classificação e abre `classificacao.txt`.
- **Opção 4**: encerra o programa.
> Os arquivos `.txt` são abertos automaticamente pelo navegador padrão do sistema (via `webbrowser`).

## 🛠️ Tecnologias utilizadas
 
- Python 3
- Módulos da biblioteca padrão: `random` e `webbrowser`

## ✍️ Autor
 
Desenvolvido por [Gilberto Gulart](https://github.com/gilgulart) como trabalho da disciplina de Algoritmos.