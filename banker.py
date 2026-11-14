def _validate(available, allocation, maximum):
    if not isinstance(available, list) or not isinstance(allocation, list) or not isinstance(maximum, list):
        raise ValueError("Los datos deben ser listas.")
    if not allocation or len(allocation) != len(maximum):
        raise ValueError("Allocation y Maximum deben tener igual número de procesos.")
    resources = len(available)
    if resources == 0:
        raise ValueError("Debe existir al menos un recurso.")
    for row in allocation + maximum:
        if not isinstance(row, list) or len(row) != resources:
            raise ValueError("Todas las filas deben tener el mismo número de recursos.")
        if any(not isinstance(x, int) or x < 0 for x in row):
            raise ValueError("Los recursos deben ser enteros no negativos.")
    if any(not isinstance(x, int) or x < 0 for x in available):
        raise ValueError("Available debe contener enteros no negativos.")
    for i in range(len(allocation)):
        if any(allocation[i][j] > maximum[i][j] for j in range(resources)):
            raise ValueError("Allocation no puede superar Maximum.")
    return len(allocation), resources

def is_safe_state(available, allocation, maximum):
    n, m = _validate(available, allocation, maximum)
    need = [[maximum[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    work = available[:]
    finish = [False] * n
    sequence = []
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + allocation[i][j] for j in range(m)]
                finish[i] = True
                sequence.append(i)
                changed = True
    safe = all(finish)
    return {"safe": safe, "sequence": sequence if safe else [],
            "need": need, "message": "Estado seguro" if safe else "Estado inseguro"}

def request_resources(available, allocation, maximum, process, request):
    n, m = _validate(available, allocation, maximum)
    if not 0 <= process < n:
        raise ValueError("Índice de proceso fuera de rango.")
    if not isinstance(request, list) or len(request) != m:
        raise ValueError("Request debe tener un valor por recurso.")
    if any(not isinstance(x, int) or x < 0 for x in request):
        raise ValueError("Request debe contener enteros no negativos.")
    need = [maximum[process][j] - allocation[process][j] for j in range(m)]
    if any(request[j] > need[j] for j in range(m)):
        return {"granted": False, "message": "La petición supera la necesidad máxima del proceso."}
    if any(request[j] > available[j] for j in range(m)):
        return {"granted": False, "message": "No hay recursos disponibles suficientes."}
    new_available = [available[j] - request[j] for j in range(m)]
    new_allocation = [row[:] for row in allocation]
    new_allocation[process] = [new_allocation[process][j] + request[j] for j in range(m)]
    safety = is_safe_state(new_available, new_allocation, maximum)
    return {"granted": safety["safe"], "message": "Petición concedida: el estado sigue siendo seguro." if safety["safe"] else "Petición denegada: dejaría el sistema inseguro.",
            "safe": safety["safe"], "sequence": safety["sequence"],
            "available": new_available, "allocation": new_allocation}
