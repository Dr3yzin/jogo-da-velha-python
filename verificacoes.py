def verificar(matriz):
    if matriz[0][0] == matriz[0][1] and matriz[0][1] == matriz[0][2]:
        return matriz[0][0]

    if matriz[1][0] == matriz[1][1] and matriz[1][1] == matriz[1][2]:
        return matriz[1][0]

    if matriz[2][0] == matriz[2][1] and matriz[2][1] == matriz[2][2]:
        return matriz[2][0]

    if matriz[0][0] == matriz[1][0] and matriz[1][0] == matriz[2][0]:
        return matriz[0][0]

    if matriz[0][1] == matriz[1][1] and matriz[1][1] == matriz[2][1]:
        return matriz[0][1]

    if matriz[0][2] == matriz[1][2] and matriz[1][2] == matriz[2][2]:
        return matriz[0][2]

    if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] or matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0]:
        return matriz[1][1]

    return 0
