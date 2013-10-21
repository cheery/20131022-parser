from lexemes import BeginList, EndList, Variable, String, Integer
from character_stream import CharacterStream, EOFError

class MissingParenthesis(Exception):
    pass

class IncompleteString(Exception):
    pass

class TokenStream(object):
    def __init__(self, stream):
        self.stream = CharacterStream(stream)
        self.paren_count = 0
        self.eof = False
        self.adv()

    def get(self):
        return self.token

    def adv(self):
        if self.eof and self.paren_count > 0:
            raise MissingParenthesis("right")
        if self.eof:
            raise EOFError()
        stream = self.stream
        while stream.get().isspace():
            stream.adv()
        string = stream.get()
        if string == '(':
            self.token = BeginList()
            self.paren_count += 1
            try:
                stream.adv()
            except EOFError, e:
                self.eof = True
        elif string == ')':
            if self.paren_count <= 0:
                raise MissingParenthesis("left")
            self.token = EndList()
            self.paren_count -= 1
            try:
                stream.adv()
            except EOFError, e:
                self.eof = True
        elif string.isalpha():
            try:
                string = ''
                while stream.get().isalnum() or stream.get() == '_':
                    string += stream.get()
                    stream.adv()
            except EOFError, e:
                self.eof = True
            self.token = Variable(string)
        elif string.isdigit():
            try:
                string = ''
                while stream.get().isdigit():
                    string += stream.get()
                    stream.adv()
            except EOFError, e:
                self.eof = True
            self.token = Integer(string)
        elif string == '"':
            string = ''
            stream.adv()
            try:
                while stream.get() != '"':
                    string += stream.get()
                    stream.adv()
            except EOFError, e:
                raise IncompleteString()
            try:
                stream.adv()
            except EOFError, e:
                self.eof = True
            self.token = String(string)
        else:
            raise Exception("unknown character %r" % string)
