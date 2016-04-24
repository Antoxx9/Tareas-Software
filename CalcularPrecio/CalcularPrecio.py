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
        self.normal = nm
        self.weekend = wk

def calcularPrecio(tarifa,tiempoDeTrabajo):
    total_pago = 0
    entrada = tiempoDeTrabajo[0]
    salida = tiempoDeTrabajo[1]
    tiempo_total = salida - entrada
    dias_estadia = tiempo_total.days
    horas_estadia = tiempo_total.days*24 + tiempo_total.seconds//3600
    segundos_estadia = tiempo_total.seconds
    
    if(segundos_estadia % 3600 > 0):
        horas_estadia += 1
        
    #print("El tiempo total de estadia es de: ")
    #print(tiempo_total)
    #print("Las horas de estadia son de: " + str(horas_estadia))
    
    if(dias_estadia == 0 and segundos_estadia < 950):
        print("El tiempo de trabajo fue menor a 15 minutos.")
        return -1
    elif(dias_estadia > 7):
        print("El tiempo de trabajo fue mayor a 7 dias")
        return -1
    else:
        dia_entrada = entrada.weekday()
        if(dia_entrada == 5 or dia_entrada == 6):
            total_pago += decimal.Decimal((24-entrada.hour)*tarifa.weekend)
        else:
            total_pago += decimal.Decimal((24-entrada.hour)*tarifa.normal)
        horas_restantes = horas_estadia
        horas_restantes -= (24-entrada.hour)
        '''
        La duda esta aca, como yo al principio sumo lo del dia que llegue para
        luego sumar los dias restantes, con esta formula obtengo siempre cuantos
        dias quedan sin tomar en cuenta cuando llegue no?
        '''
        if(dia_entrada == 6):
            dia_actual = 0
        else:
            dia_actual = dia_entrada + 1
        if(horas_restantes < 24 and horas_restantes > 0):
            dias_restantes = 1
        else:
            dias_restantes = math.ceil(horas_restantes/24)
            
        while(dias_restantes > 0):
            #print("Quedan " + str(dias_restantes) + " dias")
            #print("Quedan " + str(horas_restantes) + " horas")
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
