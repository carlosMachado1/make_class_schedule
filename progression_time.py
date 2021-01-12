def hour_progression(time: int):
    inicio = 420
    horarios = []
    continuar = True
    while continuar:
        hora = inicio // 60
        if hora < 10:
            if hora == 9:
                horario = "0{}:00 - {}:00".format(hora, hora + 1)
            else:
                horario = "0{}:00 - 0{}:00".format(hora, hora + 1)
        else:
            horario = "{}:00 - {}:00".format(hora, hora + 1)
        horarios.append(horario)
        inicio += time * 60
        if hora >= 21:
            continuar = False
    return horarios


'''
def minuts_progression(time: int):
    inicio = 420
    horarios = []
    continuar = True
    while continuar:
        hora = inicio // 60
        minuto = ((inicio / 60) - hora) * 60
        if hora < 10:
            if hora == 9:
                horario = "0{}:{} - {}:{}".format(hora, hora + 1)
            horario = "0{}:{}".format(hora, minuto)
        else:
            horario = "{}:{}".format(hora, minuto)
        horarios.append(horario)
        inicio += time * 60
    if hora > 24:
        continuar = False
    return horarios


horarios = hour_progression(1)
print(len(horarios))
for i in horarios:
    print(i)
'''
