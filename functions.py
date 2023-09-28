def linha():
    print('-'*50)

def cabecalho(msg):
    linha()
    print(msg.center(50))
    linha()

def exbirMenu(lst):
    for i in range(len(lst)):
        print(f'{i+1} - {lst[i]}')

def validarInt(str):
    while True:
        n = input(str)
        if n.isalnum():
            return int(n)
        print('erro, digite um numero')

def validarLivreOuOcupado(str):
    while True:
        txt = input(str).lower().strip()
        if txt == 'livre' or txt == 'ocupado':
            return txt
        print('erro, digite livre ou ocupado')
def cadastrarHotel(hotel):
    quantidadeDehoteis = validarInt('quantos quartos você deseja adicionar? ')
    for i in range(quantidadeDehoteis):
        numeroHotel = validarInt('digite o numero do id do quarto: ')
        tipo = input('qual o tipo do quarto? ')
        status = validarLivreOuOcupado('qual o status do hotel? (livre/ocupado)')

        hotel[numeroHotel] = {'tipo': tipo, 'status': status}

    return hotel

def exibirDisponiveis(hotel):
    linha()
    for i in hotel.items():
        if i[1]['status'] == 'livre':
            print(f'Id de Quartos Livres: {i[0]} / Tipo de Quarto: {i[1]["tipo"]}')
    linha()
def reservarQuarto(hotel):
    while True:
        exibirDisponiveis(hotel)
        IdQuarto = validarInt('qual o id do quarto que deseja reservar? ')
        for i in hotel.items():
            if i[0] == IdQuarto and i[1]['status'] == 'livre':
                i[1]['status'] = 'ocupado'
                return 'reserva realizada com sucesso!!'
        print('quarto já reservado ou não encontrado!')

def buscarQuarto(hotel):
    exibirTodosQuartos(hotel)
    while True:
        IdQuarto = validarInt('qual o id do quarto que deseja ver? ')
        for i in hotel.items():
            if i[0] == IdQuarto:
                cabecalho(f'QUARTO {IdQuarto}')
                return f'Status: {i[1]["status"]} / Tipo de Quarto: {i[1]["tipo"]}'
        print('quarto não encontrado!')

def excluirQuarto(hotel):
    exibirTodosQuartos(hotel)
    IdQuarto = validarInt('qual o id do quarto que deseja ver? ')
    for i in hotel.items():
        if i[0] == IdQuarto:
            cabecalho(f'EXCLUINDO QUARTO {IdQuarto}')
            del hotel[IdQuarto]
            return 'quarto excluído com sucesso'
    print('quarto não encontrado!')

def exibirTodosQuartos(hotel):
    linha()
    for i in hotel.items():
        print(f'Id de Quartos: {i[0]}')
    linha()
