from os import system
import time

# Parte do usuário
def cadastroUsu(): # Função para realizar o cadastro do usuário
    lista_cad = [] # Lista para ser agrupar variáveis que serão enviadas para o arquivo txt
    espaco = " : " # Variável para corrigir formatação no arquivo txt
    
    # Realizar o cadastro do usuário
    usuario = str(input("Digite o usuário: ")) # Input usuário
    with open("dadosUsu.txt", "r") as arquivo: # Parte que verifica se o usuário já exite ou não
            listaU = arquivo.readlines()
            correcaoU = 0
            for item in listaU:
                while usuario == "" or (" " in usuario) or usuario in item: # Parte de verificação de erros
                    print("Usuário Inválido ou já existente!")
                    usuario = str(input("Digite outro usuário: "))
                    correcaoU = 1
                else:
                    correcaoU = 0
            if correcaoU == 0:
                print("Usuário aceito")
                lista_cad.append(usuario) # Adicionar na lista que irá para o txt
                lista_cad.append(espaco) # Adicionar na lista que irá para o txt
    
    # Realizar o cadastro do email
    email = str(input("Digite o email: "))  # Input email
    with open("dadosUsu.txt", "r") as arquivo: # Parte que verifica se o email já exite ou não
            listaE = arquivo.readlines()
            correcaoE = 0
            for item in listaE:
                # Parte de verificação de erros
                while email.find('@') == -1 or email.endswith('.com') == False or email in item: 
                    print("Email inválido ou já existente!")
                    email = str(input("Digite um outro email: "))
                else:
                    correcaoE == 0
            if correcaoE == 0:
                print("Email válido")
                lista_cad.append(email) # Adicionar na lista que irá para o txt
                lista_cad.append(espaco) # Adicionar na lista que irá para o txt

    # Realizar o cadastro da senha
    senha = str(input("Digite a senha: "))  # Input senha
    while senha.isdigit() == False: # Parte de verificação de erros
        print("Senha Inválida!")
        senha = str(input("Digite outra senha: "))
    else:
        print("Senha válida!")
        lista_cad.append(senha) # Adicionar na lista que irá para o txt
        # Parte que o que foi digitado é enviado para o arquivo txt
        with open("dadosUsu.txt", "r") as arquivo:
            listaA = arquivo.readlines()
            tamanho = len(listaA)
        with open('dadosUsu.txt', 'a') as arquivo:
            for valor in lista_cad:
                arquivo.write(str(valor))
            arquivo.write(str("\n"))
            arquivo.seek(tamanho)

