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
        sexpr = parser.parse(StringIO("hello world\n5"), '<scratch>')
        self.assertEquals(sexpr[0].string, 'hello')
        self.assertEquals(repr(sexpr[0].location), '<scratch>:1:1')
        self.assertEquals(sexpr[1].string, 'world')
        self.assertEquals(repr(sexpr[1].location), '<scratch>:1:7')
        self.assertEquals(sexpr[2].string, '5')
        self.assertEquals(repr(sexpr[2].location), '<scratch>:2:1')

if __name__=='__main__':
    unittest.main()
