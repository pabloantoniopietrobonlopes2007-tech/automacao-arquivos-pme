from pathlib import Path
import os
import shutil

#FUNÇÕES
def teste_repetido(item, lista):
    nome, tipo = os.path.splitext(item.name)
    contador = 1
    novo_nome = f"{nome}_{contador}{tipo}"

    #MUDA O NOME DO ARUIVO ATE ACHAR UM DIFERENTE
    while novo_nome in lista:
        contador += 1
        novo_nome = f"{nome}_{contador}{tipo}"
    return novo_nome


#PRÉ-DEFINIÇÕES

#regras para classificação por extenção
regras = {
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas": [".xlsx", ".csv"],
    "Imagens": [".jpg", ".jpeg", ".png"]
    #Outros     = qualquer extensão não conhecida
}

#LISTA DE ARQUIVOS APOS ORGANIZAÇÃO
categorias = {
    "Documentos": [],
    "Planilhas": [],
    "Imagens": [],
    "Outros": []
}

existentes = {
    "Documentos": [],
    "Planilhas": [],
    "Imagens": [],
    "Outros": []
}

#CAMINHO DA PASTA COM DADOS
caminho_data = "data_simulada"

#objeto da pasta com dados
pasta_data = Path(caminho_data)

#VERIFICA SE A PASTA COM DADOS A SEREM ORGANIZADOS EXISTE
if pasta_data.exists() and pasta_data.is_dir():

    #CRIAÇÃO DAS PASTAS DE ORGANIZAÇÃO(DENTRO DA PASTA DE DADOS)
    for categoria in categorias:
        caminho_dir = Path(caminho_data)/ categoria
        os.makedirs(caminho_dir, exist_ok=True)
        for arqs in caminho_dir.iterdir():
            if arqs.is_file():
                existentes[categoria].append(arqs.name)

    #VERIFICA CADA ITEM DA PASTA COM DADOS
    for item in pasta_data.iterdir():

        

        #VERIFICA SE O ITEM É UM ARQUIVO
        if item.is_file():

            extensao = item.suffix.lower()
            encontrado = False
            falha = False
            #VERIFICA A EXTENSÃO
            for categoria, lista in regras.items():
                #encontra categoria
                if extensao in lista:
                    nome_arq = item.name
                    
                    #VERIFICA SE ITEM JA EXISTE
                    if nome_arq in existentes[categoria]:
                        nome_arq = teste_repetido(item, existentes[categoria])

                    #DESTINO FINAL COM O NOVO NOME
                    destino = os.path.join(caminho_data, categoria, nome_arq)
                    try:
                        shutil.move(item, destino)
                        categorias[categoria].append(nome_arq)
                        existentes[categoria].append(nome_arq)
                        encontrado = True
                        break
                    except OSError as erro:
                        falha = True
                        print(erro)
                        break
                    """
                    else:
                        destino = os.path.join(caminho_data,categoria, nome_arq)
                        shutil.move(item, destino)
                        categorias[categoria].append(nome_arq)
                        existentes[categoria].append(nome_arq)
                        encontrado = True
                        break
                    """

            #CASO NÃO TENHA A EXTENSÃO DE UMA CATEGORIA ESPECIFICADA VAI PARA OUTROS
            if not encontrado and not falha:
                nome_arq = item.name

                if nome_arq in existentes["Outros"]:
                    nome_arq = teste_repetido(item, existentes["Outros"])

                    """
                    #DESTINO FINAL COM O NOVO NOME      
                    destino = os.path.join(caminho_data, "Outros", nome_arq)
                    try:
                        shutil.move(item, destino)
                        existentes["Outros"].append(nome_arq)
                        categorias["Outros"].append(nome_arq)
                    except OSError as erro:
                        print(erro)
                        continue
                    """
                """
                else:
                    destino = os.path.join(caminho_data, "Outros", nome_arq)
                    try:
                        shutil.move(item, destino)
                        existentes["Outros"].append(nome_arq)
                        categorias["Outros"].append(nome_arq)
                    except OSError as erro:
                        print(erro)
                        continue
                    """
                #DESTINO FINAL COM O NOVO NOME      
                destino = os.path.join(caminho_data, "Outros", nome_arq)
                try:
                    shutil.move(item, destino)
                    existentes["Outros"].append(nome_arq)
                    categorias["Outros"].append(nome_arq)
                except OSError as erro:
                    print(erro)
                    continue

else:
    print("Pasta não encontrada")


#MOSTRA O RESULTADO DA ORGANIZAÇÃO
for categoria in categorias.items():
    print(categoria)
print("-"*50)
for categoria in existentes.items():
    print(categoria)
