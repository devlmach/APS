#CASA ELETRICIDADE
casa_eletricidade = int(input("""Gostaria de inserir seu consumo de ELETRICIDADE em: 
    1- R$/mês
    2- kWh/mês
    0- Não quero inserir valor
    Digite a opção: """))

print("")
if casa_eletricidade == 0:
    kgCO2anualEnergia = 0
elif casa_eletricidade == 1:
    valor = float(input("Digite o valor mensal do seu gasto em R$: "))
    kgCO2anualEnergia = valor * 1.2192
elif casa_eletricidade == 2:
    valor = float(input("Digite o consumo mensal de kWh: "))
    kgCO2anualEnergia = valor * 0.9  
else:
    print("Valor inválido")

print("")
#CASA GÁS
casa_gas = int(input("""Gostaria de inserir seu consumo de GÁS em: 
    1- R$/mês
    2- m³/mês
    3- Quantidade de botijões/mês
    0- Não quero inserir valor
    Digite a opção: """))

print("")
if casa_gas == 0:
    kgCO2anualGas = 0
elif casa_gas == 1:
    valorGas = float(input("Digite o valor mensal do seu gasto em R$: "))
    kgCO2anualGas = valorGas * 1.92
elif casa_gas == 2:
    valorGas = float(input("Digite o valor do seu gasto em m³: "))
    kgCO2anualGas = valorGas * 24.8052
elif casa_gas == 3:
    valorGas = int((input("Digite quantos botijões você usa no mês (valor arredondado): ")))
    kgCO2anualGas = valorGas * 35.256  
else:
    print("Valor inválido")
    
print("")
#TRANSPORTE INDIVIDUAL
somaIndividual = 0
while True:
    print("")
    transporte_individual = int(input("""Selecione o tipo de transporte individual que você usa:
        1- Carro
        2- Moto
        0- Nenhum dos dois acima
        Digite a opção: """))
    if transporte_individual == 0:
        break
    print("")
    combustivel = int(input("""Digite o tipo do combustível do seu transporte:
        1- Diesel
        2- Etanol
        3- Gasolina
        4- GNV 
        Digite a opção: """))

    print("")  
    km_rodados = float(input("Digite sua quilometragem rodada no mês: "))

#CARRO
    
    if transporte_individual == 1:
        print("")
        tipo_motor = int(input("""Selecione o tipo do motor do seu transporte:
        1- 1.0 a 1.5
        2- 1.6 a 2.0
        3- Maior que 2.0:
        Digite a opção: """))
        if combustivel == 1:
            if tipo_motor == 1 or tipo_motor == 2:
                kgCO2anualIndividual = 0
                print("Motores 1.0 a 2.0 não queimam Diesel.")
            elif tipo_motor == 3:
                kgCO2anualIndividual = km_rodados * 2.688
                somaIndividual += kgCO2anualIndividual
        elif combustivel == 2:
            if tipo_motor == 1: 
                kgCO2anualIndividual = km_rodados * 0.0168
                somaIndividual += kgCO2anualIndividual
            elif tipo_motor == 2:
                kgCO2anualIndividual = km_rodados * 0.0228
                somaIndividual += kgCO2anualIndividual
            elif tipo_motor == 3:
                kgCO2anualIndividual = km_rodados * 0.0348
                somaIndividual += kgCO2anualIndividual
        elif combustivel == 3:
            if tipo_motor == 1:
                kgCO2anualIndividual = km_rodados * 1.536
                somaIndividual += kgCO2anualIndividual 
            elif tipo_motor == 2:
                kgCO2anualIndividual = km_rodados * 2.028
                somaIndividual += kgCO2anualIndividual
            elif tipo_motor == 3:
                kgCO2anualIndividual = km_rodados * 2.964
                somaIndividual += kgCO2anualIndividual
        elif combustivel == 4:
            if tipo_motor == 1:
                kgCO2anualIndividual = km_rodados * 1.644
                somaIndividual += kgCO2anualIndividual
            elif tipo_motor == 2:
                kgCO2anualIndividual = km_rodados * 1.956
                somaIndividual += kgCO2anualIndividual
            elif tipo_motor == 3:
                kgCO2anualIndividual = km_rodados * 2.82
                somaIndividual += kgCO2anualIndividual

#MOTO
    elif transporte_individual == 2:
        print("")
        cilindradas = int(input("""Seleccione quantas cilindradas sua moto possui
        1- até 125ccc
        2- de 126cc a 250cc
        3- mais de 251cc
        Selecione sua opção: """))

        if combustivel == 1 or combustivel == 4:
            kgCO2anualIndividual = 0
            print("Motos queimam apenas gasolina ou etanol.")
        elif combustivel == 2:
            if cilindradas == 1:
                kgCO2anualIndividual = km_rodados * 0.0084
                somaIndividual += kgCO2anualIndividual
            elif cilindradas == 2:
                kgCO2anualIndividual = km_rodados * 0.0096
                somaIndividual += kgCO2anualIndividual
            elif cilindradas == 3:
                kgCO2anualIndividual = km_rodados * 0.0132
                somaIndividual += kgCO2anualIndividual
        elif combustivel == 3:
            if cilindradas == 1:
                kgCO2anualIndividual = km_rodados * 0.72
                somaIndividual += kgCO2anualIndividual
            elif cilindradas == 2:
                kgCO2anualIndividual = km_rodados * 0.816
                somaIndividual += kgCO2anualIndividual
            elif cilindradas == 3:
                kgCO2anualIndividual = km_rodados * 1.128   
                somaIndividual += kgCO2anualIndividual               
    
                
#TRANSPORTE PÚBLICO
soma = 0
while True:
    print("")
    transporte_publico = int(input("""Voce usa qual transporte público? 
    1- Metro
    2- Onibus
    0- Nenhum 
    Selecione a opção: """))
    
    if transporte_publico == 0:
        break

    print("")
    km = float(input("Digite a quilometragem mensal do uso do transporte: "))
    
    if transporte_publico == 1:
        kgCO2anualPublico = km * 0.048
        soma += kgCO2anualPublico
    elif transporte_publico == 2:
        kgCO2anualPublico = km * 1.056
        soma += kgCO2anualPublico
    
    
print("")
def resultado():
    print("")
    print(f"Toneladas de CO² emitidas anualmente em TRANSPORTE INDIVIDUAL: {(somaIndividual / 1000):.4f}")
    print(f"Toneladas de CO² emitidas anualmente em TRANSPORTE COLETIVO: {(soma / 1000):.4f}")
    print(f"Toneladas de CO² emitidas anualmente em ELETRICIDADE: {(kgCO2anualEnergia / 1000):.4f}")
    print(f"Toneladas de CO² emitidas anualmente em GÁS: {(kgCO2anualGas / 1000):.4f}")
    
    total = ((somaIndividual + soma + kgCO2anualEnergia + kgCO2anualGas) / 1000)
    print(f"{total:.4f} toneladas de CO² emitidas anualmente")
    tot = somaIndividual + soma + kgCO2anualEnergia + kgCO2anualGas

    numArvore = tot / 200
    
    print(f"Para compensar suas emissões, é preciso plantar {numArvore:.01f} árvores. Para essa compensação, você pode desembolsar um valor de R${20 * numArvore:.0f}")

resultado()








'''Gasto em R$ = (((T/60)*Kg/h)/B)*PB
Onde:
T = Tempo de uso em minutos dividido por 60;
Kg/h = Consumo por queimador, em Kg/h (ver o manual do fabricante do fogão)
B = Capacidade do botijão (13 ou 45 Kg);
PB = Preço do Botijão.'''