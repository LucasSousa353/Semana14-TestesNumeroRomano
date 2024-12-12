import unittest

def converte(numeroEmRomano):
    tabela = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    acumulador = 0
    ultimovizinhodireita = 0
    for i in reversed(range(len(numeroEmRomano))):
        atual = 0
        numCorrente = numeroEmRomano[i]
        if numCorrente in tabela:
            atual = tabela[numCorrente]

        multiplicador = 1
        if atual < ultimovizinhodireita:
            multiplicador = -1

        acumulador += atual * multiplicador
        ultimovizinhodireita = atual

    return acumulador

class TestConverteNumerosRomanos(unittest.TestCase):
    
    def testes_atividade(self):
        self.assertEqual(converte("I"),1)
        self.assertEqual(converte("V"),5)
        self.assertEqual(converte("II"),2)
        self.assertEqual(converte("XXII"),22)
        self.assertEqual(converte("IX"),9)
        self.assertEqual(converte("XXIV"),24)

    def test_simples(self):
        self.assertEqual(converte("I"), 1)
        self.assertEqual(converte("V"), 5)
        self.assertEqual(converte("X"), 10)
        self.assertEqual(converte("L"), 50)
        self.assertEqual(converte("C"), 100)
        self.assertEqual(converte("D"), 500)
        self.assertEqual(converte("M"), 1000)

    def test_combinacoes(self):
        self.assertEqual(converte("II"), 2)
        self.assertEqual(converte("IV"), 4)
        self.assertEqual(converte("IX"), 9)
        self.assertEqual(converte("XL"), 40)
        self.assertEqual(converte("XC"), 90)
        self.assertEqual(converte("CD"), 400)
        self.assertEqual(converte("CM"), 900)

    def test_numeros_maiores(self):
        self.assertEqual(converte("MCMXCIV"), 1994)
        self.assertEqual(converte("MMXXIV"), 2024)
        self.assertEqual(converte("MMMCMXCIX"), 3999)

if __name__ == "__main__":
    unittest.main()
