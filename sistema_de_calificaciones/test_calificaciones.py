import unittest
from calificaciones import calcular_promedio, determinar_estado


class TestCalificaciones(unittest.TestCase):

    def test_calcular_promedio_correcto(self):
        notas = [4.0, 3.5, 4.5]
        resultado = calcular_promedio(notas)
        self.assertEqual(resultado, 4.0)

    def test_determinar_estado_aprobado(self):
        resultado = determinar_estado(3.8)
        self.assertEqual(resultado, "Aprobado")

    def test_nota_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            calcular_promedio([4.0, 6.0, 3.5])


if __name__ == "__main__":
    unittest.main()