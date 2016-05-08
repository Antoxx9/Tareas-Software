#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime

class recarga():  
    
    def __init__(self,monto,anio,mes,dia,idEst):
        self.monto = monto
        self.fecha = datetime.datetime(anio,mes,dia,0,0,0)
        self.idEst = idEst
        
class consumo():
    
    def __init__(self,monto,anio,mes,dia,idRes):
        self.monto = monto
        self.fecha = datetime.datetime(anio,mes,dia,0,0,0)
        self.idRes = idRes
        
        
class billeteraElectronica():
    
    def __init__(self,identificador,nombres,apellidos,ci,pin):
        self.id = identificador
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.pin = pin
        self.recargas = []
        self.consumos = []
        self.saldo = 0
        
    def getSaldo(self):
        return self.saldo
    
    def recargar(self,recarga):
        if(recarga.monto > 0):
            self.recargas.append(recarga)
            self.saldo += recarga.monto
            return 0
        else:
            return -1
        
    def consumir(self,debito):
        if(consumo.monto > 0):
            self.consumos.append(recarga)
            self.saldo -= consumo.monto
            return 0
        else:
            return -1