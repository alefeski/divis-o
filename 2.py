.# url='abcdfghi'
# print(url.find('c'))

# url='cavalo locomotivo americano'
# print(url[0:27]) or print(url[0:])

# url='cavalo locomotivo americano'
# nova_url=url[0:6]
# print(nova_url)

# url='Python Fluente; Progamação clara, Concisa e Eficaz'
# nova_url=url[15:42]
# print(nova_url)

# fruta=['melão','jaca','uva','abacaxi','morango']
# fruta_vinho=('uva')
# print(fruta_vinho)

# url='Para ter sucesso, você deve eliminar dúvidas, aceitar desafios e rejeitar qualquer negatividade externa'
# newstrig=url[0:16]
# stringnews=url[27:95]
# print(newstrig)
# print(stringnews)

class Petcao:
    
    def __init__(self, nome, peso, raça):
        print('ficha do seu eu pet'.format(self))
        self.__nome = nome
        self.__peso = peso
        self.__raça = raça

def nome(self):
    print('o nome do seu pet é {}'.format(self.__nome))

def peso(self):
    print('o peso do seu pet é {}'.format(self.__peso))

def raça(self):
    print('esse é a raça do seu pet {}'.format(self.__raça))
