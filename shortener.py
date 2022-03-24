import pickle
from math import floor
from urllib.parse import urlparse


# ------------------------------------------------------------------------------------


class Encurtador:
    def __init__(self):
        self.dic = {}
        self.nome_arq = "urls.dat"
        self.__load_dic()
        self.indice = 1000 + len(self.dic)

    def __load_dic(self):
        try:
            arq = open(self.nome_arq, "rb").close()
            dic = self.dic
            return arq, dic
        except:
            print("Arquivo nao existe!")

    def __save_dic(self):
        with open(self.nome_arq, "wb") as arq:
            pickle.dump(self.dic, arq)

    def toBase(self, num, b=62):
        if b <= 0 or b > 62:
            return 0
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r = num % b
        res = base[r]
        q = floor(num / b)
        while q:
            r = q % b
            q = floor(q / b)
            res = base[int(r)] + res
        return res

    def to10(self, num, b=62):
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        limit = len(num)
        res = 0
        for i in range(limit):
            res = b * res + base.find(num[i])
        return res

    def encurtar(self, url):
        base = self.toBase(self.indice + len(self.dic))
        parts = urlparse(url)
        self.dic[self.indice] = parts.hostname+'/'+base, url
        self.__save_dic()
        self.indice += len(self.dic)

    def buscar(self, url_curta):
        indice = self.to10(url_curta)
        return self.dic[indice][1]

    def listar_urls(self):
        print(self.dic)


# ------------------------------------------------------------------------------------


e = Encurtador()
urls = []


#------------------------ MENU ------------------------ #


while True:
    print("""

    0 - Sair
    1 - Encurtar uma URL
    2 - Listar URLs
    3 - Codificar int para base62
    4 - Decodificar base62 para int

    """)

    option = str(input())

    if option == '0':
        break

    elif option == '1':
        url = input("Digite uma URL: ")
        if url in urls:
            print("URL invavlida")

        else:
            urls.append(url)
            e.encurtar(url)
    elif option == '2':
        e.listar_urls()

    elif option == '3':
        num = int(input('Digite um num para codificar: '))
        print(e.toBase(num))

    elif option == '4':
        str = input('Digite uma string para decodificar: ')
        print(e.to10(str))
