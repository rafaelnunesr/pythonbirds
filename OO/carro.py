'''Voce deve criar uma classe carro que vai possuir dois atributos
compostos por outras duas classes:

1) Motor
    tera a responsabilidade de controlar a velocidade.
    ele oferece os seguintes atributos:
        1) atributo de dado velocidade
        2) metodo acerelar, que devera incrementar a velocidade de uma unidade
        3) Metodo frear que devera drementar a velocidade em duas unidades
2) Direcao
    tera a responsabilidade de controlar a direcao.
    ela oferece os seguintes atributos:
        1)valor de direcao com valores possiveis: norte, sul, leste, oeste
        2) metodo girar_a_direita
        3) metodo girar_a_esquerda

        N
      O   L
        S

Exemplo:
>>>#testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>>motor.acerelar()
>>>motor.velocidade
1
>>>motor.acerelar()
>>>motor.velocidade
2
>>>motor.acerelar()
>>>motor.velocidade
3
>>>motor.frear()
>>>motor.velocidade
1
>>>motor.frear()
>>>motor.velocidade
0

>>>#Testando direcao
>>>direcao = Direcao()
>>>direcao.valor
'Norte'
>>>direcao_girar_a_direita()
>>>direcao.valor
'Leste'
>>>direcao_girar_a_direita()
>>>direcao.valor
'Sul'
>>>direcao_girar_a_direita()
>>>direcao.valor
'Oeste'
>>>direcao_girar_a_direita()
>>>direcao.valor
'Norte'
>>>direcao_girar_a_esquerda()
>>>direcao.valor
'Oeste'
>>>direcao_girar_a_esquerda()
>>>direcao.valor
'Sul'
>>>direcao_girar_a_esquerda()
>>>direcao.valor
'Leste'
>>>direcao_girar_a_esquerda()
>>>direcao.valor
'Norte'

>>>carro = Carro(direcao, motor)
>>>carro.calcular_velocidade()
0 #informacao pegada do motor
>>>carro.acerelar()
>>>carro.calcular_velocidade()
1 #informacao pegada do motor
>>>carro.acerelar()
>>>carro.calcular_velocidade()
2 #informacao pegada do motor
>>>carro.freiar()
>>>carro.calcular_velocidade()
0 #informacao pegada do motor
>>>carro.calcular_direcao()
'Norte' #informacao pegada da direcao
>>>carro.girar_a_direita()
>>>carro.calcular_direcao()
'Leste' #informacao pegada da direcao
>>>carro.girar_a_esquerda()
>>>carro.calcular_direcao()
'Norte' #informacao pegada da direcao
>>>carro.girar_a_esquerda()
>>>carro.calcular_direcao()
'Oeste' #informacao pegada da direcao


'''

class Carro:
    @classmethod
    def __init__(clss, direcao='direcao', motor='motor'):
        Carro = Motor(), Direcao()


class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acerelar(self):
         self.velocidade += 1

    def freiar(self):
        if (self.velocidade - 2) < 0:
            self.velocidade = 0
        else:
            self.velocidade -= 2
    @property
    def calcular_velocidade(self):
        return self.velocidade


class Direcao:

    def __init__(self, pos_atual='Norte'):
        self.pos_atual = pos_atual

    def girar_a_direita(self):
        if self.pos_atual == 'Norte':
            self.pos_atual = 'Leste'
        elif self.pos_atual == 'Leste':
            self.pos_atual = 'Sul'
        elif self.pos_atual == 'Sul':
            self.pos_atual = 'Oeste'
        else:
            self.pos_atual = 'Norte'

    def girar_a_esquerda(self):
        if self.pos_atual == 'Norte':
            self.pos_atual = 'Oeste'
        elif self.pos_atual == 'Oeste':
            self.pos_atual = 'Sul'
        elif self.pos_atual == 'Sul':
            self.pos_atual = 'Leste'
        else:
            self.pos_atual = 'Norte'

    @property
    def valor(self):
        return self.pos_atual