def dadospessoaisUsu(): # Função para cadastrar os dados pessoais
    menuDadosUsu = ""
    while menuDadosUsu != 3:
        print("Consulta de dados pessoais") # Print das informações iniciais
        print("Opções  Funções\n", "[1]   Cadastrar dados\n", "[2]   Mostrar dados\n", "[3]   Sair")
        try:
            menuDadosUsu = int(input("Digite a opção que desejar: "))
        except ValueError:
            pass
        if menuDadosUsu == 1:
            time.sleep(0.5)
            system("cls")
            with open("dadosPessoaisUsu.txt", "r") as arquivo:
                listaVerificar = arquivo.readlines()
                for x in listaVerificar:
                    if usuarioEmail not in x:
                        cadastrar = 1
                    else:
                        cadastrar = 0
                if cadastrar == 1:
                    print("Será realizado o cadastro completo")

                    listaGeral = [] # Lista para ser agrupar variáveis que serão enviadas para o arquivo txt
                    espaco = " : " # Variável para corrigir formatação no arquivo txt
    
                    nomeCompleto = str(input("Digite o nome completo: ")) #Input nome
                    while nomeCompleto.isdigit(): # Parte de verificação de erros
                        print("Nome Inválido!")
                        nomeCompleto = str(input("Digite outro nome: "))
                    else:
                        print("Nome aceito")
                        listaGeral.append(nomeCompleto) # Adicionar na lista que irá para o txt
                        listaGeral.append(espaco) # Adicionar na lista que irá para o txt
            
                    idade = str(input("Digite sua idade: "))
                    # Parte de verificação de erros
                    while idade.isdigit() == False or (int(idade) > 130 and int(idade) < 0) or " " in idade or idade == "":
                        print("Idade inválida")
                        idade = str(input("Digite uma idade válida: "))
                    else:
                        print("Idade Válida")
                        listaGeral.append(idade) # Adicionar na lista que irá para o txt
                        listaGeral.append(" anos") # Adicionar na lista que irá para o txt
                        listaGeral.append(espaco) # Adicionar na lista que irá para o txt

                    email = ""
                    with open("dadosUsu.txt", "r") as arquivoEmail:
                        listar = arquivoEmail.readlines()
                    for linha in listar:
                        if usuarioEmail in linha:
                            acharEmail = linha.split()
                            email = acharEmail[2]
                            listaGeral.append(email) # Adicionar na lista que irá para o txt
                            listaGeral.append(espaco) # Adicionar na lista que irá para o txt
                    
                    celular = input("Digite seu telefone: ")
                    # Parte de verificação de erros
                    while len(celular) != 9 or celular.isnumeric() == False or celular[0] != "9":
                        print("Telefone inválido")
                        celular = input("Digite um telefone válido: ")
                    else:
                        print("Telefone aceito")
                        listaGeral.append(celular) # Adicionar na lista que irá para o txt

                    with open("dadosPessoaisUsu.txt", "r") as arquivo:
                        listaB = arquivo.readlines()
                        tamanho = len(listaB)
                    with open('dadosPessoaisUsu.txt', 'a') as arquivo:
                        for valor in listaGeral:
                            arquivo.write(str(valor))
                        arquivo.write(str("\n"))
                        arquivo.seek(tamanho)
                        
                    time.sleep(0.5)
                    system("cls")
                    break
                else:
                    print("Usuário já cadastrado!")
                    time.sleep(1)
                    system("cls")
                        

        elif menuDadosUsu == 2:
            with open("dadosPessoaisUsu.txt", "r") as arquivo:
                listaVerificar = arquivo.readlines()
                correcaoVerificar = 0
                for y in listaVerificar:
                    if usuarioEmail in y:
                        print("Cadastro encontrado")
                        print(y)
                        correcaoVerificar = 1
                        time.sleep(2)
                        system("cls")
                if correcaoVerificar == 0:
                    print("Cadastro não encontrado")
                    time.sleep(1)
                    system("cls")

        elif menuDadosUsu == 3:
            time.sleep(1)
            system("cls")
            pass

        else:
            print("Valor inválido")

def consultarEstatisticas(): # Função para consultar estatísticas
    print("Aqui vão algumas estatísticas sobre a produção de resíduos:")
    print('''
    - Consultar dados estatísticos sobre a produção de lixo no país: as estatísticas apresentadas ao usuário nessa função também servem como alerta e como impulso para tomar medidas emergenciais. Segundo pesquisas, o Brasil é o 4º país que mais produz lixo no mundo, segundo o Fundo Mundial para a Natureza (WWF), ficando atrás apenas dos Estados Unidos (1º lugar), da China (2º) e da Índia (3º). Durante a pandemia, a produção de resíduo domiciliar cresceu cerca de 10% e deve chegar em média 25% ou mais, segundo a Abrelpe.
    - Consultar o cálculo da produção de lixo: segunda a pesquisa de Caracterização dos Resíduos Sólidos Urbanos, realizada pela Comcap/CEFET/UFSC, em 2002, cada pessoa em Florianópolis produzia 0,77 Kg de resíduos sólidos por dia. De acordo com dados mais recentes do Panorama dos Resíduos Sólidos no Brasil 2020, em 2019 tivemos a geração de 79,1 milhões de toneladas de resíduos, isso corresponde a mais de 1 Kg de resíduos por dia vindo de cada pessoa no Brasil, esses dados foram coletados e publicados pela Associação Brasileira das Empresas de Limpeza Pública e Resíduos Especiais (Abrelpe). Isso posto, adotamos no nosso sistema o número de 1 Kg por dia, por pessoa. Ao multiplicarmos esse número pela quantidade de dias do ano chegamos a 365 Kg de resíduos por pessoa, por ano. Com esse dado e com o dado da idade do usuário conseguimos encontrar a média do número, em Kg, de resíduos produzimos pelo usuário até hoje em sua vida. Por exemplo, um usuário com 42 anos de idade, levando em conta que esse usuário segue o padrão de vida adotado pela maioria das pessoas na sociedade atual, produziu até hoje em sua vida 15.330 Kg de resíduos.
    ''')
    try:
        sairMenu = int(input("Digite [1] para sair das estatísticas: "))
    except ValueError:
        pass
    while sairMenu != 1:
        print("Valor inválido!!!")
        try:
            sairMenu = int(input("Digite um número válido: "))
        except ValueError:
            pass
    else:
        print("Espero que tenha adquirido conhecimento com nossas estatísiticas!!!")
        time.sleep(1.5)
        system("cls")

