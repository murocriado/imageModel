# teste-assistent-code

Repositório desenvolvido nas aulas de **Programação Assistida por Inteligência Artificial**, utilizando o **GitHub Copilot** integrado ao VS Code como assistente de código. O projeto reúne práticas de geração, explicação, refatoração, depuração e documentação de scripts Python.

---

## Estrutura do repositório

```
teste-assistent-code/
├── num_primos.py              ← Função que verifica se um número é primo (com docstring)
├── refatoracao.py             ← Código original e versão refatorada (com docstring)
├── debug.py                   ← Script com análise de bugs e versão corrigida (com comentários inline)
├── explicacao_num_primo.md    ← Explicação linha a linha + comparação de versões
├── explicacao-refatoracao.md  ← Análise dos problemas e melhorias aplicadas
├── explicacao-debug.md        ← Descrição dos bugs, causas e correções
└── README.md                  ← Este arquivo
```

> Na raiz do repositório há também um `index.html` com a aplicação publicada via GitHub Pages.

---

## Scripts Python

### `num_primos.py`

Implementa duas funções:

- `eh_primo(numero)` — verifica se um número inteiro é primo usando verificação até a raiz quadrada, com complexidade **O(√n)**.
- `listar_primos(limite)` — retorna todos os primos em um intervalo usando a função anterior.

**Como executar:**
```bash
python num_primos.py
```

**Saída esperada:**
```
29 é um número primo.

Primos até 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

### `refatoracao.py`

Demonstra o processo de refatoração de um código mal estruturado. O arquivo contém:

- O código original comentado (com os problemas preservados para comparação)
- A versão refatorada com boas práticas: nomes descritivos, iteração idiomática, `sum()` nativo e docstring completa.

**Como executar:**
```bash
python refatoracao.py
```

**Saída esperada:**
```
Entrada:       [1, 2, 3, 4, 5, 6]
Transformados: [2, 4, 4, 8, 6, 12]
Soma total:    36
```

---

### `debug.py`

Apresenta funções para cálculo de média e classificação de alunos, acompanhadas de comentários inline que explicam as decisões de lógica. O arquivo também documenta os bugs originais e as correções aplicadas.

**Como executar:**
```bash
python debug.py
```

**Saída esperada:**
```
Aluno: Ana Silva
Notas: [8.5, 7.0, 9.0, 6.5]
Média: 7.75
Situação: Aprovado

Aluno: Carlos Lima
Notas: [4.0, 5.5, 4.5, 6.0]
Média: 5.00
Situação: Recuperação

Aluno: Beatriz Santos
Notas: [3.0, 2.5, 4.0, 3.5]
Média: 3.25
Situação: Reprovado
```

---

## Arquivos de documentação

| Arquivo | Conteúdo |
|---------|----------|
| `explicacao_num_primo.md` | Análise linha a linha da função de primos, comparação entre versão inicial e otimizada, e tabela de desempenho |
| `explicacao-refatoracao.md` | Identificação dos anti-padrões no código original e tabela comparativa antes/depois |
| `explicacao-debug.md` | Descrição detalhada dos bugs (`SyntaxError` e `IndexError`), causas e correções aplicadas |

---

## Tecnologias e ferramentas utilizadas

| Ferramenta | Finalidade |
|------------|------------|
| **Python 3.11+** | Linguagem principal dos scripts |
| **GitHub Copilot** | Assistente de IA para geração, refatoração e documentação de código |
| **Visual Studio Code** | Editor com integração ao Copilot |
| **Git / GitHub** | Versionamento e hospedagem do repositório |
| **GitHub Pages** | Publicação da página web (`index.html`) |
| **Teachable Machine** | Treinamento do modelo de reconhecimento de padrões integrado ao `index.html` |

---

## Práticas realizadas

| Prática | Descrição |
|---------|-----------|
| **Prática 1 — IA como Copiloto** | Geração da função de primos, explicação linha a linha e otimização com clean code |
| **Prática 2 — Refatoração** | Reestruturação de código com nomes ruins, loops inadequados e sem documentação |
| **Prática 3 — Debug com IA** | Identificação e correção de `SyntaxError` e `IndexError` em código intencional com bugs |
| **Prática 4 — IA explicando código** | Explicação detalhada do código refatorado, validando a capacidade interpretativa da IA |

---

## Como clonar e executar

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Entrar na pasta
cd teste-assistent-code

# Executar qualquer script (Python 3.11+ necessário)
python num_primos.py
python refatoracao.py
python debug.py
```

---

## Autor

Desenvolvido como atividade prática da disciplina de Programação Assistida por IA.
