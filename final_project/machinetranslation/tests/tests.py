import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(englishToFrench("sure"), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')    

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(frenchToEnglish("sure"), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') 
        
unittest.main()