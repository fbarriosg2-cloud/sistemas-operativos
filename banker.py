def safe_sequence(available, allocation, need):
    """Determina si el estado es seguro y devuelve una secuencia segura."""
    work = available[:]
    n = len(allocation)
    finished = [False] * n
    sequence = []

    while len(sequence) < n:
        progress = False
        for p in range(n):
            if not finished[p] and all(need[p][j] <= work[j] for j in range(len(work))):
                work = [work[j] + allocation[p][j] for j in range(len(work))]
                finished[p] = True
                sequence.append(f"P{p}")
                progress = True
        if not progress:
            break

    return {"safe": len(sequence) == n, "sequence": sequence,
            "message": "Estado seguro" if len(sequence) == n else "Estado inseguro: no se encontró secuencia completa"}

def request_resources(available, allocation, need, request, process):
    p = int(process)
    if any(request[j] > need[p][j] for j in range(len(request))):
        return {"granted": False, "message": "Solicitud inválida: supera la necesidad declarada."}
    if any(request[j] > available[j] for j in range(len(request))):
        return {"granted": False, "message": "No se puede conceder: recursos insuficientes disponibles."}

    # Simular asignación provisional
    av = [available[j] - request[j] for j in range(len(request))]
    al = [row[:] for row in allocation]
    ne = [row[:] for row in need]
    al[p] = [al[p][j] + request[j] for j in range(len(request))]
    ne[p] = [ne[p][j] - request[j] for j in range(len(request))]
    check = safe_sequence(av, al, ne)
    if check["safe"]:
        return {"granted": True, "message": "Solicitud concedida: el estado sigue siendo seguro.",
                "sequence": check["sequence"]}
    return {"granted": False, "message": "Solicitud denegada: dejaría el sistema en estado inseguro."}
