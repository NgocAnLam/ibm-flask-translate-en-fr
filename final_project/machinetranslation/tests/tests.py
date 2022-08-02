import unittest

from translator import englishToFrench, frenchToEnglish


class TestEnToFr(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench(""), "Chaîne vide")


class TestFrToEn(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish(""), "Empty String")


if __name__ == '__main__':
    unittest.main()
