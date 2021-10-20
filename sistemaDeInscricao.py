import sistemaUI as UI

def adicionaNovosUsuarios(list: []):
    menuAtual = "CADASTRAR USUÁRIOS"
    erro = None
    usuariosParaCadastrar = []
    while True:
        desenhaMenu(menuAtual, erro)
        umAluno = True
        try:
            qtdalunos = int(input("\nQuantidade: "))
            if(qtdalunos >= 0):
                cont = 0
                while(cont < qtdalunos):
                    umAluno = criaAluno(list, usuariosParaCadastrar)
                    if (umAluno == False):
                        break
                    usuariosParaCadastrar.append(umAluno)
                    cont += 1
                if (umAluno != False):
                    if (cont > 0):
                        list.extend(usuariosParaCadastrar)
                        desenhaMenu(menuAtual, etapa = 3, dadosParaExibir = usuariosParaCadastrar)
                    else:
                        desenhaMenu(menuAtual, etapa = 3, dadosParaExibir = "\nNenhum cadastro foi realizado.\n")
                if (qtdalunos == cont or umAluno == False):
                    return
            else:
                erro = "Digite um valor válido!"
        except:
            erro = "Favor, digite apenas números inteiros!"

def criaAluno(listaAlunos, listaParaCadastrar):

    menuAtual = "CADASTRAR USUÁRIOS"
    erro = None
    desenhaMenu(menuAtual, etapa = 2, dadosParaExibir = listaParaCadastrar)

    novoAluno = {}
    existeEmail = True
    escolha = input("\nDigite o nome do aluno: ")
    if (escolha != "CANCELAR"):
        novoAluno["nome"] = escolha
        while existeEmail:
            desenhaMenu(menuAtual, erro, 2, listaParaCadastrar)
            escolha = input("\nDigite o email do aluno: ")
            if (escolha != "CANCELAR"):
                novoAluno["email"] = escolha
                existeEmail = (len(listaAlunos) > 0)
                for usuario in listaAlunos:
                    if usuario["email"] == novoAluno["email"]:
                        existeEmail = True
                        erro = f"Email \"{usuario['email']}\" já existente, digite outro por favor."
                        break
                    else:
                        existeEmail = False
                for usuario in listaParaCadastrar:
                    if usuario["email"] == novoAluno["email"]:
                        existeEmail = True
                        erro = f"Email \"{usuario['email']}\" já está sendo cadastrado, digite outro por favor."
                        break
                    else:
                        existeEmail = False
                if not existeEmail:
                    return novoAluno
            else:
                break
    desenhaMenu(menuAtual, etapa = 3, dadosParaExibir = "\nCadastro cancelado.\n")
    return False

def listarUsuarios(list: []):
    if len(list) > 0:
        mensagemPrincipal = "\nLista de Inscritos por Ordem de Inscrição.\n"
        for usuario in list:
            mensagemPrincipal += "\nNome: " + usuario["nome"] + "  ===  " + "Email: " + usuario["email"]
        mensagemPrincipal += "\n"
    else:
        mensagemPrincipal = "\nNão há usuários cadastrados!\n"
    return mensagemPrincipal

def exibirUsuariosAlfabetica(list: []):
    if len(list) > 0:
        mensagemPrincipal = "\nLista de Inscritos por Ordem Alfabética.\n"
        nomesOrdenados = sorted(list, key=lambda k: k["nome"])
        for nome in nomesOrdenados:
            mensagemPrincipal += f'\nNome: {nome["nome"]}     E-mail: {nome["email"]}'
        mensagemPrincipal += "\n"
    else:
        mensagemPrincipal = "\nNão há usuários cadastrados!\n"
    return mensagemPrincipal

def buscaPorNome(list: []):
    menuAtual = "BUSCAR USUÁRIO"
    desenhaMenu(menuAtual, dadosParaExibir = "\nBusque por um usuário digitando seu nome para a consulta\n")
    try:
        nome = input("\nNome: ")
        for usuario in list:
            if usuario['nome'] == nome:
                mensagem = f"\nUsuário encontrado:\nNome: {nome} === Email: {usuario['email']}\n"
                break
            else:
                mensagem = "\nUsuário não encontrado!\n"
        desenhaMenu(menuAtual, etapa = 2, dadosParaExibir = mensagem)
    except:
        erro = "Ainda não há uma lista. Favor insira ao menos um usuário\n"
        desenhaMenu(menuAtual, erro, 2)

