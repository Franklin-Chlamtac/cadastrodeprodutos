#recebi o pedido, guarde ele no sistema: !!!
#quero continuar cadastrando ou não?
from datetime import date
datahj=date.today()

def leianumero():
    valido=False

    while not valido:
        v=str(input(f'\033[0;34mQual produto será cadastrado?( 0 irá finalizar o pedido.) \033[m')).strip()
        if v.isalpha() or v == '':
            print(f'\033[1;31mERRO! PRODUTO "{v}" NÃO EXISTE, TENTE DIGITAR APENAS OS NUMEROS ACIMA!')
            print(f'\033[m')
        else:
            valido=True
            return int(v)

def leiaqntd():
    valido=False

    while not valido:
        q=str(input(f'\033[0;34mQual a quantidade do pedido?  ')).strip()
        if q.isalpha() or q == '':
            print(f'\033[1;31mERRO!  "{q}" NÃO É UMA QUANTIDADE VALIDA, TENTE DIGITAR APENAS OS NUMEROS!')
            print(f'\033[m')
        else:
            valido=True
            return int(q)

def pedido():
    pedidop = {}
    tabela = []
    print(f'\033[1;31m~' * 40)
    print('\033[1;31m', end='')
    print(f"{'<<<CADASTRO DO PEDIDO>>>':^40}")
    print(f'\033[1;31m~' * 40)
    while True:
        print(f'\033[1;35mSelecione o produto: \033[m')
        print(f'\033[0;32mPara finalizar o pedido digite 0: \033[1;32m[0]')
        print(f'\033[0;32mPara selecionar o produto A digite: \033[1;32m[1]')
        print(f'\033[0;32mPara selecionar o produto B digite: \033[1;32m[2]')
        print(f'\033[0;32mPara selecionar o produto C digite: \033[1;32m[3]\033[m')
        estoque=['~', 'produtoA', 'produtoB', 'produtoC']

        while True:
            produto=leianumero()
            if produto > 3:
                print(f'\033[1;31mERRO!!! Produto não existe, tente digitar o numero de um produto valido.')
                print(f'\033[0;32mPara finalizar o pedido digite 0: \033[1;32m[0]')
                print(f'\033[0;32mPara selecionar o produto A digite: \033[1;32m[1]')
                print(f'\033[0;32mPara selecionar o produto B digite: \033[1;32m[2]')
                print(f'\033[0;32mPara selecionar o produto C digite: \033[1;32m[3]\033[m')
            elif produto < 0:
                print(f'\033[1;31mERRO!!! Produto não existe, tente digitar o numero de um produto valido.')
                print(f'\033[0;32mPara finalizar o pedido digite 0: \033[1;32m[0]')
                print(f'\033[0;32mPara selecionar o produto A digite: \033[1;32m[1]')
                print(f'\033[0;32mPara selecionar o produto B digite: \033[1;32m[2]')
                print(f'\033[0;32mPara selecionar o produto C digite: \033[1;32m[3]\033[m')
            else:
                break
        if produto == 0:
            print(f'\033[1;33m~' * 40)
            print(f"{'<<<FINALIZANDO PEDIDO>>>':^40}")
            print(f'\033[1;33m~' * 40)
            print(f'\033[1;35mOs seguintes itens foram adcionados ao pedido: \033[m')

            for p, v in enumerate(tabela):
                print(f"\033[1;32m{v['quantidade']} unidades de: {v['produto']}")

            print(f'data do pedido: {datahj}')
            print(f'\033[1;34mDESEJA SALVAR ESSE PEDIDO NA TABELA?\033[m')
            print('...')


            break

        else:
            print(f'\033[1;33m O PRODUTO {estoque[produto]} SERÁ CADASTRADO AO PEDIDO! ')
            qntd = leiaqntd()
            print(f'\033[1;33m~'*40)
            print(f"{qntd} {estoque[produto]} SERÃO ADCIONADOS AO PEDIDO!")
            print(f'\033[1;33m~' * 40)
            print()
            print(f'\033[1;35mContinue adcionando itens ou finalize o pedido.')


            pedidop['produto'] = estoque[produto]
            pedidop['quantidade'] = qntd
            tabela.append(pedidop.copy())


















pedido()