def consultarEmpresas(): # Função para consultar empresas
    menuConsulta = ""
    while menuConsulta != 3:
        print("Aqui você pode se tornar cliente de uma empresa ou ver as empresas que já é cliente")
        print("Opções  Funções\n", "[1]   Se tornar cliente\n", "[2]   Consultar suas empresas\n", "[3]   Sair")
        try:
            menuConsulta = int(input("Digite a opção que desejar: "))
        except ValueError:
            pass
        if menuConsulta == 1:
            time.sleep(1.5)
            system("cls")
            with open("listaempresas.txt", "r") as arquivo:
                visorEmpresas = arquivo.read()
                print(visorEmpresas)
            with open("listaempresas.txt", "r") as arquivo1:
                listarEmpresas = arquivo1.readlines()
                empresaSelect = str(input("Digite o email da empresa que deseja ser cliente: "))
                for item in listarEmpresas:
                    if empresaSelect in item:
                        correcao = 1
                        listaConsulta = []
                        espaco = " : "
                        email = ""
                        with open("dadosUsu.txt", "r") as arquivoEmail:
                            listar = arquivoEmail.readlines()
                        for linha in listar:
                            if usuarioEmail in linha:
                                acharEmail = linha.split()
                                usuario = acharEmail[0]
                                email = acharEmail[2]
                                listaConsulta.append(usuario) # Adicionar na lista que irá para o txt
                                listaConsulta.append(espaco) # Adicionar na lista que irá para o txt
                                listaConsulta.append(email)
                                listaConsulta.append(espaco)
                                listaConsulta.append(empresaSelect)

                        with open("listaclientes.txt", "r") as arquivo2:
                            listaC = arquivo2.readlines()
                            tamanho = len(listaC)
                        with open("listaclientes.txt", "a") as arquivo3:
                            for valor in listaConsulta:
                                arquivo3.write(str(valor))
                            arquivo3.write(str("\n"))
                            arquivo3.seek(tamanho)
                        print("Agora você é cliente dessa empresa!!!")
                        time.sleep(2)
                        system("cls")
                        pass
                    else:
                        pass
                if correcao != 1:
                    print("Empresa não encontrada!!!")
                    time.sleep(1.5)
                    system("cls")

        elif menuConsulta == 2:
            time.sleep(1.5)
            system("cls")
            with open("listaclientes.txt", "r") as arquivo4:
                listarConsulta = arquivo4.readlines()
                with open("dadosUsu.txt", "r") as arquivoEmail:
                    listar = arquivoEmail.readlines()
                for linha in listar:
                    if usuarioEmail in linha:
                        acharEmail = linha.split()
                        usuario = acharEmail[0]
                print("Você é cadastrado nessas empresas:")
                for line in listarConsulta:
                    if usuario in line:
                        print(line)
                time.sleep(5)
                system("cls")

        elif menuConsulta == 3:
            time.sleep(1)
            system("cls")
            pass

        else:
            print("Valor inválido!!!")

def consultarDicas(): # Função para consultar dicas
    print("As dicas para reduzir cada vez mais o consumo de lixo são:")
    print('''
    - Reciclar
    - Usar uma garrafinha de alumínio ao invés de plástico, quando você sente sede é a melhor opção.
    - Usar as famosas ecobags (sacolas ecológicas), eliminam o uso das sacolas plásticas, que por sua vez, 
    demoram cerca de 400 a 1000 anos para se decompor na natureza e evitam a poluição em mares e rios e a 
    morte de animais aquáticos.
    - Filtros de barro não utilizam componentes plásticos, que por sua vez, são utilizados em filtros de plástico e o descarte incorreto, gera consequências ambientais.
    - Aproveitar o lixo orgânico para fazer compostagem.
    - Optar por pilhas recarregáveis e fazer o descarte correto das mesmas
    ''')
    try:
        sairMenu = int(input("Digite [1] para sair das dicas: "))
    except ValueError:
        pass
    while sairMenu != 1:
        print("Valor inválido!!!")
        try:
            sairMenu = int(input("Digite um número válido: "))
        except ValueError:
            pass
    else:
        print("Espero que tenha gostado das dicas!!!")
        time.sleep(1.5)
        system("cls")

