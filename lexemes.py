class Lexeme(object):
    start = -1
    stop  = -1

    def __repr__(self):
        name = self.__class__.__name__
        return "%s[%i:%i]" % (name, self.start, self.stop)

class BeginList(Lexeme):
    pass

class EndList(Lexeme):
    pass

class StringLexeme(Lexeme):
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return Lexeme.__repr__(self) + repr(self.string)

class Variable(StringLexeme):
    pass

class String(StringLexeme):
    pass

class Integer(StringLexeme):
    pass
