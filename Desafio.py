"""
Atividade para por e prática assuntos aprendidos!

Quero que você crie um programa que dirá se um entrevistado (um usuário) é do grupo de risco da COVID-19, 
ou não. Para isso, seguem as informações que você precisa coletar do usuário e as condições para determinar 
se o mesmo pertence ao grupo de risco, ou não;

->	O entrevistado possui mais de 60 anos?

->	O entrevistado possui alguma doença pré-existente, tipo asma, diabetes, hipertensão, ou câncer?

->	Se mulher, está grávida?

"""

# Dando boas vindas ao paciente (usuário):
print(''' 
      Olá seja muito bem vindo!! 
      Está é uma pesquisa para sabermos se o senhor ou senhorita estaria qualificado como parte do grupo de risco da COVID-19 ou não 
      ''')

# Criando variável de recomendação
Recomendação = '''
Nossas recomendações são:
1- Lavar as mãos frequentemente com água e sabão e passar álcool em gel;
2- Manter distância e evitar tocar em pessoas doentes;
3- Evitar lugares aglomerados e/ou fechados;
4- Quando tossir ou espirrar, cobrir a boca e o nariz;
5- Sempre utilize máscara!
'''

# Criando a sequência de perguntas e repostas:
Sexo = input('''
             Qual seu gênero? 
             Masculino (M)
             Feminino (F)
             Outro (O)
             Prefiro não participar (X)?\n
             ''')

if Sexo.upper( ) == "Feminino, F" or Sexo.upper( ) == "O":
    gravida = (input("Você está grávida? Sim ('S') ou Não ('N')?\n"))
    if Sexo.upper( ) == "F" and gravida.upper( ) == "S":
        print("\n Você faz parte do grupo de risco\n",Recomendação)
    else:
        idade = int(input("Qual a sua idade?\n"))
        if idade >=60:
           print("Você faz parte do grupo de risco\n",Recomendação)
        else:
           doença = (input("Você possui algum tipo de comorbidade? (Asma, Diabetes, Hipertensão ou Câncer). Sim ('S') ou Não ('N')?\n"))
        if doença.upper( ) == "S":
           print("Você faz parte do grupo de risco\n",Recomendação) 
        else:
           print("Carambolas!! vejo que você não faz parte de nenhum dos grupos de risco, mesmo assim deixo nossas recomendações para que evite a COVID-19\n",Recomendação)
        
elif Sexo.upper( ) == "M":
    idade = int(input("Qual a sua idade?\n"))
    if idade >=60:
        print("Você faz parte do grupo de risco\n",Recomendação)
    else:
        doença = (input("Você possui algum tipo de comorbidade? (Asma, Diabetes, Hipertensão ou Câncer). Sim ('S') ou Não ('N')?\n"))
        if doença.upper( ) == "S":
             print("Você faz parte do grupo de risco\n",Recomendação)
        else:
             print("Carambolas!! vejo que você não faz parte de nenhum dos grupos de risco, mesmo assim deixo nossa recomendação para que evite a COVID-19\n",Recomendação)
else:
    print("Muito obrigado de qualquer forma, mesmo assim recomendo que cuide de sua saúde e sempre siga nossas recomendações:\n", Recomendação)