def consultarCalculo(): # Função para consultar cálculo
    menuCalculo = ""
    while menuCalculo != 3:
        print("Opções  Funções\n", "[1]   Realizar seu cálculo\n", "[2]   Consultar seu cálculo\n", "[3]   Sair")
        try:
            menuCalculo = int(input("Digite a opção que desejar: "))
        except ValueError:
            pass
        if menuCalculo == 1: #Realização do Cálculo
            time.sleep(1.5)
            system("cls")
            with open("producaolixo.txt", "r") as arquivo:
                listarCalc = arquivo.readlines()
                for item in listarCalc:
                    if usuarioEmail in item:
                        corrigir = 1
                    else: 
                        corrigir = 0
                if corrigir == 1:
                    print("Estatísticas já cadastradas")
                    divisao = item.split()
                    numero = divisao[2]
                    letras = divisao[3]
                    print("Sua produção de lixo durante a vida é de: ", numero, letras)
                    print("Opções  Funções\n", "  [1]   Cadastrar Nova\n", "  [2]   Sair")
                    pergunta = int(input("Digite a opção que desejar: "))
                    while pergunta != 1 and pergunta != 2:
                        pergunta = int(input("Digite uma opção válida: "))
                    else:
                        if pergunta == 1:
                            time.sleep(3.5)
                            system("cls")
                            correcao_rem = 0
                            for linha in listarCalc:
                                if usuarioEmail in linha:
                                    indice = listarCalc.index(linha)
                                    del(listarCalc[indice])
                                    with open('producaolixo.txt', 'w') as arquivo1:
                                        for valor1 in listarCalc:
                                            arquivo1.write(str(valor1))
                                    correcao_rem = 1
                            if correcao_rem == 0:
                                print("Valor não foi encontrado!")
                                time.sleep(3.5)
                                system('cls')
                            else:
                                diasDoAno = 365
                                idade = int(input("Por favor, confirme sua idade: "))
                                calculo = diasDoAno * idade
                                print("Sua produção de lixo durante a vida é de: ", calculo, "Kg")
                                espaco = " : "
                                quilograma = " Kg"
                                listaCalculo = []
                                listaCalculo.append(usuarioEmail)
                                listaCalculo.append(espaco)
                                listaCalculo.append(calculo)
                                listaCalculo.append(quilograma)
                                with open("producaolixo.txt", "r") as arquivo:
                                    listaX = arquivo.readlines()
                                    tamanho = len(listaX)
                                with open("producaolixo.txt", "a") as arquivo1:
                                    for valor in listaCalculo:
                                        arquivo1.write(str(valor))
                                    arquivo1.write(str("\n"))
                                    arquivo1.seek(tamanho)

                                time.sleep(4)
                                system("cls")
                        elif pergunta == 2:
                            time.sleep(2)
                            system("cls")
                            pass
                else:
                    diasDoAno = 365
                    idade = int(input("Por favor, confirme sua idade: "))
                    calculo = diasDoAno * idade
                    print("Sua produção de lixo durante a vida é de: ", calculo, "Kg")
                    espaco = " : "
                    quilograma = " Kg"
                    listaCalculo = []
                    listaCalculo.append(usuarioEmail)
                    listaCalculo.append(espaco)
                    listaCalculo.append(calculo)
                    listaCalculo.append(quilograma)
                    with open("producaolixo.txt", "r") as arquivo:
                        listaX = arquivo.readlines()
                        tamanho = len(listaX)
                    with open("producaolixo.txt", "a") as arquivo1:
                        for valor in listaCalculo:
                            arquivo1.write(str(valor))
                        arquivo1.write(str("\n"))
                        arquivo1.seek(tamanho)

                    time.sleep(4)
                    system("cls")
        elif menuCalculo == 2:
            time.sleep(1.5)
            system("cls")
            with open("producaolixo.txt", "r") as arquivo1:
                listarConsCalc = arquivo1.readlines()
                for x in listarConsCalc:
                    if usuarioEmail in x:
                        ajuste = 1
                    else: ajuste = 0
                if ajuste == 1:
                    print("Estatísticas já cadastradas")
                    dividir = x.split()
                    numero2 = dividir[2]
                    letras2 = dividir[3]
                    print("Sua produção de lixo durante a vida é de: ", numero2, letras2)
                    time.sleep(4)
                    system("cls")
                else:
                    print("Estatísticas ainda não cadastradas!!!")
                    time.sleep(3.5)
                    system("cls")
        elif menuCalculo == 3:
            time.sleep(1)
            system("cls")
            pass
        else:
            print("Digite um valor válido!!!")
            time.sleep(1)
            system("cls")

