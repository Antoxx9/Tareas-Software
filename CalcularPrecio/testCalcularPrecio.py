'''
Created on 23/4/2016

@author: usuario
'''
import unittest
from CalcularPrecio import*


class Test(unittest.TestCase):

    def test_entrar_y_salir_mismo_dia(self):
        entrada = datetime.datetime(2016,5,20,15,54,0)
        salida = datetime.datetime(2016,5,20,23,59,0)
        tarifa_actual = tarifa(1.5,5.4)
        tiempo_trabajo = [entrada,salida]
        self.assertEquals(calcularPrecio(tarifa_actual, tiempo_trabajo),13.5)

    def test_entrar_y_salir_distinto_dia(self):
        entrada = datetime.datetime(2016,4,20,15,54,0)
        salida = datetime.datetime(2016,4,21,15,59,0)
        tarifa_actual = tarifa(1.5,5.4)
        tiempo_trabajo = [entrada,salida]
        self.assertEquals(calcularPrecio(tarifa_actual, tiempo_trabajo),37.5)

    def test_entrar_y_salir_fin_de_semana(self):
        entrada = datetime.datetime(2016,4,22,15,54,0)
        salida = datetime.datetime(2016,4,23,15,59,0)
        tarifa_actual = tarifa(1.5,5.4)
        tiempo_trabajo = [entrada,salida]
        self.assertEquals(calcularPrecio(tarifa_actual, tiempo_trabajo),99.9)
        
    def test_estar_una_semana(self):
        entrada = datetime.datetime(2016,4,22,15,54,0)
        salida = datetime.datetime(2016,4,29,15,54,0)
        tarifa_actual = tarifa(1.5,5.4)
        tiempo_trabajo = [entrada,salida]
        self.assertEquals(calcularPrecio(tarifa_actual, tiempo_trabajo),439.2)

    def test_estar_mas_de_siete_dias(self):
        entrada = datetime.datetime(2016,4,22,15,54,0)
        salida = datetime.datetime(2016,4,30,15,54,0)
        tarifa_actual = tarifa(1.5,5.4)
        tiempo_trabajo = [entrada,salida]
        self.assertEquals(calcularPrecio(tarifa_actual, tiempo_trabajo),-1)
        
    def test_estar_menos_de_quince_minutos(self):
        entrada = datetime.datetime(2016,4,22,15,30,0)
        salida = datetime.datetime(2016,4,22,15,44,0)
        tarifa_actual = tarifa(1.5,5.4)
        tiempo_trabajo = [entrada,salida]
        self.assertEquals(calcularPrecio(tarifa_actual, tiempo_trabajo),-1)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()