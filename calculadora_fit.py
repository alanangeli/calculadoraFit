nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = int(input("Digite sua altura em centímetros: "))
peso = int(input("Digite seu peso: "))
print("Digite o número correspondente abaixo")
print("(1) - Homem")
print("(2) - Mulher")
sexo = int(input("Qual seu sexo? "))

tmb_masculino = 66 + (14 * peso ) + (5 * altura) - (7 * idade)
tmb_feminino = 655 + (10 * peso) + (2 * altura) - (5 * idade)

#gasto diário masculino

gasto_diario_moderado_mas =  tmb_masculino + 500
gasto_diario_intenso_mas =  tmb_masculino + 800

#deficit diário masculino
deficit_masc_moder = gasto_diario_moderado_mas - 400
deficit_masc_intenso = gasto_diario_intenso_mas - 400

#superavit diário masculino
superavit_masc_moder = gasto_diario_moderado_mas  + 500
superavit_masc_intenso = gasto_diario_intenso_mas + 500

#gasto diário feminino
gasto_dfem_mod = tmb_feminino + 300
gasto_dfem_int = tmb_feminino + 500

#deficit feminino
deficit_fem_mod= gasto_dfem_mod - 200
deficit_fem_int= gasto_dfem_int- 300

#superavit feminino
superavit_fem_mod = gasto_dfem_mod + 300
superavit_fem_int= gasto_dfem_int + 300




print("Digite o número correspondente abaixo")
print("(1) - Sou sedentário")
print("(2) - Pratico de forma moderada")
print("(3) - Pratico de forma intensa")
atividade_fisica = int(input("Você pratica atividade física com regularidade? "))


if sexo == 1:
    print(nome, ", sua taxa de metabolismo basal é de", tmb_masculino, "kcal")
    if atividade_fisica == 1:
        print("É recomendado que pratrique alguma atividade física.")
    elif atividade_fisica == 2:
        print("Você tem um gasto calórico de aproximadamente", gasto_diario_moderado_mas, "kcal por dia")
        print("Para ganhar mais massa muscular, é necessário ingerir", superavit_masc_moder, "kcal por dia")
        print("Para emagrecimento, é necessário ingerir", deficit_masc_moder, "kcal por dia")
    elif atividade_fisica == 3:
        print("Você tem um gasto calórico de aproximadamente", gasto_diario_intenso_mas, "kcal por dia")
        print("Para ganhar mais massa muscular, é necessário ingerir", superavit_masc_intenso, "kcal por dia")
        print("Para emagrecimento, é necessário ingerir",deficit_masc_intenso, "kcal por dia")

elif sexo == 2:
    print(nome, ", sua taxa de metabolismo basal é de", tmb_feminino, "kcal")
    if atividade_fisica == 1:
        print("É recomendado que pratrique alguma atividade física.")
    elif atividade_fisica == 2:
        print("Você tem um gasto calórico de aproximadamente", gasto_dfem_mod, "kcal por dia")
        print("Para ganhar mais massa muscular, é necessário ingerir", superavit_fem_mod, "kcal por dia")
        print("Para emagrecimento, é necessário ingerir", deficit_fem_mod, "kcal por dia")
    elif atividade_fisica == 3:
        print("Você tem um gasto calórico de aproximadamente", gasto_dfem_int, "kcal por dia")
        print("Para ganhar mais massa muscular, é necessário ingerir", superavit_fem_int, "kcal por dia")
        print("Para emagrecimento, é necessário ingerir",deficit_fem_int, "kcal por dia")
        
        