def excluiAlunoPorEmail(list: []):
    menuAtual = "DELETAR USUÁRIO"
    desenhaMenu(menuAtual)
    email = input("\nEmail para a exclusão: ")
    erro = None

    usuarioNaoEncontrado = True
    for usuario in list:
        if usuario['email'] == email:
            usuarioNaoEncontrado = False
            while True:
                desenhaMenu(menuAtual, erro, 2, usuario)
                try:
                    verificacao = input("\nEscolha: ").upper()[0]
                except:
                    verificacao = "erro"
                if (verificacao == "S"):
                    list.pop(list.index(usuario))
                    desenhaMenu(menuAtual, etapa = 3, dadosParaExibir = "\nUsuário deletado com sucesso!\n")
                    break
                elif (verificacao == "N"):
                    desenhaMenu(menuAtual, etapa = 3, dadosParaExibir = "\nO usuário não foi deletado.\n")
                    break
                else:
                    erro = "Digite apenas S ou N!"

    if usuarioNaoEncontrado:
        desenhaMenu(menuAtual, etapa = 3, dadosParaExibir = "\nUsuário não encontrado!\n")

def alterarNome(list: []):
    menuAtual = "ALTERAR USUÁRIO"
    desenhaMenu(menuAtual)
    email = input("\nDigite o email do usuário para alterar seu nome: ")
    usuarioNaoEncontrado = True
    erro = None
    for usuario in list:
        if usuario["email"] == email:
            usuarioNaoEncontrado = False
            while True:
                desenhaMenu(menuAtual, erro, 2, usuario)
                try:
                    verificacao = input("\nEscolha: ").upper()
                except:
                    verificacao = "erro"
                if (verificacao == "S"):
                    desenhaMenu(menuAtual, etapa = 3, dadosParaExibir = usuario)
                    novoNome = input("\nNome: ")
                    usuario["nome"] = novoNome
                    desenhaMenu(menuAtual, etapa = 4, dadosParaExibir = "\nNome alterado com sucesso!\n")
                    break
                elif (verificacao == "N"):
                    desenhaMenu(menuAtual, etapa = 4, dadosParaExibir = "\nO nome do usuário não foi alterado.\n")
                    break
                else:
                    erro = "Digite apenas S ou N!"
    if usuarioNaoEncontrado:
        desenhaMenu(menuAtual, etapa = 4, dadosParaExibir = "\nUsuário não encontrado!\n")

def menu():
    listaAlunos = []
    escolha = None
    erro = None
    while (escolha != "S"):
        menuAtual = "MENU PRINCIPAL"
        desenhaMenu(menuAtual, erro)
        erro = None
        try:
            op = int(input("\nEscolha uma opção de (1 a 7): "))
            if(op == 1):
                adicionaNovosUsuarios(listaAlunos)
            elif(op == 2):
                menuAtual = "EXIBIR USUÁRIOS"
                desenhaMenu(menuAtual, dadosParaExibir = listaAlunos)
            elif(op == 3):
                menuAtual = "EXIBIR USUÁRIOS (ORDEM ALFABÉTICA)"
                desenhaMenu(menuAtual, dadosParaExibir = listaAlunos)
            elif(op == 4):
                buscaPorNome(listaAlunos)
            elif(op == 5):
                excluiAlunoPorEmail(listaAlunos)
            elif(op == 6):
                alterarNome(listaAlunos)
            elif(op == 7):
                while (escolha != "S" and escolha != "N"): 
                    menuAtual = "SAIR DO PROGRAMA"
                    desenhaMenu(menuAtual, erro)
                    escolha = input("\nEscolha: ").upper()
                    if(escolha != "S" and escolha != "N"):
                        erro = "Escolha inválida!"
                    else:
                        erro = None
            else:
                erro = "Escolha inválida!"
        except:
            erro = "Por favor, digite apenas números inteiros!"
        if (escolha == "S"):
            break
        else: 
            escolha = None

