import unittest
from StringIO import StringIO
from character_stream import EOFError
from lexer import TokenStream, MissingParenthesis, IncompleteString
from lexemes import BeginList, EndList, Variable, String, Integer

class TestTokenStream(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(EOFError):
            TokenStream(StringIO(''))

    def test_list(self):
        stream = TokenStream(StringIO("()"))
        lexeme = stream.get()
        self.assertTrue(isinstance(lexeme, BeginList))
        stream.adv()
        lexeme = stream.get()
        self.assertTrue(isinstance(lexeme, EndList))

    def test_digit(self):
        lexeme = TokenStream(StringIO("15")).get()
        self.assertTrue(isinstance(lexeme, Integer))
        self.assertEqual(lexeme.string, "15")

    def test_variable(self):
        lexeme = TokenStream(StringIO("foo_bar")).get()
        self.assertTrue(isinstance(lexeme, Variable))
        self.assertEqual(lexeme.string, "foo_bar")

    def test_string(self):
        lexeme = TokenStream(StringIO('"hello world"')).get()
        self.assertTrue(isinstance(lexeme, String))
        self.assertEqual(lexeme.string, "hello world")

    def test_badstring(self):
        with self.assertRaises(IncompleteString):
            stream = TokenStream(StringIO('"bad string'))

    def test_noparen(self):
        with self.assertRaises(MissingParenthesis):
            stream = TokenStream(StringIO(')'))
        with self.assertRaises(MissingParenthesis):
            stream = TokenStream(StringIO('(()'))
            stream.adv()
            stream.adv()
            stream.adv()
            stream.adv()
            stream.adv()
        
    def test_usage(self):
        stream = TokenStream(StringIO('abc("def")guux"ball"aba5 7  '))
        self.assertTrue(isinstance(stream.get(), Variable))
        self.assertEqual(stream.get().string, 'abc')
        stream.adv()
        self.assertTrue(isinstance(stream.get(), BeginList))
        stream.adv()
        self.assertTrue(isinstance(stream.get(), String))
        self.assertEqual(stream.get().string, 'def')
        stream.adv()
        self.assertTrue(isinstance(stream.get(), EndList))
        stream.adv()
        self.assertTrue(isinstance(stream.get(), Variable))
        self.assertEqual(stream.get().string, 'guux')
        stream.adv()
        self.assertTrue(isinstance(stream.get(), String))
        self.assertEqual(stream.get().string, 'ball')
        stream.adv()
        self.assertTrue(isinstance(stream.get(), Variable))
        self.assertEqual(stream.get().string, 'aba5')
        stream.adv()
        self.assertTrue(isinstance(stream.get(), Integer))
        self.assertEqual(stream.get().string, '7')
        with self.assertRaises(EOFError):
            stream.adv()

if __name__=='__main__':
    unittest.main()
