import fundamentus
import pprint


response = int(input("Você deseja: \n[1] - Ver a lista de empresas e tickets\n[2] - Ver a lista de empresas por setor\n"
                     "[3] - Já possuo um ticket para avaliar"))


stock = str(input("digite o papel que você deseja analisar: "))

result = fundamentus.get_resultado()

#fundamentus.print_table(result.columns)
pprint.pprint(result['cotacao'])
