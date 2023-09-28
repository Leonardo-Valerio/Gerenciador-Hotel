from functions import *
hoteis = {
    101: {'tipo': 'simples', 'status': 'livre'},
    102: {'tipo': 'duplo', 'status': 'ocupado'},
    201: {'tipo': 'suíte', 'status': 'livre'}
}
menu = ['ADICIONAR QUARTOS', 'LISTAR QUARTOS','RESERVAR QUARTO', 'BUSCAR QUARTO', 'REMOVER QUARTO', 'SAIR']
cabecalho('Seja Bem Vindo!!!')

while True:
    linha()
    exbirMenu(menu)
    linha()
    escolha = validarInt('digite uma opção: ')
    if escolha == 1:
        cabecalho(menu[0])
        cadastrarHotel(hoteis)
        print(hoteis)
    elif escolha == 2:
        cabecalho(menu[1])
        exibirDisponiveis(hoteis)
    elif escolha == 3:
        cabecalho(menu[2])
        print(reservarQuarto(hoteis))
    elif escolha == 4:
        cabecalho(menu[3])
        print(buscarQuarto(hoteis))
    elif escolha == 5:
        cabecalho(menu[4])
        print(excluirQuarto(hoteis))
    elif escolha == 6:
        cabecalho('SAINDO...')
        break

    else:
        print('digite um numero entre 1 e 5!')