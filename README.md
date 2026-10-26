# Automação Inteligente de Arquivos, Pastas e Planilhas Empresariais com Python e Inteligência Artificial

Sistema de automação em Python que organiza arquivos, cria pastas automaticamente, processa planilhas de gastos e permite consultas em linguagem natural sobre os documentos de uma pequena ou média empresa (PME).

Projeto de Iniciação Científica (PIBIFSP) — IFSP, 2026.

## Sumário

- [Qual problema o projeto pretende resolver?](#qual-problema-o-projeto-pretende-resolver)
- [Qual é o objetivo do sistema?](#qual-é-o-objetivo-do-sistema)
- [Quais funcionalidades estão previstas?](#quais-funcionalidades-estão-previstas)
- [Quais tecnologias estão sendo consideradas?](#quais-tecnologias-estão-sendo-consideradas)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Roteiro de desenvolvimento](#roteiro-de-desenvolvimento)
- [Status do projeto](#status-do-projeto)

## Qual problema o projeto pretende resolver?

Pequenas e médias empresas (PMEs) costumam armazenar documentos, contratos, planilhas de gastos e outros arquivos de forma desorganizada. Esse modelo manual torna a localização de informações um processo repetitivo, demorado e sujeito a erros, comprometendo a produtividade e a tomada de decisão.

Na prática, isso significa:

- Profissionais gastam tempo excessivo procurando arquivos espalhados em pastas e planilhas.
- Informações importantes se perdem por falta de padronização e rastreabilidade.
- Decisões são tomadas com base em dados dispersos, muitas vezes desatualizados.

O projeto busca eliminar a busca manual por meio de **organização automática** dos arquivos e de **consultas em linguagem natural** sobre o que já está armazenado.

## Qual é o objetivo do sistema?

**Objetivo geral:** desenvolver um sistema de automação baseado em Python e Inteligência Artificial, capaz de organizar arquivos, pastas e planilhas de gastos de PMEs e permitir consultas rápidas e instantâneas sobre os dados armazenados.

**Objetivos específicos:**

- **Organização automática:** ler, classificar e movimentar arquivos para as pastas corretas conforme sua categoria.
- **Criação automática de pastas:** estruturar o diretório a partir das categorias identificadas pelo sistema.
- **Tratamento de planilhas:** ler e organizar planilhas de gastos com `pandas` e `openpyxl`.
- **Classificação inteligente:** classificar arquivos pelo conteúdo, não apenas pela extensão.
- **Busca em linguagem natural:** permitir perguntas como *"onde estão os contratos?"* e retornar o resultado de forma instantânea.
- **Rastreabilidade:** registrar todas as movimentações em um banco de dados local.
- **Acessibilidade:** manter a solução leve, local e de baixo custo, viável para PMEs.

## Quais funcionalidades estão previstas?

| Funcionalidade | Descrição | Status |
| :-- | :-- | :-- |
| **Varredura de arquivos** | Percorrer um diretório informado pelo usuário e identificar todos os arquivos. | Em desenvolvimento |
| **Classificação por tipo** | Separar arquivos por categoria com base na extensão (documentos, planilhas, imagens, contratos, outros). | Em desenvolvimento |
| **Criação automática de pastas** | Criar as pastas de destino conforme as categorias identificadas, sem duplicar as existentes. | Em desenvolvimento |
| **Movimentação automática** | Mover os arquivos para as pastas correspondentes, tratando conflitos de nome. | Em desenvolvimento |
| **Organização de planilhas de gastos** | Ler planilhas `.xlsx` e `.csv` e organizar os dados para consulta. | Em desenvolvimento |
| **Interface CLI** | Execução via terminal com argumentos claros (`--dir`, `--buscar`, `--help`). | Em desenvolvimento |
| **Histórico de movimentações** | Registrar em SQLite: arquivo, origem, destino, categoria e data/hora. | Prevista |
| **Relatório de organização** | Gerar relatório `.csv` com o histórico das movimentações. | Prevista |
| **Classificação inteligente com IA** | Classificar arquivos pelo conteúdo textual usando PLN. | Prevista |
| **Busca semântica em linguagem natural** | Buscar por significado com *embeddings* locais, em português. | Prevista |

## Quais tecnologias estão sendo consideradas?

| Tecnologia | Categoria | Justificativa |
| :-- | :-- | :-- |
| **[Python 3](https://www.python.org/)** | Linguagem principal | Simples, com amplo ecossistema para automação, dados e IA. |
| **[pathlib](https://docs.python.org/3/library/pathlib.html), [os](https://docs.python.org/3/library/os.html) e [shutil](https://docs.python.org/3/library/shutil.html)** | Manipulação de arquivos e pastas | Bibliotecas nativas para varredura, movimentação e criação de diretórios. |
| **[pandas](https://pandas.pydata.org/) e [openpyxl](https://openpyxl.readthedocs.io/)** | Manipulação de planilhas | Leitura, tratamento e organização das planilhas de gastos. |
| **[argparse](https://docs.python.org/3/library/argparse.html)** | Interface CLI | Interface de terminal sem necessidade de GUI. |
| **[sqlite3](https://docs.python.org/3/library/sqlite3.html)** | Banco de dados local | Armazenar o histórico de movimentações de forma leve. |
| **[sentence-transformers](https://www.sbert.net/) e [scikit-learn](https://scikit-learn.org/)** | IA e busca semântica | Gerar *embeddings* locais e calcular similaridade de cosseno, sem depender de APIs pagas. |
| **[logging](https://docs.python.org/3/library/logging.html)** | Rastreamento | Registrar ações, erros e eventos do sistema. |
| **[rich](https://github.com/Textualize/rich)** (opcional) | CLI aprimorada | Tabelas, cores e mensagens mais legíveis no terminal. |

## Estrutura do projeto

```text
automacao-arquivos-pme/
├── src/               # Código-fonte do sistema
├── config/            # Arquivos de configuração (ex: config.json)
├── data_simulada/     # Base fictícia representando uma PME (para testes)
├── docs/              # Documentação e anotações do projeto
├── logs/              # Logs de execução
├── requirements.txt
├── .gitignore
├── README.md
└── Plano_de_Estudos_Automacao_Inteligente.md
```

## Como executar

```bash
# 1. Clone o repositório
git clone https://github.com/pabloantoniopietrobonlopes2007-tech/automacao-arquivos-pme.git
cd automacao-arquivos-pme

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows (CMD)
.\venv\Scripts\Activate.ps1  # Windows (PowerShell)

# 3. Instale as dependências
pip install -r requirements.txt
```

> A execução do sistema (`python src/main.py --dir ./data_simulada`) será documentada aqui assim que o MVP estiver disponível.

## Roteiro de desenvolvimento

O projeto evolui em fases, sempre priorizando o MVP da Iniciação Científica antes de qualquer melhoria de portfólio.

| Fase | Foco |
| :-- | :-- |
| **0. Preparação** | Repositório, ambiente virtual, estrutura de pastas e base de dados simulada. |
| **1. MVP da IC** | Varredura, classificação por tipo, criação de pastas, movimentação e leitura de planilhas. |
| **2. Refatoração** | Modularização, classes, configuração via `config.json`, logs, tratamento de erros e tipagem. |
| **3. Banco de dados** | Histórico em SQLite e geração de relatório em CSV. |
| **4. IA** | Classificação pelo conteúdo com regras e depois *embeddings* locais. |
| **5. Busca em linguagem natural** | Indexação, busca semântica no CLI e polimento final. |

O detalhamento de cada etapa, com tarefas e tempo estimado, está em [`Plano_de_Estudos_Automacao_Inteligente.md`](./Plano_de_Estudos_Automacao_Inteligente.md).

## Status do projeto

**Em desenvolvimento — Fase 1 (MVP da Iniciação Científica).**

Nenhuma funcionalidade está concluída ainda. A coluna *Status* da tabela de funcionalidades é atualizada conforme o desenvolvimento avança.

## Informações institucionais

- **Modalidade:** Bolsa PIBIFSP de Iniciação Científica
- **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP)
- **Área do conhecimento:** Ciência da Computação — Metodologia e Técnicas da Computação
- **Ano:** 2026
- **Tipo de solução:** protótipo funcional com validação em base de dados simulada

## Licença

Projeto acadêmico desenvolvido para fins de pesquisa e divulgação científica.
