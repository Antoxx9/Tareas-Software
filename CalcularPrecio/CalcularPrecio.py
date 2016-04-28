'''
Created on 27/4/2016

Autores: Anthony El Kareh, Eliot Diaz
'''

import decimal
import math
import datetime
import sys

class tarifa():
    
    def __init__(self,nm,wk):
        if((type(nm) is int or type(nm) is float)
            and (type(wk) is int or type(wk) is float)):
            self.normal = decimal.Decimal(nm)
            self.weekend = decimal.Decimal(wk)
        else:
            self.normal = -1
            self.weekend = -1

def calcularPrecio(tarifa,tiempoDeTrabajo):
    if(tarifa.weekend < 0 or tarifa.normal < 0):
        return -1
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
    if(dia_inicio == 4 and dia_fin == 0):
        horas_trabajo += 1
        
    if(dias_trabajo == 0 and segundos_trabajo < 900):
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
        if(entrada.day == salida.day):
            if(dia_inicio == 5 or dia_inicio == 6):
                total_pago += decimal.Decimal(horas_trabajo*tarifa.weekend)
            else:
                total_pago += decimal.Decimal(horas_trabajo*tarifa.normal)
        else:
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
    return total_pago