# Parte da empresa
def cadastroEmpre(): # Função para realizar o cadastro da empresa
    lista_cadEmp = [] # Lista para ser agrupar variáveis que serão enviadas para o arquivo txt
    espaco = " : " # Variável para corrigir formatação no arquivo txt
    
    # Realizar o cadastro da empresa
    usuario = str(input("Digite o nome da empresa: ")) #Input empresa
    with open("dadosEmp.txt", "r") as arquivoEmp:
            listaUEmp = arquivoEmp.readlines()
            correcaoUEmp = 0
            for item in listaUEmp:
                while usuario == "" or (" " in usuario) or usuario in item: 
                    print("Usuário Inválido ou já existente!")
                    usuario = str(input("Digite outro usuário: "))
                    correcaoUEmp = 1
                else:
                    correcaoUEmp = 0
            if correcaoUEmp == 0:
                print("Usuário aceito")
                lista_cadEmp.append(usuario) # Adicionar na lista que irá para o txt
                lista_cadEmp.append(espaco) # Adicionar na lista que irá para o txt
    
    # Realizar o cadastro do email
    email = str(input("Digite o email: "))  # Input email
    with open("dadosEmp.txt", "r") as arquivoEmp:
            listaEEmp = arquivoEmp.readlines()
            correcaoEEmp = 0
            for item in listaEEmp:
                while email.find('@') == -1 or email.endswith('.com') == False or email in item:
                    print("Email inválido ou já existente!")
                    email = str(input("Digite um outro email: "))
                else:
                    correcaoEEmp == 0
            if correcaoEEmp == 0:
                print("Email válido")
                lista_cadEmp.append(email) # Adicionar na lista que irá para o txt
                lista_cadEmp.append(espaco) # Adicionar na lista que irá para o txt

    # Realizar o cadastro da senha
    senha = str(input("Digite a senha: "))  # Input senha
    while senha.isalpha == False:
        print("Senha Inválida!")
        senha = str(input("Digite outra senha: "))
    else:
        print("Senha válida!")
        lista_cadEmp.append(senha) # Adicionar na lista que irá para o txt
        # Parte que o que foi digitado é enviado para o arquivo txt
        with open("dadosEmp.txt", "r") as arquivoEmp:
            listaA = arquivoEmp.readlines()
            tamanho = len(listaA)
        with open('dadosEmp.txt', 'a') as arquivoEmp:
            for valor in lista_cadEmp:
                arquivoEmp.write(str(valor))
            arquivoEmp.write(str("\n"))
            arquivoEmp.seek(tamanho)

