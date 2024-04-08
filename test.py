import unittest
from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = Palindrome.is_palindrome('a')
        self.assertEqual(resultado, True)
    
    def test_b(self):
        resultado = Palindrome.is_palindrome('B')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = Palindrome.is_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = Palindrome.is_palindrome('ab')
        self.assertEqual(resultado, False)
    
    def test_aCa(self):
        resultado = Palindrome.is_palindrome('aCa')
        self.assertEqual(resultado, True)

    def test_aCs(self):
        resultado = Palindrome.is_palindrome('aCs')
        self.assertEqual(resultado, False)

    def test_ABBA(self):
        resultado = Palindrome.is_palindrome('ABBA')
        self.assertEqual(resultado, True)

    def test_ABCA(self):
        resultado = Palindrome.is_palindrome('BACB')
        self.assertEqual(resultado, False)

    def test_ABCBA(self):
        resultado = Palindrome.is_palindrome('ABCBA')
        self.assertEqual(resultado, True)

    def test_ABCCBA(self):
        resultado = Palindrome.is_palindrome('ABCCBA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA(self):
        resultado = Palindrome.is_palindrome('ZBCCBA')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = Palindrome.is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_neuqueM(self):
        resultado = Palindrome.is_palindrome('neuqueM')
        self.assertEqual(resultado, False)

    def test_neuqueN(self):
        resultado = Palindrome.is_palindrome('neuqueN')
        self.assertEqual(resultado,True)
        
    def test_neu_quen(self):
        resultado = Palindrome.is_palindrome('neu quen')
        self.assertEqual(resultado,True)

    def test_neu_q_ueN(self):
        resultado = Palindrome.is_palindrome('neu q uen')
        self.assertEqual(resultado,True)

    def test_anita_lava_la_tina(self):
        resultado = Palindrome.is_palindrome('anita lava la tina')
        self.assertEqual(resultado,True)



if __name__ == '__main__':
    unittest.main()