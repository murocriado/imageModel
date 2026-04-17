# Explicação da refatoração para `refatoracao.py`

O código em `refatoracao.py` calcula estatísticas básicas sobre uma lista de números: total, média, maior valor e menor valor.

## O que o código faz

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

- A função `c` percorre a lista `l` duas vezes.
- Na primeira passagem, calcula a soma total `t` dos elementos.
- Em seguida, calcula a média `m` dividindo `t` pelo tamanho da lista.
- Depois, inicia `mx` e `mn` com o primeiro elemento e percorre a lista novamente para encontrar o maior e o menor valor.
- Por fim, retorna uma tupla com `t`, `m`, `mx` e `mn`.
- O código principal define `x`, chama `c(x)` e imprime os resultados.

## Pontos de refatoração aplicados ou recomendados

1. Nomes de função e variáveis mais descritivos:
   - `c` → `calcular_estatisticas`
   - `l` → `numeros` ou `valores`
   - `t` → `total`
   - `m` → `media`
   - `mx` → `maior_valor`
   - `mn` → `menor_valor`
   - `a`, `b`, `c2`, `d` → use nomes que indiquem o que representam.

2. Evitar redundância e melhorar legibilidade:
   - Use `for numero in numeros:` em vez de `for i in range(len(l)):`.
   - Use `sum(numeros)`, `max(numeros)` e `min(numeros)` quando possível.
   - Calcule a média apenas depois de obter a soma.

3. Separar responsabilidades:
   - A função deve apenas calcular e retornar valores.
   - Imprimir os resultados deve ser feito fora da função.

4. Evitar sobrescrever nomes de funções ou builtins:
   - A letra `c` é um nome pouco claro e pode ser confundida com outros símbolos.
   - Use nomes completos para deixar o código mais fácil de entender.

## Benefícios da refatoração

- Código mais legível e fácil de manter.
- Menos chances de erro ao entender o propósito das variáveis.
- Facilita testes unitários quando a lógica de cálculo está isolada.
- Reduz duplicação de loops e torna o código mais expressivo.

## Exemplo de refatoração ideal

Uma versão refatorada poderia ser:

```python
def calcular_estatisticas(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    maior_valor = max(numeros)
    menor_valor = min(numeros)
    return total, media, maior_valor, menor_valor

valores = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

soma, media, maior, menor = calcular_estatisticas(valores)
print("total:", soma)
print("media:", media)
print("maior:", maior)
print("menor:", menor)
```

Essa refatoração mantém o comportamento, mas melhora a clareza e a estrutura do código.