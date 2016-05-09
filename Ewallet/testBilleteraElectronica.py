'''
Created on 09/5/2016

Autores:    Anthony El Kareh,     carnet 12-11075
            Guillermo Betancourt, carnet 11-10103
'''
import unittest
from billeteraElectronica import *

class billeteraElectronicaTester(unittest.TestCase):
    
    def testRecargaUnicaPinCorrecto(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(500,2016,2,23,1221)
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.getSaldo(), 500)
        
    def testRecargaConsumoCorrecto(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(500,2016,2,23,1221)
        miConsumo = consumo(300,2016,2,24,1221,5555)
        miBilletera.recargar(miRecarga)
        miBilletera.consumir(miConsumo)
        self.assertEquals(miBilletera.getSaldo(), 200)
        
    def testConsumoMayorQueRecarga(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(500,2016,2,23,1221)
        miConsumo = consumo(600,2016,2,24,1221,5555)
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.consumir(miConsumo), -1)
        self.assertEquals(miBilletera.getSaldo(), 500)

    def testRecargaNegativa(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(-1,2016,2,23,1221)
        self.assertEquals(miBilletera.recargar(miRecarga), -1)
        self.assertEquals(miBilletera.getSaldo(), 0)
        
    def testConsumoNegativo(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(500,2016,2,23,1221)
        miConsumo = consumo(-1,2016,2,24,1221,5555)
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.consumir(miConsumo), -1)
        self.assertEquals(miBilletera.getSaldo(), 500)

    def testConsumoPinIncorrecto(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(500,2016,2,23,1221)
        miConsumo = consumo(300,2016,2,24,1221,1111)
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.consumir(miConsumo), -1)
        self.assertEquals(miBilletera.getSaldo(), 500)
    
    def testRecargaConsumoVarios(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        saldo = miBilletera.getSaldo()
        misRecargas = [recarga(500,2016,2,23,1221),
                       recarga(20,2016,2,23,2332),
                       recarga(35,2016,2,23,3443),
                       recarga(340,2016,2,23,4554)]
        misConsumos = [consumo(10,2016,2,24,1001,5554),
                       consumo(225,2016,2,24,2002,5555),
                       consumo(700,2016,2,24,3003,5555),
                       consumo(10,2016,2,24,4004,5551)]
        consumoEfectivo = []
        for i in range(4):
            miBilletera.recargar(misRecargas[i])
            saldo += misRecargas[i].monto
            self.assertEquals(miBilletera.getSaldo(), saldo)
        for i in range(4):
            consumoEfectivo.append(miBilletera.consumir(misConsumos[i]))
            if consumoEfectivo[i] == 0:
                self.assertEquals(miBilletera.getSaldo(), saldo - misConsumos[i].monto)
            else:
                self.assertEquals(consumoEfectivo[i], -1)
        self.assertEquals(miBilletera.getSaldo(), 670)
        
    def testRecargaConsumoNegativos(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(-1000,2016,2,23,1221)
        miConsumo = consumo(-300,2016,2,24,1221,1111)
        self.assertEquals(miBilletera.recargar(miRecarga), -1)
        self.assertEquals(miBilletera.consumir(miConsumo), -1)
        self.assertEquals(miBilletera.getSaldo(), 0)
    
    def testNombreApellidoCaracteresEspeciales(self):
        miBilletera = billeteraElectronica(12345, "Bárbara", "Ñato", 98765, 5555)
        self.assertEquals(miBilletera.nombres,"Bárbara")
        self.assertEquals(miBilletera.apellidos,"Ñato")
    
    def testRecargasDecimales(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(0.00001,2016,2,23,1001)
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.getSaldo(), 0.00001)
    
    def testRecargasConsumosDecimales(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(0.00001,2016,2,23,1001)
        miConsumo = consumo(0.000001,2016,2,24,4554,5555)
        miBilletera.recargar(miRecarga)
        miBilletera.consumir(miConsumo)
        self.assertEquals(miBilletera.getSaldo(), 0.000009)
    
    def testRecargaMaxInt(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(2147483647,2016,2,23,1001)
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.getSaldo(), 2147483647)
        
    def testRecargaConsumoTotal(self):
        miBilletera = billeteraElectronica(12345, "Guillermo", "Betancourt", 98765, 5555)
        miRecarga = recarga(500,2016,2,23,1001)
        miConsumo = consumo(500,2016,2,24,4554,5555)
        self.assertEquals(miRecarga.monto, 500)
        self.assertEquals(miConsumo, 500)
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.getSaldo(), 500)
        miBilletera.consumir(miConsumo)
        self.assertEquals(miBilletera.getSaldo(), 0)