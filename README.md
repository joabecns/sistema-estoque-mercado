# sistema-estoque-mercado
Atividade relativa ao Seminário (3ª avaliação) da Faculdade Estadual PIT na disciplina de Algoritmos e Lógica de Programação. 

Aluno: Joabe Carvalho Neco e Silva
Aluno: Pedro Rodrigues de Amorim Neto
Aluno: Luis Carlos Barbosa de Almeida

Projeto de controle de estoque usando a metodologia CRUD:
 Create (Criar);
 Read (Ler); 
 Update (Atualizar);
 Delete (Deletar)

Linguagem e ferramentas utilizadas: 
- Python
- JSON
- Git/GitHub

------estoque.py---------
 - Criamos a função mostrar 'mostrar_estoque', utilizada para receber os dados do estoque.padrao e, com eles, chamar no arquivo principal(main.py). 

 - As funções 'salvar_estoque', 'carregar_estoque' são usadas para salvar os dados do estoque disposto no 'estoque_padrao' e, caso não existir o arquivo.json no diretório, ele cria um arquivo com o estoque padrão. 

 - A função 'adicionar_item' serve para adicionar e atualizar, caso o item já existida. 

 - Por fim, a função 'remover_item' é empregada para remover items do estoque.json. 


------main.py------

O arquivo 'main.py' é responsável por chamar todas funções definidas no arquivo 'estoque.py'. Além disso, foi criado uma interface intuitiva, amigável e organizada, utilizando técnicas de estilização como '<20' para centralizar a direita e 'center:' para centralizar. 

------estoque.json------ 
O estoque.json é criado a partir da execução do programa, servindo para armazenar. de forma permanente, os dados recebido pelo programa. É usado, como um banco de dados, sendo útil para inserir, visualizar, atualizar e deletar dados de um programa CRUD, por exemplo. 

OBS: uso da inteligência artificial ao final do projeto para refinamento e aperfeiçoamento do código


Referência Bibliográfica:

PYTHON SOFTWARE FOUNDATION - Codificador e decodificador JSON.
Python 3 Documentation 2024 Disponível em:
<https://docs.python.org/pt-br/3/library/json.html#module-json>.

Manipulação de Arquivo JSON em Python
Disponível em: <https://www.youtube.com/watch?v=Cp3tWEXwrTc&t=90s>.

PYTHON SOFTWARE FOUNDATION. os.path — Manipulações comuns de nomes de caminho.
Python 3 Documentation, 2024. Disponível em:
<https://docs.python.org/pt-br/3/library/os.path.html#module-os.path>.

CRUD: o que é e como funciona?:
<https://blog.geekhunter.com.br/crud/>

Cores no Terminal
<https://www.youtube.com/watch?v=0hBIhkcA8O8>
