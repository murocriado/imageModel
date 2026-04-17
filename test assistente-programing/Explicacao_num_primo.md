## Explicação linha por linha de num_primo.py

```python
"""Solicita um número ao usuário e verifica se ele é primo."""
```
- Comentário de documentação do arquivo (docstring do módulo).
- Serve para descrever o propósito geral do script ao pedir um número e verificar se ele é primo.

```python
def eh_primo(n: int) -> bool:
```
- Declara a função `eh_primo` que recebe um argumento `n` e retorna um valor booleano.
- O tipo `int` indica que a função espera um número inteiro.

```python
    """Retorna True se n for primo, caso contrário False."""
```
- Docstring da função.
- Explica o comportamento esperado de maneira clara e direta.

```python
    if n <= 1:
        return False
```
- Verifica os casos base.
- Números menores ou iguais a 1 não são primos.

```python
    if n <= 3:
        return True
```
- Trata `2` e `3` como casos especiais retornando `True`.
- Mantém o código simples para pequenos valores que são primos.

```python
    if n % 2 == 0:
        return False
```
- Descarta números pares maiores que 2 imediatamente.
- Isso reduz pela metade o conjunto de candidatos a divisores.

```python
    max_divisor = int(n**0.5)
```
- Calcula o maior divisor possível que precisa ser testado.
- Usar a raiz quadrada torna a verificação significativamente mais eficiente.

```python
    for divisor in range(3, max_divisor + 1, 2):
```
- Percorre apenas divisores ímpares a partir de 3.
- O passo `2` evita testar números pares, que já foram eliminados.

```python
        if n % divisor == 0:
            return False
```
- Verifica se `divisor` divide `n` completamente.
- Se encontrar um divisor, retorna `False` imediatamente.

```python
    return True
```
- Quando não há divisores até a raiz quadrada, `n` é primo.
- Retorna `True` no final da função.

```python
def solicitar_numero_do_usuario() -> None:
```
- Define a função que lê um número digitado pelo usuário.
- Separa a lógica de entrada do usuário da lógica de verificação.

```python
    entrada = input("Digite um número inteiro: ")
```
- Exibe uma mensagem solicitando ao usuário que digite um número.
- Recebe a entrada como texto.

```python
    try:
        numero = int(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return
```
- Converte a entrada para `int`.
- Mostra uma mensagem de erro se o valor não for um inteiro.

```python
    resultado = eh_primo(numero)
    mensagem = 'primo' if resultado else 'não primo'
    print(f"{numero} é {mensagem}.")
```
- Usa `eh_primo` para verificar se o número informado é primo.
- Mostra o resultado ao usuário em formato legível.

```python
def main() -> None:
    solicitar_numero_do_usuario()
```
- Define a função principal do programa.
- Mantém o ponto de entrada organizado.

```python
if __name__ == '__main__':
    main()
```
- Executa `main()` apenas quando o arquivo é usado como script.
- Permite importar `eh_primo` sem executar a solicitação de entrada automaticamente.

---

## Resumo técnico
- O código separa lógica de verificação (`eh_primo`) da leitura de entrada do usuário (`solicitar_numero_do_usuario`).
- Usa `input()` para solicitar um número inteiro ao usuário e `int()` para converter a entrada.
- Trata entradas inválidas com `ValueError` e exibe uma mensagem de erro amigável.
- O bloco `main()` melhora a estrutura e facilita manutenção futura.
