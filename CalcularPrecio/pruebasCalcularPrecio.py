'''
Created on 27/4/2016
Autores: Anthony El Kareh, Eliot Diaz
'''
import unittest
from CalcularPrecio import*

class CalcularPrecioTester(unittest.TestCase):
    
    def testTrabajoEnAnioBisiesto(self):
        entrada = datetime.datetime(2016,2,23,3,0,0)
        salida = datetime.datetime(2016,2,29,3,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(10,20)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 1920)
    
    def testTrabajoEnAnioNoBisiesto(self):
        entrada = datetime.datetime(2016,2,23,3,0,0)
        salida = datetime.datetime(2016,2,28,3,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(10,20)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 1470)

    def testTrabajoTiempoMinimo(self):
        entrada = datetime.datetime(2015,10,23,9,45,0)
        salida = datetime.datetime(2015,10,23,10,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(1,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 1)

    def testTrabajoTiempoMaximo(self):
        entrada = datetime.datetime(2015,8,23,15,0,0)
        salida = datetime.datetime(2015,8,30,15,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(1,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 216)

    def testTrabajoEnMinutosFrontera(self):
        entrada = datetime.datetime(2015,2,17,0,0,0)
        salida = datetime.datetime(2015,2,17,0,59,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(1,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 1)

    def testTrabajoEnHorasFrontera(self):
        entrada = datetime.datetime(2015,1,15,0,0,0)
        salida = datetime.datetime(2015,1,15,23,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(1,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 23)

    def testTrabajoDesdeMedianocheAMedianocheEnDiaDeSemana(self):
        entrada = datetime.datetime(2015,3,24,0,0,0)
        salida = datetime.datetime(2015,3,25,0,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(1,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 24)

    def testTrabajoDesdeMedianocheAMedianocheEnDiaDeFinDeSemana(self):
        entrada = datetime.datetime(2016,3,12,0,0,0)
        salida = datetime.datetime(2016,3,13,0,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(1,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 48)    

    def testTrabajoConTarifaMinimaEnDiaDeSemana(self):
        entrada = datetime.datetime(2016,4,13,12,0,0)
        salida = datetime.datetime(2016,4,13,13,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(0,2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 0)

    def testTrabajoConTarifaMinimaEnDiaDeFinDeSemana(self):
        entrada = datetime.datetime(2016,4,16,12,0,0)
        salida = datetime.datetime(2016,4,16,13,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(2,0)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 0)

    def testTrabajoConTarifaDecimalEnDiaSemana(self):
        entrada = datetime.datetime(2016,6,15,13,0,0)
        salida = datetime.datetime(2016,6,15,15,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(2.56,5)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 5.12)

    def testTrabajoConTarifaDecimalEnDiaDeFinDeSemana(self):
        entrada = datetime.datetime(2016,6,18,13,0,0)
        salida = datetime.datetime(2016,6,18,15,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(5,3.78)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 7.56)
        
    def testTrabajoConAmbasTarifaDecimal(self):
        entrada = datetime.datetime(2016,6,15,13,0,0)
        salida = datetime.datetime(2016,6,15,15,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(2.56,3.56)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 2*2.56)
        
    def testTrabajoConAmbasTarifaDecimalPrecisionCompleja(self):
        entrada = datetime.datetime(2016,6,15,13,0,0)
        salida = datetime.datetime(2016,6,15,15,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(2.123456789,3.987654321)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 2*2.123456789)
        
    def testTrabajoEntreDiasDeSemana(self):
        entrada = datetime.datetime(2016,8,6,20,0,0)
        salida = datetime.datetime(2016,8,7,4,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 8*4)
        
    def testTrabajoEntreMeses(self):
        entrada = datetime.datetime(2016,10,31,15,0,0)
        salida = datetime.datetime(2016,11,2,15,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 48*3)
        
    def testTrabajoEntreAnios(self):
        entrada = datetime.datetime(2016,12,31,9,0,0)
        salida = datetime.datetime(2017,1,1,9,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), 24*4)
        
    def testTrabajoEntreDiasDeSemanaYFinDeSemana(self):
        entrada = datetime.datetime(2016,4,29,23,59,0)
        salida = datetime.datetime(2016,4,30,0,14,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), (1*3)+(1*4))
        
    def testTrabajoDeViernesALunes(self):
        entrada = datetime.datetime(2016,5,13,23,45,0)
        salida = datetime.datetime(2016,5,16,0,15,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(3,4)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), (1*3)+(48*4)+(1*3))
        
    def testTrabajoConTarifaNegativaEnDiaDeSemana(self):
        entrada = datetime.datetime(2016,4,28,8,0,0)
        salida = datetime.datetime(2016,4,28,10,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(-6,9)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), -1)
        
    def testTrabajoConTarifaNegativaEnFinDeSemana(self):
        entrada = datetime.datetime(2016,4,9,8,0,0)
        salida = datetime.datetime(2016,4,9,10,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(6,-9)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), -1)
        
    def testTrabajoConTarifaCaracterEnDiaDeSemana(self):
        entrada = datetime.datetime(2016,4,28,8,0,0)
        salida = datetime.datetime(2016,4,28,10,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa("a",2)
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), -1)
        
    def testTrabajoConTarifaCaracterEnFinDeSemana(self):
        entrada = datetime.datetime(2016,4,9,8,0,0)
        salida = datetime.datetime(2016,4,9,10,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(2,"a")
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), -1)
        
    def testTrabajoConFechaEntradaMayorAFechaSalida(self):
        entrada = datetime.datetime(2016,7,8,0,0,0)
        salida = datetime.datetime(2016,7,7,0,0,0)
        tiempoDeTrabajo = [entrada, salida]
        tarifaActual = tarifa(2,"a")
        self.assertEquals(calcularPrecio(tarifaActual, tiempoDeTrabajo), -1)
        
if __name__ == '__main__':
    unittest.main()