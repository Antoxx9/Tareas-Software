'''
Created on 27/4/2016

Autores: Anthony El Kareh, Eliot Diaz
'''

import datetime
import decimal
import sys
import math

decimal.getcontext().prec = 6

class tarifa():
    
    def __init__(self,nm,wk):
        self.normal = decimal.Decimal(nm)
        self.weekend = decimal.Decimal(wk)

def calcularPrecio(tarifa,tiempoDeTrabajo):
    total_pago = 0
    entrada = tiempoDeTrabajo[0]
    salida = tiempoDeTrabajo[1]
    tiempo_total = salida - entrada
    dias_trabajo = tiempo_total.days
    horas_trabajo = tiempo_total.days*24 + tiempo_total.seconds//3600
    segundos_trabajo = tiempo_total.seconds
    dia_inicio = entrada.weekday()
    dia_fin = salida.weekday()
    if(segundos_trabajo % 3600 > 0):
        horas_trabajo += 1
    
    if(dias_trabajo == 0 and segundos_trabajo < 950):
        print("El tiempo de trabajo fue menor a 15 minutos.")
        return -1
    elif(dias_trabajo > 7):
        print("El tiempo de trabajo fue mayor a 7 dias")
        return -1
    elif(((dia_inicio == 4 and dia_fin == 5) or
          (dia_inicio == 6 and dia_fin == 0)) and horas_trabajo == 1):
        if(dia_inicio == 5 or dia_inicio == 6):
            total_pago += tarifa.weekend
        else:
            total_pago += tarifa.normal
        if(dia_fin == 5 or dia_fin == 6):
            total_pago += tarifa.weekend
        else:
            total_pago += tarifa.normal
    else:
        dia_inicio = entrada.weekday()
        if(dia_inicio == 5 or dia_inicio == 6):
            total_pago += decimal.Decimal((24-entrada.hour)*tarifa.weekend)
        else:
            total_pago += decimal.Decimal((24-entrada.hour)*tarifa.normal)
        horas_restantes = horas_trabajo
        horas_restantes -= (24-entrada.hour)

        if(dia_inicio == 6):
            dia_actual = 0
        else:
            dia_actual = dia_inicio + 1
        if(horas_restantes < 24 and horas_restantes > 0):
            dias_restantes = 1
        else:
            dias_restantes = math.ceil(horas_restantes/24)
            
        while(dias_restantes > 0):
            if(dias_restantes == 1):
                if(dia_actual == 5 or dia_actual == 6):
                    total_pago += decimal.Decimal(horas_restantes*tarifa.weekend)
                else:
                    total_pago += decimal.Decimal(horas_restantes*tarifa.normal)
            else:
                horas_restantes -= 24
                if(dia_actual == 5 or dia_actual == 6):
                    total_pago += decimal.Decimal(24*tarifa.weekend)
                else:
                    total_pago += decimal.Decimal(24*tarifa.normal)
                    
            if(dia_actual == 6):
                dia_actual = 0
            else:
                dia_actual += 1
                            
            dias_restantes -= 1
                
    print("El total a pagar es de: " + str(total_pago))
    return float(total_pago)