def desenhaMenu(menuAtual, erro = None, etapa = 1, dadosParaExibir = []):

    UI.limparTela()

    UI.printFormatado(preenchimento = "|")
    UI.printFormatado(texto = f"\n---> {menuAtual} <---\n",
                      alinhamento = "centralizado",
                      laterais = "||",
                      separaLateral = True)
    UI.printFormatado(preenchimento = "|")

    if (erro != None):
        UI.printFormatado(texto = f"\n{erro}",
                          alinhamento = "centralizado",
                          laterais = "||",
                          separaLateral = True)

    if (menuAtual == "MENU PRINCIPAL"):
        mensagemPrincipal = ("\n1 - Cadastrar usuários\n" + 
                            "2 - Exibir usuários cadastrados\n" +
                            "3 - Exibir usuários cadastrados em ordem alfabetica\n" +
                            "4 - Verificar se um nome de um usuário está cadastrado\n" +
                            "5 - Remover um usuário cadastrado pelo seu email\n" +
                            "6 - Alterar o nome de um usuário\n" +
                            "7 - Sair do programa\n")

    elif (menuAtual == "CADASTRAR USUÁRIOS"):
        mensagemPrincipal = ""
        if (etapa == 1):
            mensagemPrincipal = "\nPara cadastrar usuários digite primeiramente a quantidade de usuários que deseja cadastrar\n"
        elif (etapa == 2):
            mensagemPrincipal = "\nAgora digite o nome e o email dos usuários\nCaso deseje cancelar a operação digite \"CANCELAR\"\n"
        if (etapa == 2 or etapa == 3):
            if (etapa == 2 or (etapa == 3 and not isinstance(dadosParaExibir, str))):
                qtdUsuarios = len(dadosParaExibir)
                if (qtdUsuarios > 0):
                    for indice in range(qtdUsuarios):
                        mensagemPrincipal += f"\nUsuário {indice+1}:\nNome: {dadosParaExibir[indice]['nome']} === Email: {dadosParaExibir[indice]['email']} \n"
                    if (etapa == 3):
                        usuarios = ("Usuários" if qtdUsuarios > 1 else "Usuário")
                        cadastrados = ("cadastrados" if qtdUsuarios > 1 else "cadastrado")
                        mensagemPrincipal += f"\n{usuarios} {cadastrados} com sucesso!\n"
            else:
                mensagemPrincipal = dadosParaExibir

    elif (menuAtual == "EXIBIR USUÁRIOS"):
        mensagemPrincipal = listarUsuarios(dadosParaExibir)

    elif(menuAtual == "EXIBIR USUÁRIOS (ORDEM ALFABÉTICA)"):
        mensagemPrincipal = exibirUsuariosAlfabetica(dadosParaExibir)

    elif(menuAtual == "BUSCAR USUÁRIO"):
        mensagemPrincipal = dadosParaExibir

    elif(menuAtual == "DELETAR USUÁRIO"):
        if (etapa == 1):
            mensagemPrincipal = "\nDelete um usuário digitando seu email\n"
        elif (etapa == 2):
            mensagemPrincipal = f"\nTem certeza que quer excluir o usuário:\nNome: {dadosParaExibir['nome']} === Email: {dadosParaExibir['email']}? [S/N]\n"
        else:
            mensagemPrincipal = dadosParaExibir

    elif(menuAtual == "ALTERAR USUÁRIO"):
        if (etapa == 1):
            mensagemPrincipal = "\nAltere o nome de um usuário digitando seu email\n"
        elif (etapa == 2):
            mensagemPrincipal = f"Gostaria de alterar o nome do usuário:\nNome: {dadosParaExibir['nome']} === Email: {dadosParaExibir['email']}? [S/N]\n"
        elif (etapa == 3):
            mensagemPrincipal = "\nDigite o novo nome desse usuário\n"
        else:
            mensagemPrincipal = dadosParaExibir
    
    elif (menuAtual == "SAIR DO PROGRAMA"):
        mensagemPrincipal = "\nDeseja mesmo sair do programa? [S/N]\n"


    UI.printFormatado(texto = mensagemPrincipal,
                      alinhamento = "centralizado" if (menuAtual == "EXIBIR USUÁRIOS" or menuAtual == "EXIBIR USUÁRIOS (ORDEM ALFABÉTICA)") else "esquerda",
                      laterais = "||",
                      separaLateral = True)  

    UI.printFormatado(preenchimento = "|")

    if((menuAtual == "CADASTRAR USUÁRIOS" and etapa == 3) or
        menuAtual == "EXIBIR USUÁRIOS" or 
        menuAtual == "EXIBIR USUÁRIOS (ORDEM ALFABÉTICA)" or 
       (menuAtual == "BUSCAR USUÁRIO" and etapa == 2) or 
       (menuAtual == "DELETAR USUÁRIO" and etapa == 3) or
       (menuAtual == "ALTERAR USUÁRIO" and etapa == 4)):
        UI.pausarTela()

def main():
    print("\nAntes de usar o programa, experimente aumentar o tamanho do terminal para melhor visualizar a interface")
    UI.pausarTela()
    menu()
    UI.limparTela()            
    print("Obrigado por utilizar o programa!")
    UI.pausarTela()


if __name__ == "__main__":
    main()
