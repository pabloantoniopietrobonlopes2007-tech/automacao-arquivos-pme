# Plano de Estudos: Automação Inteligente de Arquivos, Pastas e Planilhas

O objetivo aqui é simples: **unir sua Iniciação Científica com seu portfólio voltado para Dev Júnior Python**. Tudo vai girar em torno de **UM ÚNICO REPOSITÓRIO**, crescendo verticalmente a cada etapa.

**Nome do repositório:** `automacao-arquivos-pme`

**Tempo disponível:** ~3 horas diárias (trabalhando)

## 1) Rotina para 3h Diárias

Não tente estudar tudo de uma vez. Use esse divisão para manter o foco e ainda aprender com eficiência.

| Tempo | Atividade | Objetivo |
| :-- | :-- | :-- |
| **30 min** | *Revisão + Git* | Ver o que fez ontem, pensar no que vai fazer hoje e fazer um commit com descrição clara. |
| **1h30** | *Prática (Código)* | Mão na massa. Resolva o problema da etapa sem pedir pro ChatGPT fazer tudo. |
| **1h** | *Aprendizado Direcionado + Testes* | Estudar a biblioteca que acabou de usar, teste com dados simulados e anotar aprendizados em um `anotacoes.md`. |

## 2) Plano Por Etapas

### FASE 0: Preparação (1 - 2 dias | ~3 - 6 horas)

Antes de codar, organize tudo para manter esse projeto limpo desde o início.

| Passo | Tarefa | Aprendizado | Status |
| :-- | :-- | :-- | :-- |
| **0.1** | Criar o repositório `automacao-arquivos-pme` no GitHub. | Git, versionamento e organização. | [ ] |
| **0.2** | Criar ambiente virtual (`venv`) e arquivo `requirements.txt`. | Ambientes isolados. | [ ] |
| **0.3** | Montar a estrutura inicial: `src/`, `data_simulada/`, `config/`, `logs/`, `docs/`. | Organização profissional. | [ ] |
| **0.4** | Criar uma pasta `data_simulada/` com arquivos falsos (contratos `.PDF`, `.DOCX`, planilhas `.XLSX`, imagens, etc). | Ter dados reais pra teste sem usar arquivos pessoais. | [ ] |
| **0.5** | Ler novamente o PDF da sua IC e anotar **exatamente** o que precisa pro MVP. | Saber distinguir "obrigatório" x "diferencial. | [ ] |

**Meta:** Repositório criado, estruturado e pronto para iniciar o MVP.

### FASE 1: MVP da Iniciação Científica (2 - 3 semanas | ~30 - 40 horas)

Aqui é **prioridade máxima**. Foque em cumprir o que foi proposto no projeto, da forma mais simples e funcional possível.

| Passo | Tarefa | Aprendizado | Status |
| :-- | :-- | :-- | :-- |
| **1.1** | **Varredura de arquivos** | Aprenda `pathlib.Path`, `os.listdir` e filtragem por extensão. | [ ] |
| **1.2** | **Classificação por tipo** | Criar regras para separar por categoria: Documentos, Planilhas, Imagens, Contratos, Outros. | [ ] |
| **1.3** | **Criação automática de pastas** | Usar `os.makedirs` e `pathlib.mkdir(exist_ok=True)`. Tratar casos onde a pasta já existe. | [ ] |
| **1.4** | **Movimentação de arquivos** | Aprender `shutil.move`. Cuidar de possíveis conflitos (arquivo com mesmo nome). | [ ] |
| **1.5** | **Organização of planilhas** | Usar `pandas` and `openpyxl` para ler planilhas de gastos, identificar colunas e extrair informações relevantes. | [ ] |
| **1.6** | **Interface CLI** | Criar um `main.py` simples com `argparse` para rodar: `python main.py --dir ./data_simulada`. | [ ] |
| **1.7** | **Testes com dados simulados** | Rodar várias vezes com seus arquivos falsos, corrigir bugs e garantir que está estável. | [ ] |

**Meta:** MVP funcional, rodando pelo terminal e cumprindo o essencial da sua IC.

### FASE 2: Refatoração para Portfólio (1 - 2 semanas | ~15 - 20 horas)

Com the MVP funcionando, é hora de deixar com **cara of projeto profissional**. Isso vai fazer toda a diferença no GitHub.