def dadospessoaisEmp(): # Função para cadastrar dados da empresa
    menuDadosEmp = ""
    while menuDadosEmp != 3:
        print("Consulta de dados da empresa") # Print das informações iniciais
        print("Opções  Funções\n", "[1]   Cadastrar dados\n", "[2]   Mostrar dados\n", "[3]   Sair")
        try:
            menuDadosEmp = int(input("Digite a opção que desejar: "))
        except ValueError:
            pass
        if menuDadosEmp == 1:
            time.sleep(0.5)
            system("cls")
            with open("dadosPessoaisEmp.txt", "r") as arquivo:
                listaVerificar = arquivo.readlines()
                for x in listaVerificar:
                    if empresaEmail not in x:
                        cadastrar = 1
                    else:
                        cadastrar = 0
                if cadastrar == 1:
                    print("Será realizado o cadastro completo")

                    listaGeral = [] # Lista para ser agrupar variáveis que serão enviadas para o arquivo txt
                    espaco = " : " # Variável para corrigir formatação no arquivo txt
                    listaNomes = []

                    nomeCompleto = str(input("Digite o nome da empresa: ")) #Input nome
                    while nomeCompleto.isdigit() or nomeCompleto.endswith(" "): 
                        print("Nome Inválido!")
                        nomeCompleto = str(input("Digite um nome válido: "))
                    else:
                        print("Nome aceito")
                        listaGeral.append(nomeCompleto)
                        listaGeral.append(espaco)
                        listaNomes.append(nomeCompleto)
                        listaNomes.append(espaco)

                    email = ""
                    with open("dadosEmp.txt", "r") as arquivoEmail:
                        listar = arquivoEmail.readlines()
                    for linha in listar:
                        if empresaEmail in linha:
                            acharEmail = linha.split()
                            email = acharEmail[2]
                            listaGeral.append(email)
                            listaGeral.append(espaco)
                            listaNomes.append(email)
                            listaNomes.append(espaco)
                    
                    celular = input("Digite seu telefone: ")
                    while len(celular) != 9 or celular.isnumeric() == False or celular[0] != "9":
                        print("Telefone inválido")
                        celular = input("Digite um telefone válido: ")
                    else:
                        print("Telefone aceito")
                        listaGeral.append(celular)
                        listaGeral.append(espaco)

                    listaRamos = [1, 2, 3, 4, 5, 6]
                    ramo = ""
                    while ramo not in listaRamos:
                        print("Opções  Tipos\n", "[1]   Coleta Seletiva\n", "[2]   Vendedor de Ecobags\n", 
                        "[3]   Compra de usados\n", "[4]   Catador de latinha\n", 
                        "[5]   Produtos ecológicos no geral\n", "[6]   Outro\n")
                        try:
                            ramo = int(input("Escolha a opção do ramo da empresa: "))
                        except ValueError:
                            pass
                        if ramo == 1:
                            ramo1 = "Coleta Seletiva"
                            listaGeral.append(ramo1)
                            listaNomes.append(ramo1)
                        elif ramo == 2:
                            ramo2 = "Vendedor de Ecobags"
                            listaGeral.append(ramo2)
                            listaNomes.append(ramo2)
                        elif ramo == 3:
                            ramo3 = "Compra de usados"
                            listaGeral.append(ramo3)
                            listaNomes.append(ramo3)
                        elif ramo == 4:
                            ramo4 = "Catador de latinha"
                            listaGeral.append(ramo4)
                            listaNomes.append(ramo4)
                        elif ramo == 5:
                            ramo5 = "Produtos ecológicos no geral"
                            listaGeral.append(ramo5)
                            listaNomes.append(ramo5)
                        elif ramo == 6:
                            ramo6 = str(input("Digite qual seu ramo: "))
                            listaGeral.append(ramo6)
                            listaNomes.append(ramo6)
                        else:
                            print("Valor inválido!!!")
                            time.sleep(1)
                            system('cls')

                    with open("dadosPessoaisEmp.txt", "r") as arquivo:
                        listaB = arquivo.readlines()
                        tamanho = len(listaB)
                    with open('dadosPessoaisEmp.txt', 'a') as arquivo:
                        for valor in listaGeral:
                            arquivo.write(str(valor))
                        arquivo.write(str("\n"))
                        arquivo.seek(tamanho)

                    with open("listaempresas.txt", "r") as arquivo1:
                        listaT = arquivo1.readlines()
                        tamanhoT = len(listaT)
                    with open('listaempresas.txt', 'a') as arquivo1:
                        for item in listaNomes:
                            arquivo1.write(str(item))
                        arquivo1.write(str("\n"))
                        arquivo1.seek(tamanhoT)
                        
                    time.sleep(0.5)
                    system("cls")
                else:
                    print("Empresa já cadastrada!")
                    time.sleep(1)
                    system("cls")


        elif menuDadosEmp == 2:
            with open("dadosPessoaisEmp.txt", "r") as arquivo:
                listaVerificar = arquivo.readlines()
                correcaoVerificar = 0
                for y in listaVerificar:
                    if empresaEmail in y:
                        print("Cadastro encontrado")
                        print(y)
                        correcaoVerificar = 1
                        time.sleep(2)
                        system("cls")
                if correcaoVerificar == 0:
                    print("Cadastro não encontrado")
                    time.sleep(1)
                    system("cls")

        elif menuDadosEmp == 3:
            time.sleep(0.5)
            system("cls")
            pass

        else:
            print("Valor inválido")
            time.sleep(1)
            system("cls")

