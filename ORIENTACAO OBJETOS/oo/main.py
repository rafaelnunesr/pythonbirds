from oo.calculadora import Calculadora, Operacao


'''
Sem mexer no codigo original (calculadora) conseguimos extender a funcionalidade
'''
def produto(operandos):
        return operandos[0] * operandos[1]


class CalculadoraPrefixa(Calculadora): #calculadora prefixa implementada pelo usuario

    def extrair_inputs(self): # subescreve somente a parte que deseja alterar
        operandos = []        # todo o resto herda de Calculadora
        sinal = input('Digite o sinal da operacao ')
        operandos.append(float(input('Digite o primeiro operando ')))
        operandos.append(float(input('Digite o segundo operando ')))
        return operandos, sinal


if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora2 = CalculadoraPrefixa()
    calculadora.adicionar_operacao('*', produto) #usuario instanciando a operacao
    print(calculadora.calcular())