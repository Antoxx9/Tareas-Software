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
    totalPago = 0
    entrada = tiempoDeTrabajo[0]
    salida = tiempoDeTrabajo[1]
    tiempoTotal = salida - entrada
    diasTrabajo = tiempoTotal.days
    horasTrabajo = tiempoTotal.days*24 + tiempoTotal.seconds//3600
    segundosTrabajo = tiempoTotal.seconds
    diaInicio = entrada.weekday()
    diaFin = salida.weekday()
    if(segundosTrabajo % 3600 > 0):
        horasTrabajo += 1
    if(diaInicio == 4 and diaFin == 0):
        horasTrabajo += 1
        
    if(diasTrabajo == 0 and segundosTrabajo < 900):
        print("El tiempo de trabajo fue menor a 15 minutos.")
        return -1
    elif(diasTrabajo > 7):
        print("El tiempo de trabajo fue mayor a 7 dias")
        return -1
    elif(((diaInicio == 4 and diaFin == 5) or
          (diaInicio == 6 and diaFin == 0)) and horasTrabajo == 1):
        if(diaInicio == 5 or diaInicio == 6):
            totalPago += tarifa.weekend
        else:
            totalPago += tarifa.normal
        if(diaFin == 5 or diaFin == 6):
            totalPago += tarifa.weekend
        else:
            totalPago += tarifa.normal
    else:
        if(entrada.day == salida.day):
            if(diaInicio == 5 or diaInicio == 6):
                totalPago += decimal.Decimal(horasTrabajo*tarifa.weekend)
            else:
                totalPago += decimal.Decimal(horasTrabajo*tarifa.normal)
        else:
            if(diaInicio == 5 or diaInicio == 6):
                totalPago += decimal.Decimal((24-entrada.hour)*tarifa.weekend)
            else:
                totalPago += decimal.Decimal((24-entrada.hour)*tarifa.normal)
            horasRestantes = horasTrabajo
            horasRestantes -= (24-entrada.hour)
    
            if(diaInicio == 6):
                diaActual = 0
            else:
                diaActual = diaInicio + 1
            if(horasRestantes < 24 and horasRestantes > 0):
                diasRestantes = 1
            else:
                diasRestantes = math.ceil(horasRestantes/24)
                
            while(diasRestantes > 0):
                if(diasRestantes == 1):
                    if(diaActual == 5 or diaActual == 6):
                        totalPago += decimal.Decimal(horasRestantes*tarifa.weekend)
                    else:
                        totalPago += decimal.Decimal(horasRestantes*tarifa.normal)
                else:
                    horasRestantes -= 24
                    if(diaActual == 5 or diaActual == 6):
                        totalPago += decimal.Decimal(24*tarifa.weekend)
                    else:
                        totalPago += decimal.Decimal(24*tarifa.normal)
                        
                if(diaActual == 6):
                    diaActual = 0
                else:
                    diaActual += 1
                                
                diasRestantes -= 1
    return totalPago
