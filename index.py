from classes.Produto import Produto

def menu():
    print()
    print('1 - Listar Produtos')
    print('2 - Inserir Produtos')
    print('3 - Alterar Produtos')
    print('4 - Excluir Produtos')
    print('0 - Sair')
    print()
    
opcao = 1 

while opcao != 0:
    menu()
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            print('****************************************************')
            Produto.listarTodos()
            print('****************************************************')
        case 2:
            codigo = input('Digiteo codigo: ')
            nome = input('Informe o nome do produto: ')
            quantidade = input('Digite a quantidade: ')
            valor = input('Digite o valor do produto: ')
            
            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
            
        case 3:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja alterar?'))
            item = Produto.consultar(selecionado)
            
            quantidade = int(input('Qual a nova quantidade?'))
            valor = int(input('Qual o novo valor?'))
            produto = Produto(item["codigo"], item["nome"], quantidade, valor)
            produto.alterar(selecionado)
            
        case 4:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja alterar?'))
            
            Produto.excluir(selecionado)

print()
print("Programa encerrado! Até a proxima!")            


#produto = Produto('003', 'calça', 100, 100)
#produto.inserir()
#produto.listarTodos()

#categoria = Categoria('Vestuario')
#categoria.inserir()
#categoria.listarTodos()