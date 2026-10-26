from pathlib import Path
import os

regras = {
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas": [".xlsx", ".csv"],
    "Imagens": [".jpg", ".jpeg", ".png"]
    #Outros     = qualquer extensão não conhecida
}

caminho_data = "data_simulada"
arqs_organizados = {
    "Documentos": [],
    "Planilhas": [],
    "Imagens": [],
    "Outros": []
}

pasta = Path(caminho_data)
#caso essa pasta seja existente
if pasta.exists() and pasta.is_dir():

    for item in arqs_organizados:
        os.makedirs(f"data_simulada/{item}", exist_ok=True)

    #vasculha todos os itens da pasta
    for item in pasta.iterdir():
        #verifica se o item é um arquivo ou pasta
        if item.is_file():
            sufixo = item.suffix.lower()
            encontrado = False
            for chave, lista in regras.items():
                if sufixo in lista:
                    arqs_organizados[chave].append(item.name)
                    encontrado = True
                    break
            if not encontrado:
                arqs_organizados["Outros"].append(item.name)


    for chave, lista in arqs_organizados.items():
        print(f"{chave}: {lista}")

else:
    print("essa pasta não existe")