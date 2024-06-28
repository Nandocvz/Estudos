#Neste inicio de codigo, irei utilizar o dict para definir diversas funções especificas ao "aluno" e retomar cada uma delas no momento que necessário.
aluno = dict() 
"""
Defini o "Aluno" como uma base para outros nomes que são: aop01, aop02, aop03, prova_regular, prova_recuperacao, status
"""
turma = list()
aprovados = 0
reprovados = 0

for user in range(1, 100):
    aluno["nome"] = f"aluno {user}"
    
    #Aqui irei definir a nota da Aop 01
    try:
        aluno["Aop01"] = float(input('Nota [0, 1] na AOP 01: Atividade Online Pontuada 01:\n'))
        if aluno["Aop01"] < 0 or aluno["Aop01"] > 1:
            raise ValueError
    except ValueError:
        while True:
            try:
                aluno["Aop01"] = float(input("Nota inválida, digite uma nova nota entre 0 e 1 para a AOP 01:\n "))
                if aluno["Aop01"] >= 0 and aluno["Aop01"] <= 1:
                    break #utilizando o break para quebrar o looping do if
            except ValueError:
                pass         

    #Aqui irei definir a nota da Aop 02
    try: 
        aluno["Aop02"] = float(input("Nota [0, 2] na AOP 02: Atividade Online Pontuada 02:\n"))
        if aluno["Aop02"] < 0 or aluno["Aop02"] > 2:
            raise ValueError
    except ValueError:
        while True:
            try:
                aluno["Aop02"] = float(input("Nota inválida, digite uma nova nota entre 0 e 2 para a AOP 02:\n"))
                if aluno["Aop02"] >= 0 and aluno["Aop02"] <= 2:
                    break #utilizando o break para quebrar o looping do if
            except ValueError:
                pass
    
    #Aqui irei definir a nota da Aop 03
    try:
        aluno["Aop03"] = float(input("Nota [0, 1] na AOP 03: Atividade Online Pontuada 03:\n"))
        if aluno["Aop03"] < 0 or aluno["Aop03"] > 1:
            raise ValueError
    except ValueError:
        while True:
            try:
                aluno["Aop03"] = float(input("Nota inválida, digite uma nova nota entre 0 e 1 para a AOP 03:\n"))
                if aluno["Aop03"] >= 0 and aluno["Aop03"] <= 1:
                    break #utilizando o break para quebrar o looping do if
            except ValueError:
                pass
    
    #Aqui irei definir a nota da prova regular
    try:
        aluno["prova_regular"] = float(input("Nota [0, 6] da PROVA REGULAR:\n"))
        if aluno["prova_regular"] < 0 or aluno["prova_regular"] > 6:
            raise ValueError
    except ValueError:
        while True:
            try: 
                aluno["prova_regular"] = float(input("Nota inválida, digite um valor entre 0 e 6 para a prova regular:\n"))
                if aluno["prova_regular"] >= 0 and aluno["prova_regular"] <= 6:
                    break #utilizando o break para quebrar o looping do if
            except ValueError:
                pass
    
    soma_aop = aluno["Aop01"] + aluno["Aop02"] + aluno["Aop03"] + aluno["prova_regular"]
    print(f'Soma do Módulo (SM) do {aluno["nome"]} = Nota da Aop 01 ({aluno["Aop01"]}) + Nota da Aop 02({aluno["Aop02"]}) + Nota da Aop 03({aluno["Aop03"]}) + Nota da prova regular({aluno["prova_regular"]})')
    print(f'Soma do Módulo (SM) do {aluno["nome"]} = ', soma_aop)

    if soma_aop < 7:
        try:
            aluno["prova_recuperacao"] = float(input("Nota [0, 10] da PROVA DE RECUPERAÇÃO:\n"))
            if aluno["prova_recuperacao"] < 0 or aluno["prova_recuperacao"] > 10:
                raise ValueError
        except ValueError:
            while True:
                try:
                    aluno["prova_recuperacao"] =  float(input("Nota inválida, digite um valor entre 0 e 10 para a prova de recuperação:\n"))
                    if aluno["prova_recuperacao"] >= 0 and aluno["prova_recuperacao"] <= 10:
                        break #utilizando o break para quebrar o looping do if
                except ValueError:
                    pass
        #Nesta parte iremos verificar se o aluno foi ou não aprovado na prova de recuperação
        prova_recuperacao = aluno["prova_recuperacao"]
        media_final = (prova_recuperacao + soma_aop)/2

        if media_final < 5:
            aluno["status"] = "Reprovado"
            print(f'Status do {aluno["nome"]} = {aluno["status"]}')
            reprovados += 1
        else:
            aluno["status"] = "Aprovado pela prova de recuperação"
            print(f'Status do {aluno["nome"]} = {aluno["status"]}')
            aprovados += 1
    else:
        aluno["status"] = "Aprovado"
        print(f'Status do {aluno["nome"]} = {aluno["status"]}')
        aprovados += 1
        
#Logo a baixo estarei definindo a porcentagem de alunos que foram aprovados e reprovados.
total = aprovados + reprovados

porcentagem_aprovados = (aprovados / total) * 100
porcentagem_reprovados = (reprovados / total) * 100

print(f'A porcentagem de aprovados foi {porcentagem_aprovados:.1f}% com {aprovados} alunos.')
print(f'A porcentagem de reprovados foi {porcentagem_reprovados:.1f}% com {reprovados} alunos')           