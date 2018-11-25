# conding: utf-8

class Calculadora:
    n1= int(input("Digite o primeiro numero: "))
    n2 = int(input("digite o segundo numero: "))

    def retornaNumeros(n1, n2):
        print("Primeiro numero: {}".format(n1))
        print("Segundo numero: {}".format(n2))
    
    def soma(n1, n2):
        return n1 + n2

    retornaNumeros(n1,n2)
    print("A soma e: {}".format(str(soma(n1, n2))))
