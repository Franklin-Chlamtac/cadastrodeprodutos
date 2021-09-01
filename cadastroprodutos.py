#recebi o pedido, guarde ele no sistema:


def leianumero():
    valido=False

    while not valido:
        v=str(input(f'\033[0;34mQual produto será cadastrado? ')).strip()
        if v.isalpha() or v == '':
            print(f'\033[1;31mERRO! PRODUTO "{v}" NÃO EXISTE, TENTE DIGITAR APENAS OS NUMEROS ACIMA!')
            print(f'\033[m')
        else:
            valido=True
            return int(v)

def leiaqntd():
    valido=False

    while not valido:
        v=str(input(f'\033[0;34mQual a quantidade do pedido?  ')).strip()
        if v.isalpha() or v == '':
            print(f'\033[1;31mERRO!  "{v}" NÃO É UMA QUANTIDADE VALIDA, TENTE DIGITAR APENAS OS NUMEROS!')
            print(f'\033[m')
        else:
            valido=True
            return int(v)

def pedido():
    print(f"\033[0;31m<<<CADASTRO DO PEDIDO>>>\033[m")
    print(f'\033[0;35mSelecione o produto: \033[m')
    print(f'\033[0;32mPara selecionar o produto A digite: [1]')
    print(f'\033[0;32mPara selecionar o produto B digite: [2]')
    print(f'\033[0;32mPara selecionar o produto C digite: [3]\033[m')
    estoque=['~', 'produtoA', 'produtoB', 'produtoC']

    while True:
        produto=leianumero()
        if produto > 3:
            print(f'\033[0;31mERRO!!! Produto não existe, tente digitar o numero de um produto valido.')
            print(f'\033[0;32mPara selecionar o produto A digite: [1]')
            print(f'\033[0;32mPara selecionar o produto B digite: [2]')
            print(f'\033[0;32mPara selecionar o produto C digite: [3]')
        else:
            break
    print(f'\033[1;33mO PRODUTO {estoque[produto]} SERÁ CADASTRADO AO PEDIDO! ')
    qntd=leiaqntd()
    print(f'\033[1;33m{qntd} {estoque[produto]} SERÃO ADCIONADOS AO PEDIDO!')


    print('...')



pedido()













