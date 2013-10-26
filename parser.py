from character_stream import EOFError
from lexer import TokenStream, MissingParenthesis, IncompleteString
from lexemes import BeginList, EndList, Variable, String, Integer

def parse_list(stream):
    lst = []
    assert isinstance(stream.get(), BeginList)
    stream.adv()
    while not isinstance(stream.get(), EndList):
        lst.append(parse_sexpr(stream))
        stream.adv()

def parse_sexpr(stream):
    current = stream.get()
    if isinstance(current, BeginList):
        return parse_list(stream)
    if isinstance(current, Variable):
        return current
    if isinstance(current, String):
        return current
    if isinstance(current, Integer):
        return current

def parse(stream, path=None):
    output = []
    try:
        stream = TokenStream(stream, path)
        while True:
            output.append(parse_sexpr(stream))
            stream.adv()
    except EOFError, e:
        pass
    return output
