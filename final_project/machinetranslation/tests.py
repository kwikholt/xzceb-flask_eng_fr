import unittest
from translation import english_to_french,french_to_english
class TestTranslateEnglishFrench(unittest.TestCase):

    def test_translate_Hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_empty_sting(self):
        self.assertEqual(english_to_french(''), '')
    def test_no_argument(self):
        self.assertEqual(english_to_french(),'')


class TestTranslateFrenchEnglish(unittest.TestCase):
    def test_translate_Bonjour(self):
         self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_empty_sting(self):
        self.assertEqual(french_to_english(''), '')
    def test_no_argument(self):
        self.assertEqual(french_to_english(),'')

if __name__ == '__main__':
    unittest.main()