import unittest
from StringIO import StringIO
from character_stream import EOFError
import parser

class TestParser(unittest.TestCase):
    def test_simple(self):
        sexpr = parser.parse(StringIO("hello 5"))
        self.assertEquals(sexpr[0].string, 'hello')
        self.assertEquals(sexpr[1].string, '5')

    def test_linenum(self):
        sexpr = parser.parse(StringIO("hello world"))
        self.assertEquals(sexpr[0].string, 'hello')
        self.assertEquals(sexpr[0].start, 0)
        self.assertEquals(sexpr[0].stop,  5)
        self.assertEquals(sexpr[1].string, 'world')
        self.assertEquals(sexpr[1].start, 6)
        self.assertEquals(sexpr[1].stop,  11)

if __name__=='__main__':
    unittest.main()
