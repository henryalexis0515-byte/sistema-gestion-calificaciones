def calcular_promedio(notas):
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía")

    for nota in notas:
        if nota < 0 or nota > 5:
            raise ValueError("Las notas deben estar entre 0 y 5")

    return sum(notas) / len(notas)


def determinar_estado(promedio):
    if promedio < 0 or promedio > 5:
        raise ValueError("El promedio debe estar entre 0 y 5")

    if promedio >= 3:
        return "Aprobado"
    else:
        return "Reprobado"