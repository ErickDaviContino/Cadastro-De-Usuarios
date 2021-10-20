import shutil
import os
import platform

def limparTela():
    sistemaOp = platform.system()
    if (sistemaOp == "Windows"):
        os.system("CLS")
    elif (sistemaOp == "Linux" or sistemaOp == "Darwin"):
        os.system("clear")

def pausarTela():
    input("\nPressione Enter para continuar. . .")

def verificaSeContemTexto(dado):
    return bool(str(dado).strip())

def verificaSeDivisivelPor2(num):
    return (num % 2 == 0)

def verificaSeForList(dado):
    return isinstance(dado, (list))

def stringParaList(stringParaConversao):
    comprimentoString = len(stringParaConversao)
    listFinal = [None for caracteresString in range(comprimentoString)]
    posicaoAtual = 0
    for indice in listFinal:
        listFinal[posicaoAtual] = stringParaConversao[posicaoAtual]
        posicaoAtual += 1
    return listFinal

def listParaString(listParaConversao):
    return "".join(listParaConversao)

def printFormatado(tamanhoLinha = shutil.get_terminal_size()[0], texto = "", alinhamento = "esquerda", repetir = 1, laterais = "", inverteLateral = True, separaLateral = False, preenchimento = " "):

    tamanhoTerminal = shutil.get_terminal_size()[0]
    if (tamanhoLinha > tamanhoTerminal):
        tamanhoLinha = tamanhoTerminal
    tamanhoTexto = tamanhoLinha
    linhaPar = verificaSeDivisivelPor2(tamanhoLinha)
    existeTexto = bool(texto)
    multiplasLinhas = verificaSeForList(texto)
    existeLaterais = verificaSeContemTexto(laterais)
    existePreenchimento = verificaSeContemTexto(preenchimento)
    textoFormatado = []
    textoQuebrado = []
    textoQuebradoLF = []

    if (repetir < 1): repetir = 1
    if (alinhamento != "esquerda" and alinhamento != "direita" and alinhamento != "centralizado"): alinhamento = "esquerda"

    if existePreenchimento:
        caracteresPreenchimento = stringParaList(str(preenchimento))
    else:
        caracteresPreenchimento = [" "]

    if existeLaterais:
        caracteresLaterais = stringParaList(laterais)
        qtdCaracteresLaterais = len(caracteresLaterais)
        tamanhoTexto -= qtdCaracteresLaterais * 2 + (2 if separaLateral else 0) 
        if (tamanhoTexto <= 0):
            caracteresAMais = 1
            caracteresLaterais.pop()
            if (tamanhoTexto < 0):
                caracteresAMais += (tamanhoTexto * -1) // 2 + 1
                del caracteresLaterais[qtdCaracteresLaterais - caracteresAMais + 1 : qtdCaracteresLaterais]
            tamanhoTexto = 2 if linhaPar else 1
        caracteresLaterais.reverse()

    if not multiplasLinhas:
        texto = [texto]
    for linha in texto:
        if "\n" in linha:
            textoQuebradoLF.extend(quebrarLinhaPorLF(linha))
        else:
            textoQuebradoLF.append(linha)
    for linha in textoQuebradoLF:
        textoQuebrado.extend(quebrarLinhaPorLimite(linha, tamanhoTexto))

    qtdLinhas = len(textoQuebrado)

    for linhaAtual in range(qtdLinhas):
        textoQuebrado[linhaAtual] = stringParaList(textoQuebrado[linhaAtual])
        qtdCaracteresTexto = len(textoQuebrado[linhaAtual])
        textoQuebrado[linhaAtual] = preencherLinha(qtdEspacosVazios = tamanhoTexto - qtdCaracteresTexto,
                                                   preenchimento = caracteresPreenchimento,
                                                   tipoPreenchimento = alinhamento,
                                                   linha = textoQuebrado[linhaAtual])
        if existeLaterais:
            if separaLateral:
                textoQuebrado[linhaAtual].insert(0," ")
                textoQuebrado[linhaAtual].append(" ")
            espacoLateral = tamanhoLinha - tamanhoTexto - (2 if separaLateral else 0)
            if inverteLateral:
                textoQuebrado[linhaAtual] = preencherLinha(qtdEspacosVazios = espacoLateral,
                                                           preenchimento = caracteresLaterais,
                                                           tipoPreenchimento = "centralizado",
                                                           linha = textoQuebrado[linhaAtual])
            else:
                textoQuebrado[linhaAtual] = preencherLinha(qtdEspacosVazios = espacoLateral // 2,
                                                           preenchimento = caracteresLaterais,
                                                           tipoPreenchimento = "direita",
                                                           linha = textoQuebrado[linhaAtual])
                caracteresLaterais.reverse()
                textoQuebrado[linhaAtual] = preencherLinha(qtdEspacosVazios = espacoLateral // 2 + (0 if linhaPar else 1),
                                                           preenchimento = caracteresLaterais,
                                                           tipoPreenchimento = "esquerda",
                                                           linha = textoQuebrado[linhaAtual])
                caracteresLaterais.reverse()

    for r in range(repetir):
        for linhaAtual in range(qtdLinhas):
            textoFormatado.append(textoQuebrado[linhaAtual])
        
    for linha in textoFormatado:
        linhaEmString = listParaString(linha)
        print(linhaEmString, end = ("" if tamanhoLinha == tamanhoTerminal else "\n"))
    
def preencherLinha(qtdEspacosVazios, preenchimento, tipoPreenchimento = "centralizado", linha = [""]):
    indice = 0
    caracterAtual = 1
    qtdCaracteresPreenchimento = len(preenchimento)
    while (caracterAtual <= qtdEspacosVazios):
        if (indice >= qtdCaracteresPreenchimento):
            indice = 0
        if (tipoPreenchimento == "direita" or tipoPreenchimento == "centralizado" and caracterAtual <= qtdEspacosVazios):
            linha.insert(0, preenchimento[indice])
            caracterAtual += 1
        if (tipoPreenchimento == "esquerda" or tipoPreenchimento == "centralizado" and caracterAtual <= qtdEspacosVazios):
            linha.append(preenchimento[indice])
            caracterAtual += 1
        indice += 1
    return linha

def quebrarLinhaPorLF(linha):
    linhasQuebradas = []
    qtdLF = linha.count("\n")
    for linhaAdicional in range(qtdLF):
        fimDaLinha = len(linha)
        indiceFinalAnterior = linha.find("\n")
        if (indiceFinalAnterior > -1):
            if (indiceFinalAnterior > 0):
                linhasQuebradas.append(linha[0 : indiceFinalAnterior])
            else:
                linhasQuebradas.append("")
            if (indiceFinalAnterior + 2 <= fimDaLinha):
                linha = linha[indiceFinalAnterior + 1 : fimDaLinha]
            else:
                linha = ""
    linhasQuebradas.append(linha)
    return linhasQuebradas

def quebrarLinhaPorLimite(linha, tamanhoLinha):
    linhasQuebradas = []
    caracteres = stringParaList(linha)
    totalCaracteres = len(caracteres)
    if (totalCaracteres > tamanhoLinha):
        totalDivisoes = totalCaracteres // tamanhoLinha + (1 if totalCaracteres % tamanhoLinha > 0 else 0)
    else:
        totalDivisoes = 1
    for linhaDividida in range(totalDivisoes):
        inicioDivisao = linhaDividida * tamanhoLinha
        finalDivisao = inicioDivisao + tamanhoLinha
        linhaAtual = linha[inicioDivisao : finalDivisao]
        linhasQuebradas.append(linhaAtual)
    return linhasQuebradas