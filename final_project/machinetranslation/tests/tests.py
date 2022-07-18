import unittest
from translator import english_to_french
from translator import french_to_english


class TestTranslatorE2F(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertIsNotNone(english_to_french('Hello'))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestTranslatorF2E(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertIsNotNone(french_to_english('Bonjour'))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()