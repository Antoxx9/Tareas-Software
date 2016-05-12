'''
Created on 09/5/2016

Autores:    Anthony El Kareh,     carnet 12-11075
            Guillermo Betancourt, carnet 11-10103
'''
import unittest
from billeteraElectronica import *

class billeteraElectronicaTester(unittest.TestCase):
    
    decimal.getcontext().prec = 15

    # Caso recarga correcta
    def testRecargaUnicaPinCorrecto(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(500,"1221")
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(500))
    
    # Caso recarga y consumo correcto
    def testRecargaConsumoCorrecto(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(500,"1221")
        miConsumo = consumo(300,"1221","5555")
        miBilletera.recargar(miRecarga)
        miBilletera.consumir(miConsumo)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(200))
    
    # Caso malicioso, consumo mayor que recarga    
    def testConsumoMayorQueRecarga(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(500,"1221")
        miConsumo = consumo(600,"1221","5555")
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.consumir(miConsumo), -1)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(500))

    # Caso frontera, recarga negativa
    def testRecargaNegativa(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(-1,"1221")
        self.assertEquals(miBilletera.recargar(miRecarga), -1)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(0))
    
    # Caso frontera, consumo negativo
    def testConsumoNegativo(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(500,"1221")
        miConsumo = consumo(-1,"1221","5555")
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.consumir(miConsumo), -1)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(500))

    # Caso pin incorrecto
    def testConsumoPinIncorrecto(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(500,"1221")
        miConsumo = consumo(300,"1221","1111")
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.consumir(miConsumo), -1)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(500))
    
    # Caso recargas y consumos varios
    def testRecargaConsumoVarios(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        saldo = miBilletera.getSaldo()
        misRecargas = [recarga(500,"1221"),
                       recarga(20,"2332"),
                       recarga(35,"3443"),
                       recarga(340,"4554")]
        misConsumos = [consumo(10,"1001","5554"),
                       consumo(225,"2002","5555"),
                       consumo(700,"3003","5555"),
                       consumo(10,"4004","5551")]
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
        
    # Caso esquina, recargas y consumos negativos
    def testRecargaConsumoNegativos(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(-1000,"1221")
        miConsumo = consumo(-300,"1221","1111")
        self.assertEquals(miBilletera.recargar(miRecarga), -1)
        self.assertEquals(miBilletera.consumir(miConsumo), -1)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(0))
    
    # Caso esquina, nombre y apellido con caracteres especiales
    def testNombreApellidoCaracteresEspeciales(self):
        miBilletera = billeteraElectronica("12345", "Bárbara", "Ñato", 98765, "5555")
        self.assertEquals(miBilletera.nombres,"Bárbara")
        self.assertEquals(miBilletera.apellidos,"Ñato")
    
    # Caso frontera, recarga con decimales pequeños
    def testRecargasDecimales(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga("0.00001","1001")
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal("0.00001"))
    
    # Caso esquina, recargas y consumos con decimales pequeños
    def testRecargasConsumosDecimales(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga("0.00001","1001")
        miConsumo = consumo("0.000001","4554","5555")
        miBilletera.recargar(miRecarga)
        miBilletera.consumir(miConsumo)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal("0.00001") - decimal.Decimal("0.000001"))
    
    # Caso frontera, recarga con el máximo entero (32 bits)
    def testRecargaMaxInt(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(2147483647,"1001")
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(2147483647))
        
    # Caso frontera, recarga y consumo total
    def testRecargaConsumoTotal(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(500,"1001")
        miConsumo = consumo(500,"4554","5555")
        self.assertEquals(miRecarga.monto, decimal.Decimal(500))
        self.assertEquals(miConsumo.monto, decimal.Decimal(500))
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(500))
        miBilletera.consumir(miConsumo)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(0))
        
    # Caso recarga entera y consumo decimal
    def testRecargaIntConsumirDecimal(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(500,"1001")
        miConsumo = consumo("499.999998","4554","5555")
        self.assertEquals(miRecarga.monto, decimal.Decimal(500))
        self.assertEquals(miConsumo.monto, decimal.Decimal("499.999998"))
        miBilletera.recargar(miRecarga)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(500))
        miBilletera.consumir(miConsumo)
        self.assertEquals(miBilletera.getSaldo(), decimal.Decimal(500)- decimal.Decimal("499.999998"))
    
    # Caso verificación de fechas
    def testFechasRecargaConsumo(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 98765, "5555")
        miRecarga = recarga(500,"1001")
        miConsumo = consumo("499.999998","4554","5555")
        self.assertLess(miRecarga.fecha,miConsumo.fecha)
        miBilletera.recargar(miRecarga)
        miBilletera.consumir(miConsumo)
    
    # Caso esquina, inicialización incorrecta de las instanciaciones de clases
    def testVerificacionInstanciacionClases(self):
        miBilletera = billeteraElectronica("12345", "Guillermo", "Betancourt", 'a', "5555")
        miRecarga = recarga('b',"1001")
        miConsumo = consumo("499.999998","4554",-1)
        
        self.assertEquals(miBilletera.getSaldo(), None)
        self.assertEquals(miBilletera.nombres, None)
        self.assertEquals(miBilletera.apellidos, None)
        self.assertEquals(miBilletera.ci, None)
        self.assertEquals(miBilletera.pin, None)
        
        self.assertEquals(miRecarga.monto, None)
        self.assertEquals(miRecarga.idEst, None)
        
        self.assertEquals(miConsumo.monto, None)
        self.assertEquals(miConsumo.idRes, None)
        self.assertEquals(miConsumo.pin, None)

        