def listaClientes(): # Função para ver lista de clientes cadastrados
    menuClientes = ""
    while menuClientes != 2:
        print("Opções  Funções\n", "[1]   Consultar clientes\n", "[2]   Sair")
        try:
            menuClientes = int(input("Digite a opção que desejar: "))
        except ValueError:
            pass
        if menuClientes == 1:
            email = ""
            with open("dadosEmp.txt", "r") as arquivoEmail:
                listar = arquivoEmail.readlines()
                for linha in listar:
                    if empresaEmail in linha:
                        acharEmail = linha.split()
                        email = acharEmail[2]
            with open("listaclientes.txt", "r") as arquivo:
                listarClientes = arquivo.readlines()
                for item in listarClientes:
                    localEmail = item.split()
                    verificarEmail = localEmail[4]
                    escritaUsuario = localEmail[0]
                    escritaPonto = localEmail[1]
                    escritaEmail = localEmail[2]
                    corrigir = 0
                    if email in verificarEmail:
                        print(escritaUsuario, escritaPonto, escritaEmail)
                        time.sleep(4)
                        system('cls')
                    else:
                        corrigir = 1
                if corrigir != 0:
                    print("Nenhum cliente encontrado!!!")
                    time.sleep(3)
                    system('cls')
        elif menuClientes == 2:
            time.sleep(1.5)
            system('cls')
            pass
        else:
            print("Valor inválido!!!")
            time.sleep(1)
            system('cls')

def retirarEmpresa(): # Função para retirar a empresa do sistema
    with open("dadosEmp.txt", "r") as arquivo:
        listar = arquivo.readlines()
    busca1 = empresaEmail
    correcao_rem = 0
    for linha in listar:
        if busca1 in linha:
            indice = listar.index(linha)
            del(listar[indice])
            with open('dadosEmp.txt', 'w') as arquivo1:
                for valor1 in listar:
                    arquivo1.write(str(valor1))
            correcao_rem = 1
    if correcao_rem == 0:
        print("Valor não foi encontrado!")
        time.sleep(3.5)
        system('cls')
    else:
        print("Cadastro removido com sucesso!")
        time.sleep(3.5)
        system('cls')
        pass

# Parte de Login
passaporteUsu = ""
usuarioEmail = ""
def loginUsu(): # Função para criar login
    with open("dadosUsu.txt", "r") as arquivoLogUsu:
        lista = arquivoLogUsu.readlines()
        print(lista) # APAGAR NA HORA DE ENVIAR O CÓDIGO
    usuarioL = ""
    senhaL = ""
    while senhaL.isdigit() == False: 
        usuarioL = str(input("Digite o usuário: "))
        senhaL = str(input("Digite a senha: "))
        correcao = 0
        for linha in lista:
            acharsenha = linha.split()
            usuario = acharsenha[0]
            senha = acharsenha[4]
            if usuarioL == usuario and senhaL == senha:
                print("Acesso Liberado")
                correcao = 1
        if correcao == 1:
            global passaporteUsu
            passaporteUsu = True
            global usuarioEmail
            usuarioEmail = usuarioL
        elif correcao == 0:
            print("Acesso negado")
        else:
            pass

passaporteEmp = ""
empresaEmail = ""
def loginEmp(): # Função para criar login
    with open("dadosEmp.txt", "r") as arquivoLogEmp:
        lista = arquivoLogEmp.readlines()
        print(lista)
    usuarioLEmp = str(input("Digite o usuário: "))
    senhaL = str(input("Digite a senha: "))
    correcao = 0
    for linha in lista:
        acharsenha = linha.split()
        usuario = acharsenha[0]
        senha = acharsenha[4]
        if usuarioLEmp == usuario and senhaL == senha:
            print("Acesso Liberado")
            correcao = 1
    if correcao == 1:
        global passaporteEmp
        passaporteEmp = True
        global empresaEmail
        empresaEmail = usuarioLEmp
    elif correcao == 0:
        print("Acesso negado")
    else:
        pass

# MENU

