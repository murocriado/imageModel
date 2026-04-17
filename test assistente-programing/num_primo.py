"""Solicita um número ao usuário e verifica se ele é primo."""

import math


def numero_eh_primo(numero: int) -> bool:
    """Retorna True se o número informado for primo."""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0:
        return False

    limite = math.isqrt(numero)
    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False

    return True


def obter_numero_inteiro() -> int | None:
    """Solicita ao usuário um número inteiro e retorna o valor convertido."""
    entrada = input("Digite um número inteiro: ")
    try:
        return int(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return None


def exibir_resultado(numero: int, eh_primo: bool) -> None:
    """Exibe o resultado da verificação de primalidade."""
    status = 'primo' if eh_primo else 'não primo'
    print(f"{numero} é {status}.")


def main() -> None:
    numero = obter_numero_inteiro()
    if numero is None:
        return

    resultado = numero_eh_primo(numero)
    exibir_resultado(numero, resultado)


if __name__ == '__main__':
    main()
