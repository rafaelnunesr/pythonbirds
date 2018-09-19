# O problema com o metodo procedural e que eu tenho que
# advinhar todas as provaveis utilizacoes da aplicacao.


class OperacaoNaoEncontrada(Exception):
    pass


def calcular():
    # Pegar inputs do usuario
    operandos = []
    operandos.append(float(input('Digite o primeiro operando ')))
    sinal = input('Digite o sinal da operacao ')
    operandos.append(float(input('Digite o segundo operando ')))
    return executar_calculo(sinal, *operandos)


def executar_calculo(sinal, *operandos):
    # Executar Operacao

    if sinal == '+':
        resultado = operandos[0] + operandos[1]
    elif sinal == '-':
        resultado = operandos[0] - operandos[1]

    else:
        raise OperacaoNaoEncontrada(f'Operacao nao encotrada no sinal: {sinal}')

    # Retornar Resultado

    raise resultado


def calcular_prefixa():
    # Pegar inputs do usuario
    operandos = []
    sinal = input('Digite o sinal da operacao ')
    operandos.append(float(input('Digite o primeiro operando ')))
    operandos.append(float(input('Digite o segundo operando ')))
    return executar_calculo(sinal, *operandos)