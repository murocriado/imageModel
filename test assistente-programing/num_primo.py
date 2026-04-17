"""Solicita um número ao usuário e verifica se ele é primo."""


def eh_primo(n: int) -> bool:
    """Retorna True se n for primo, caso contrário False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    max_divisor = int(n**0.5)
    for divisor in range(3, max_divisor + 1, 2):
        if n % divisor == 0:
            return False
    return True


def solicitar_numero_do_usuario() -> None:
    entrada = input("Digite um número inteiro: ")
    try:
        numero = int(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return

    resultado = eh_primo(numero)
    mensagem = 'primo' if resultado else 'não primo'
    print(f"{numero} é {mensagem}.")


def main() -> None:
    solicitar_numero_do_usuario()


if __name__ == '__main__':
    main()
