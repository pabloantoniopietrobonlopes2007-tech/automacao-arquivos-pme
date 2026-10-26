from pathlib import Path

caminho_data = "data_simulada"
arqs_organizados = {}

#cria objeto q instancia o caminho
pasta = Path(caminho_data)
#caso essa pasta seja existente
if pasta.exists():
    #vasculha todos os itens da pasta
    for item in pasta.iterdir():
        #verifica se o item é um arquivo ou pasta
        if item.is_file():
            sufixo = item.suffix.lower()
            if sufixo in arqs_organizados.keys():
                arqs_organizados[sufixo].append(item.name)
            else:
                arqs_organizados[sufixo] = []
                arqs_organizados[sufixo].append(item.name)

    for tipo, lista in arqs_organizados:
        print(f"sufixo: {tipo}")
        print(f"arquivos: {lista}")
else:
    print("essa pasta não existe")