"""
Ejemplo educativo del algoritmo del banquero.
Ejecutar con: python algoritmo_banquero.py
"""

def estado_seguro(disponible, asignacion, necesidad):
    n = len(asignacion)
    trabajo = disponible[:]
    terminado = [False] * n
    secuencia = []

    progreso = True
    while progreso:
        progreso = False
        for i in range(n):
            if not terminado[i] and all(
                necesidad[i][j] <= trabajo[j]
                for j in range(len(disponible))
            ):
                trabajo = [
                    trabajo[j] + asignacion[i][j]
                    for j in range(len(disponible))
                ]
                terminado[i] = True
                secuencia.append(f"P{i}")
                progreso = True

    return all(terminado), secuencia


if __name__ == "__main__":
    disponible = [3, 3, 2]
    asignacion = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],
    ]
    maximo = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3],
    ]
    necesidad = [
        [maximo[i][j] - asignacion[i][j] for j in range(3)]
        for i in range(5)
    ]

    seguro, secuencia = estado_seguro(disponible, asignacion, necesidad)
    if seguro:
        print("ESTADO SEGURO")
        print("Secuencia posible:", " -> ".join(secuencia))
    else:
        print("ESTADO NO SEGURO")