opcao = ""
while opcao != 3:
    time.sleep(1)
    system("cls")
    print("Opções  Funções\n", "  [1]   Cadastro\n", "  [2]   Login\n", "  [3]   Sair\n") # Opções menu principal
    try:
        opcao = int(input("Digite a opção que deseja no menu: "))
    except ValueError:
        pass
    if opcao == 1: # Cadastro
        time.sleep(0.5)
        system("cls")
        print("Opções Funções\n", "[1]   Usuário\n", "[2]   Empresa\n")
        opcaoCadastro = ""
        while opcaoCadastro != 1 and opcaoCadastro != 2:
            try:
                opcaoCadastro = int(input("Cadastrar Usuário ou Empresa: "))
            except ValueError:
                pass
            if opcaoCadastro == 1: # Cadastro usuário
                time.sleep(1)
                system("cls")
                cadastroUsu()
            elif opcaoCadastro == 2: # Cadastro empresas
                time.sleep(1)
                system("cls")
                cadastroEmpre()
            else:
                print("Opção Inválida!")
                time.sleep(0.5)
                system("cls")
    elif opcao == 2: # Login
        time.sleep(0.5)
        system("cls")
        opcaoLogin = ""
        while opcaoLogin != 1 and opcaoLogin != 2:
            print("Opções Funções\n", "[1]   Login Usuário\n", "[2]   Login Empresa\n")
            try:
                opcaoLogin = int(input("Login Usuário ou Empresa: "))
            except ValueError:
                pass
            if opcaoLogin == 1: # Parte do Login do Usuário
                time.sleep(1)
                system("cls")
                loginUsu()
                if passaporteUsu == True:
                    time.sleep(0.5)
                    system("cls")
                    print("Bem vindo ao nosso sistema!")
                    opcaoSistemaUsu = ""
                    while opcaoSistemaUsu != 6: # Menu opções usuário
                        print("Opções Funções\n", "[1]   Cadastrar e ver dados pessoais\n", "[2]   Consultar estatísticas\n", 
                        "[3]   Contatar empresas com ações sustentáveis\n", "[4]   Consultar dicas\n", 
                        "[5]   Consultar cálculo pessoal\n", "[6]   Sair")
                        try:
                            opcaoSistemaUsu = int(input("Digite a opção que desejar no menu: "))
                        except ValueError:
                            pass    
                        if opcaoSistemaUsu == 1:
                            time.sleep(0.5)
                            system("cls")
                            dadospessoaisUsu()
                        elif opcaoSistemaUsu == 2:
                            time.sleep(0.5)
                            system("cls")
                            consultarEstatisticas()
                        elif opcaoSistemaUsu == 3:
                            time.sleep(0.5)
                            system("cls")
                            consultarEmpresas()
                        elif opcaoSistemaUsu == 4:
                            time.sleep(0.5)
                            system("cls")
                            consultarDicas()
                        elif opcaoSistemaUsu == 5:
                            time.sleep(0.5)
                            system("cls")
                            consultarCalculo()
                        elif opcaoSistemaUsu == 6:
                            pass
                        else:
                            print("Opção inválida")
                            time.sleep(0.5)
                            system("cls")
                else:
                    pass

            elif opcaoLogin == 2: # Parte do login da empresa
                time.sleep(1)
                system("cls")
                loginEmp()
                if passaporteEmp == True:
                    time.sleep(0.5)
                    system("cls")
                    print("Bem vindo ao nosso sistema!")
                    opcaoSistemaEmp = ""
                    while opcaoSistemaEmp != 4: # Menu opções usuário
                        print("Opções Funções\n", "[1]   Cadastrar e ver dados da empresa\n", "[2]   Listar Clientes\n", 
                        "[3]   Remover empresa\n", "[4]   Sair")
                        try:
                            opcaoSistemaEmp = int(input("Digite a opção que desejar no menu: "))
                        except ValueError:
                            pass
                        if opcaoSistemaEmp == 1:
                            time.sleep(0.5)
                            system("cls")
                            dadospessoaisEmp()
                        elif opcaoSistemaEmp == 2:
                            time.sleep(0.5)
                            system("cls")
                            listaClientes()
                        elif opcaoSistemaEmp == 3:
                            time.sleep(0.5)
                            system("cls")
                            retirarEmpresa()
                            opcaoSistemaEmp = 4
                        elif opcaoSistemaEmp == 4:
                            pass
                        else:
                            print("Opção inválida")
                            time.sleep(0.5)
                            system("cls")
                            
                else:
                    pass
            else:
                print("Opção Inválida!")
                
    elif opcao == 3: # Sair
        pass

    else:
        print("Opção inválida")