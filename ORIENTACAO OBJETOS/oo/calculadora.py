from abc import ABC, abstractmethod


class OperacaoNaoEncontrada(Exception):
    pass


# Para criar novas operacoes crie uma classe Herdando de Operacao, sobrescreva o metodo __call__ recebendo um paramento
# e retornando  resultado da operacao. Depois instancie uma calculadora e use o metodo
# adicionar operacao para adicionar a operacao

class Operacao(ABC): #classe abstrata que obriga a implementar todos os metodos
    '''Classe base para todas as operacoes. Metodo __call__ precisa ser sobrescrito'''
    @abstractmethod
    def __call__(self, operandos):
        '''Metodo deve executar operacao e retornar resultado'''

class Soma(Operacao):
    def __call__(self, operandos):
        return operandos[0] + operandos[1]


class Subtracao(Operacao):
    def __call__(self, operandos):
        return operandos[0] - operandos[1]

# Para alterar a obtencao de inputs, herde de Calculadora e subescreva o metodo extrair_inputs
class Calculadora:
    '''Classe responsavel por conter operacoes, obter inputs e efetuar calculos'''

    def __init__(self):
        self.operacoes = {}
        self.adicionar_operacao('+', Soma())
        self.adicionar_operacao('-', Subtracao())

    def adicionar_operacao(self, sinal, operacao):
        self.operacoes[sinal] = operacao


    def calcular(self):
        operandos, sinal = self.extrair_inputs()

        try:
            operacao = self.operacoes[sinal]
            resultado = operacao(operandos)

        except KeyError as e:
            raise OperacaoNaoEncontrada(f'Operacao nao encontrada para o sinal: {sinal}') from e

        return resultado

    def extrair_inputs(self):
        operandos = []
        operandos.append(float(input('Digite o primeiro operando ')))
        sinal = input('Digite o sinal da operacao ')
        operandos.append(float(input('Digite o segundo operando ')))
        return operandos, sinal