| Passo | Tarefa | Aprendizado | Status |
| :-- | :-- | :-- | :-- |
| **2.1** | **Modularizar** | Mover código para `src/`. Ex: `src/scanner.py`, `src/classifier.py', `src/mover.py', `src/sheets.py'. | [ ] |
| **2.2** | **Criar classes** | Transformar funções soltas in classes (`FileOrganizer`, `SheetProcessor`). Isso ensina POO na prática. | [ ] |
| **2.3** | **Sistema de configuração** | Criar `config/config.json`. Permitir alterar pastas de destino and extensões sem mexer no código. | [ ] |
| **2.4** | **Logs** | Implementar `logging` (criar `logs/organizer.log'). Registrar: arquivo movido, data/hora and status. | [ ] |
| **2.5** | **Tratamento de erros** | Tratar permissões, arquivos abertos, nomes duplicados and caminhos inválidos. | [ ] |
| **2.6** | **Tipagem** | Adicionar type hints (`typing') em funções and classes. Mostra that you already pensa em código mais limpo. | [ ] |
| **2.7** | **Melhorar README** | Colocar: objetivo, tecnologias, print "antes/depois", como rodar, estrutura and próximos passos. | [ ] |

**Meta:** Código organizado, legível and com cara de projeto pronto pra be avaliado.

### FASE 3: Histórico com Banco de Dados (1 - 2 semanas | ~12 - 16 horas)

Here you começa to trilhar direto pro caminho of **Backend**. Perfeito pra unir with your objective.

| Passo | Tarefa | Aprendizado | Status |
| :-- | :-- | :-- | :-- |
| **3.1** | **Modelagem** | Criar tabela `historico` with: `id`, `nome_arquivo', `extensao', `origem', `destino', `categoria', `data_hora`. | [ ] |
| **3.2** | **Conexão com SQLite** | Usar `sqlite3` first (mais simples). Depois você pode migrar pra `SQLAlchemy` se quiser reforçar. | [ ] |
| **3.3** | **Registro automático** | A cada arquivo movido, salvar uma linha no banco. | [ ] |
| **3.4** | **Consulta ao histórico** | Criar uma função `ver_historico()` para listar as últimas movimentações pelo CLI. | [ ] |
| **3.5** | **Relatório simples** | Gerar um `.CSV` with todo o histórico usando `pandas`. Ótimo pra show pro orientador da IC. | [ ] |

**Meta:** Ter rastreabilidade completa. Saber "o que foi movido, quando and pra onde".

### FASE 4: Classificação Inteligente com IA (2 - 3 semanas | ~20 - 25 horas)

É aqui that you cumpre a parte mais interessante da sua IC. **Comece pelo mais simples and vá evoluindo.**

| Passo | Tarefa | Aprendizado | Status |
| :-- | :-- | :-- | :-- |
| **4.1** | **Classificação por regras** | Melhorar the classificador with palavras-chave (ex: "contrato", "nota", "boleto", "recibo"). | [ ] |
| **4.2** | **Análise de conteúdo** | Para `.TXT` and `.CSV', ler o conteúdo and classificar with base nas palavras encontradas. | [ ] |
| **4.3** | **Preparação for embeddings** | Instalar `sentence-transformers`. Entender o conceito de *embedding* na prática (sem teoria excessiva, só aplicando). | [ ] |
| **4.4** | **Classificação semântica local** | Criar um "mapa of categorias". Comparar o texto do arquivo with as descrições das categorias usando similaridade de cosseno. **Tudo 100% local.** | [ ] |
| **4.5** | **Unificar classificadores** | Fazer com que o sistema tente: 1) Regras 2) Análise de conteúdo 3) Semântica. Escolher o resultado with maior confiança. | [ ] |
| **4.6** | **Testar with dados reais-simulados** | Testar with contratos and planilhas fictícias. Ajustar palavras-chave até ter a precisão razoável. | [ ] |

**Meta:** Sistema realmente "inteligente". Classificando not só pela extensão, but pelo **conteúdo**.

### FASE 5: Busca em Linguagem Natural + Polimento (1 - 2 semanas | ~12 - 16 horas)

Esse é the **diferencial that vai te destacar absurdamente** no portfólio.

| Passo | Tarefa | Aprendizado | Status |
| :-- | :-- | :-- | :-- |
| **5.1** | **Indexação** | Gerar embeddings of todos os arquivos já organized and salvar in um arquivo local (`.json` or `faiss`). | [ ] |
| **5.2** | **Busca semântica CLI** | Criar um comando: `python main.py --buscar "onde estão os contratos?"`. Retornar caminho, categoria and similaridade. | [ ] |
| **5.3** | **Melhorar UX do CLI** | Adicionar cores with `rich` (opcional), mensagens claras and ajuda (`--help`). Fica muito mais agradável de usar. | [ ] |
| **5.4** | **Finalizar README** | Adicionar: demonstração (antes/depois), arquitetura, funcionalidades, evolução do projeto and **prints**. Coloque também "Aprendizados. | [ ] |
| **5.5** | **Polir Git** | Fazer commits semânticos (`feat:`, `refactor:`, `docs:`), limpar arquivos desnecessários and verificar `.gitignore`. | [ ] |
| **5.6** | **Preparar for apresentação da IC** | Fazer a teste completo do zero. Grave mentalmente the passo a passo pra explicar tranquilamente pro orientador. | [ ] ]

**Meta:** Ter a projeto **único, funcional and apresentável** tanto pra sua IC quanto pro your portfólio.

## 3) Cronograma Sugerido (Realista with 3h/dia)

Não se prenda to datas exatas. Use isso as **norte**, não como obrigação rígida.

| Período | Foco | Observação |
| :-- | :-- | :-- |
| **Semana 1 - 2** | **Fase 0 + 1** | 100% voltado pro MVP of IC. Não pense em IA ainda. Garanta that mova and organize corretamente. |
| **Semana 3 - 4** | **Fase 2** | Refatoração. Parece chato, mas é a etapa that mais te aproxima of um código "empregável". |
| **Semana 5** | **Fase 3** | Banco SQLite. Muito prático and te dá confiança with SQL na prática. |
| **Semana 6 - 8** | **Fase 4** | IA with regras + embeddings locais. Vá devagar, entenda each linha. |
| **Semana 9 - 10** | **Fase 5** | Busca in linguagem natural + polimento. Feche with chave de ouro. |

*Se in alguma semana sobrar pouco tempo por conta do trabalho, **corte quantity, never cut consistency**. 3h focadas valem muito more than 6h distraídas.*

## 4) Recursos Recomendados

Foque **apenas** nesses here. Não fique pulando entre 10 tutoriais ao mesmo tempo.

| Recurso | Uso |
| :-- | :-- |
| **[Documentação Python - os/shutil/pathlib](https://docs.python.org/3/)** | Base para manipulação de arquivos. Vá direto nas funções that you really precisa. |
| **[Pandas Docs](https://pandas.pydata.org/docs/)** | Essencial pra ler/organizar planilhas. Foque em `read_excel`, `DataFrame` and filtros. |
| **[Sentence-Transformers](https://www.sbert.net/)** | Perfeito pra fazer embeddings localmente, sem gastar nada. |
| **[Real Python](https://realpython.com/)** | Explica conceitos complexos of forma clara. Ótimo when travar in something and não entender. |
| **[FastAPI Tutorial (apenas consulta)](https://fastapi.tiangolo.com/)** | Guarde pra **depois** da fase 5. Se um dia quiser evoluir pra API, já has base. |

## 5) Dicas for Aprender Mais and Melhorar Rápido

- **Aprenda fazendo, explique depois.** Depois of terminar uma função, tente explicar in voz alta (or escrevendo) the what ela faz. Se não conseguir explain simples, significa that ainda não entendeu.
- **IA as mentor, not as copiador.** Ao invés of "cria isso pra mim", use: *"Por que esse código funciona?"*, *"Como eu poderia refatorar isso?"* or *"Me mostre um exemplo menor pra eu entender"*. Isso te força a pensar and te dá autonomia.
- **Commits diários.** Mesmo that seja só "ajusta função de movimentação". Isso cria um histórico limpo and shows evolução no GitHub.
- **Foque in "resolver", not in "perfeito".** Melhor ter something funcional hoje and refatorar amanhã, do que ficar 2 dias tentando deixar perfeito and não avançar.
- **Pense in "história".** When olhar seu repositório, um recrutador precisa conseguir entender: *"Problema -> Solção -> Evolução"*. Esse projeto já conta essa história naturally por causa da IC.
- **Teste with dados reais-simulados.** Quanto mais variado seu `data_simulada/` for (nomes estranhos, extensões diferentes), mais you vai aprender a tratar erros.
- **Documentar enquanto aprende.** Seu `anotacoes.md` vai be ouro daqui uns meses. Você vai esquecer coisas and esse arquivo vai te salvar.

## 6) Checklist Final (Portfólio + IC)

Quando chegar no final, confira isso antes of apresentar tanto pro orientador quanto pro LinkedIn.

- [ ] **MVP da IC:** Organiza arquivos, pastas and planilhas conforme proposto no PDF.
- [ ] **Código limpo:** Modularizado, with classes, tipagem and logs.
- [ ] **Histórico:** Salvo no SQLite with data, origem, destino and categoria.
- [ ] **IA aplicada:** Classificação por conteúdo + busca em linguagem natural funcionando.
- [ ] **CLI functional:** Roda with poucos comandos and bem intuitivo.
- [ ] **README completo:** With objetivo, prints "antes/depois", instalação, uso and tecnologias.
- [ ] **Git organized:** Commits claros, `.gitignore` correto and repositório público.
- [ ] **Teste do zero:** Rodou tudo in uma pasta vazia simulada sem erros.
- [ ] **Explicável:** Consegue explain todo the fluxo do projeto sem ler linha por linha.

## Recomendação Final

**Não troque esse projeto por outro. Expanda ele.**

Sua maior vantagem agora é exatamente essa: você has a problema real pra resolver, has 3h diárias and has a objetivo claro. Seguindo esse plano na ordem, you vai matar **duas coisas ao mesmo tempo**: entregar sua Iniciação Científica with qualidade and construir a **projeto âncora** do seu portfólio para sua primeira vaga of **Dev Júnior Python**.

**Regra of ouro:** *Qualidade > Quantidade. Termine esse projeto well feito, ao invés of começar 5 pela metade.*
