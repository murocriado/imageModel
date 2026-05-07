def calcular_media(notas: list[float]) -> float:
    """Calcula a média aritmética de uma lista de notas.

    Args:
        notas (list[float]): Lista com os valores das notas.

    Returns:
        float: Média aritmética das notas. Retorna 0.0 se a lista estiver vazia.
    """
    # Guarda contra divisão por zero: lista vazia não tem média definida
    if not notas:
        return 0.0

    # Usa sum() e len() ao invés de loop manual para manter o código idiomático
    return sum(notas) / len(notas)


def classificar_aluno(media: float) -> str:
    """Classifica o aluno com base na média calculada.

    Args:
        media (float): Média aritmética do aluno (esperado entre 0 e 10).

    Returns:
        str: Classificação textual: 'Aprovado', 'Recuperação' ou 'Reprovado'.
    """
    # O limite 7.0 define aprovação direta; abaixo disso entra em recuperação
    if media >= 7.0:
        return "Aprovado"

    # O limite 5.0 separa recuperação de reprovação direta
    if media >= 5.0:
        return "Recuperação"

    # Qualquer média abaixo de 5.0 representa reprovação
    return "Reprovado"


def exibir_resultado(nome: str, notas: list[float]) -> None:
    """Exibe no console o resumo do desempenho do aluno.

    Args:
        nome (str): Nome do aluno.
        notas (list[float]): Lista de notas do aluno.
    """
    media = calcular_media(notas)
    situacao = classificar_aluno(media)

    # Formata a média com duas casas decimais para padronizar a exibição
    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


# =============================================================================
# VERSÃO COM BUG (para fins didáticos — Debug com IA)
# =============================================================================
#
# ERRO ORIGINAL:
#   def calcular_media_bugada(notas)
#       total = 0
#       for i in range(len(notas) + 1):   # BUG: +1 causa IndexError
#           total = total + notas[i]
#       media = total / len(notas)
#       return media
#
# PROBLEMAS IDENTIFICADOS:
#   1. Falta os dois pontos ':' no final da definição da função (SyntaxError).
#   2. range(len(notas) + 1) ultrapassa o índice máximo válido (IndexError).
#
# CORREÇÃO APLICADA: a função calcular_media() acima usa sum() e len(),
# eliminando completamente a necessidade de indexação manual.
# =============================================================================


if __name__ == "__main__":
    exibir_resultado("Ana Silva", [8.5, 7.0, 9.0, 6.5])
    print()
    exibir_resultado("Carlos Lima", [4.0, 5.5, 4.5, 6.0])
    print()
    exibir_resultado("Beatriz Santos", [3.0, 2.5, 4.0, 3.5])
