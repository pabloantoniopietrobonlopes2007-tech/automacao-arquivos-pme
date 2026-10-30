from pathlib import Path
import os

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

#CAMINHO DA PASTA COM DADOS
caminho_data = "data_simulada"

#objeto da pasta com dados
pasta_data = Path(caminho_data)

#VERIFICA SE A PASTA COM DADOS A SEREM ORGANIZADOS EXISTE
if pasta_data.exists():

    #CRIAÇÃO DAS PASTAS DE ORGANIZAÇÃO(DENTRO DA PASTA DE DADOS)
    for categoria in categorias:
        os.makedirs(f"{caminho_data}/{categoria}", exist_ok=True)

    #VERIFICA CADA ITEM DA PASTA COM DADOS
    for item in pasta_data.iterdir():

        #VERIFICA SE O ITEM É UM ARQUIVO
        if item.is_file():

            extensao = item.suffix.lower()
            encontrado = False
            #VERIFICA A EXTENSÃO
            for categoria, lista in regras.items():
                #encontra categoria
                if extensao in lista:
                    categorias[categoria].append(item.name)
                    encontrado = True
                    break
                    """"
                    #VERIFICA SE ITEM JA EXISTE
                    if item.name in lista_categoria:
                        nome, tipo = os.path.splitext(item.name)
                        contador = 1
                        novo_nome = f"{nome} ({contador}){tipo}"

                        #MUDA O NOME DO ARUIVO ATE ACHAR UM DIFERENTE
                        while novo_nome in lista_categoria:
                            contador += 1
                            novo_nome = f"{nome} ({contador}){tipo}"
                        print(f"Arquivo {item.name} duplicado. Renomeando para {novo_nome}")
                        item.name = novo_nome  # Atualiza para renomear/mover o arquivo fisicamente
                        lista_categoria.append(novo_nome)
                        encontrado = True
                        break

                    else:
                        lista_categoria.append(item.name)
                        encontrado = True
                        break
                    """

            #CASO NÃO TENHA A EXTENSÃO DE UMA CATEGORIA ESPECIFICADA VAI PARA OUTROS
            if not encontrado:
                categorias["Outros"].append(item.name)


else:
    print("Pasta não encontrada")


#MOSTRA O RESULTADO DA ORGANIZAÇÃO
for categoria in categorias.items():
    print(categoria)