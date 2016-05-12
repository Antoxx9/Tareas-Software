#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import decimal

class recarga():  
    
    def __init__(self,monto,idEst):
        decimal.getcontext().prec = 15
        try:
            assert(type(idEst) is str)
            assert(decimal.Decimal(monto))
            
            self.monto = decimal.Decimal(monto)
            self.fecha = datetime.datetime.now()
            self.idEst = idEst
        except:
            print("Ocurrió un error al hacer una recarga")
            self.monto = None
            self.fecha = None
            self.idEst = None

        
class consumo():
    
    def __init__(self,monto,idRes,pin):
        decimal.getcontext().prec = 15
        try:
            assert(type(pin) is str)
            assert(type(idRes) is str)
            assert(decimal.Decimal(monto))
            
            self.monto = decimal.Decimal(monto)
            self.fecha = datetime.datetime.now()
            self.idRes = idRes
            self.pin = pin
        except:
            print("Ocurrió un error al hacer un consumo")
            self.monto = None
            self.fecha = None
            self.idRes = None
            self.pin = None
        
        
class billeteraElectronica():
    
    def __init__(self,identificador,nombres,apellidos,ci,pin):
        decimal.getcontext().prec = 15
        try:
            assert(type(identificador) is str)
            assert(type(nombres) is str)
            assert(type(apellidos) is str)
            assert(type(ci) is int)
            assert(type(pin) is str)
            
            self.id = identificador
            self.nombres = nombres
            self.apellidos = apellidos
            self.ci = ci
            self.pin = pin
            self.recargas = []
            self.consumos = []
            self.saldo = decimal.Decimal(0)            
        except:
            print("Ocurrió un error al crear la billetera virtual")
            self.id = None
            self.nombres = None
            self.apellidos = None
            self.ci = None
            self.pin = None
            self.recargas = None
            self.consumos = None
            self.saldo = None
        
    def getSaldo(self):
        return self.saldo
    
    def recargar(self,recarga):
        if(recarga.monto > 0):
            self.recargas.append(recarga)
            self.saldo += decimal.Decimal(recarga.monto)
            return 0
        else:
            return -1
        
    def consumir(self,consumo):
        if(consumo.monto >= 0 and self.saldo >= consumo.monto and self.pin == consumo.pin):
            self.consumos.append(consumo)
            self.saldo -= decimal.Decimal(consumo.monto)
            return 0
        else:
            return -1