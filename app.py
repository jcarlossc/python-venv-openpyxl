# Importa módulo Openpyxl
from openpyxl import Workbook

# Criar um novo arquivo do Excel
arquivo_excel = Workbook()

# Selecionar a planilha ativa
planilha_ativa = arquivo_excel.active

# Adicionar dados a células específicas
planilha_ativa["A1"] = "Nome"
planilha_ativa["B1"] = "Idade"
planilha_ativa["C1"] = "Peso"
planilha_ativa["D1"] = "Altura"
planilha_ativa.append(["Carlos", 25, 60.65, 1.62])
planilha_ativa.append(["soares", 30, 89.90, 1.73])
planilha_ativa.append(["Teresa", 18, 70.90, 1.73])
planilha_ativa.append(["José", 47, 85.56, 1.83])

# Salva o arquivo no diretório 'planilhas'
arquivo_excel.save("planilhas/planilha.xlsx")  

print("Arquivo criado com sucesso!")

# OBS: Antes de executar o script, apague o arquivo 'planilha.xls' que está no diretório 'planilhas'  