# Explicação — Debug com IA

## Código com bugs (versão original)

```python
def calcular_media_bugada(notas)
    total = 0
    for i in range(len(notas) + 1):
        total = total + notas[i]
    media = total / len(notas)
    return media
```

---

## Bugs encontrados

### Bug 1 — Erro de sintaxe (`SyntaxError`)

**Linha:** `def calcular_media_bugada(notas)`

**Problema:** Falta o `:` (dois pontos) ao final da definição da função.

**Por que ocorre:** Em Python, toda estrutura de bloco (`def`, `if`, `for`, `while`, `class`) obrigatoriamente termina com `:`. A ausência impede que o interpretador reconheça o início do bloco.

**Correção:**
```python
# Errado
def calcular_media_bugada(notas)

# Correto
def calcular_media_bugada(notas):
```

---

### Bug 2 — Erro de índice (`IndexError`)

**Linha:** `for i in range(len(notas) + 1)`

**Problema:** O `+ 1` faz o loop tentar acessar `notas[len(notas)]`, que não existe.

**Por que ocorre:** Os índices de uma lista em Python vão de `0` até `len(lista) - 1`. Ao usar `range(len(notas) + 1)`, a última iteração tenta acessar um índice inexistente, lançando `IndexError: list index out of range`.

**Exemplo:**
```
notas = [8.0, 7.0, 9.0]  → índices válidos: 0, 1, 2
range(len(notas) + 1)    → gera: 0, 1, 2, 3  ← índice 3 não existe!
```

**Correção:**
```python
# Errado
for i in range(len(notas) + 1):

# Correto
for i in range(len(notas)):

# Ainda melhor — sem indexação manual
total = sum(notas)
```

---

## Código corrigido e melhorado

```python
def calcular_media(notas: list[float]) -> float:
    if not notas:
        return 0.0
    return sum(notas) / len(notas)
```

### O que mudou

| Problema | Correção aplicada |
|----------|-------------------|
| Falta de `:` na definição | Adicionado `:` após os parêmetros |
| `range(len(notas) + 1)` | Substituído por `sum()` nativo |
| Divisão por zero potencial | Guarda `if not notas` adicionado |
| Ausência de type hints | Adicionados `list[float]` e `-> float` |

---

## Lição aprendida

Erros de indexação manual são uma das causas mais comuns de bugs em Python. A solução é preferir sempre as funções nativas (`sum`, `max`, `min`, `enumerate`) e a iteração direta (`for item in lista`) ao invés de `range(len(...))`.
