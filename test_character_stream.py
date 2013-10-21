import unittest
from StringIO import StringIO
from character_stream import CharacterStream, EOFError

class TestCharacterStream(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(EOFError):
            CharacterStream(StringIO(''))

    def test_get_adv(self):
        stream = CharacterStream(StringIO("abcde\n"))
        self.assertEqual(stream.get(), stream.get())
        self.assertEqual(stream.get(), 'a')
        stream.adv()
        self.assertEqual(stream.get(), 'b')
        stream.adv()
        stream.adv()
        stream.adv()
        self.assertEqual(stream.get(), 'e')
        stream.adv()
        with self.assertRaises(EOFError):
            stream.adv()

if __name__=='__main__':
    unittest.main()
