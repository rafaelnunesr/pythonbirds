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