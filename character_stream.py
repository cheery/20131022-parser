from source_location import SourceLocation

class EOFError(Exception):
    pass

class CharacterStream(object):
    def __init__(self, stream, path=None):
        self.stream = stream
        self.path = path
        self.index = -1
        self.line = 1
        self.column = 0
        self.adv()

    def get_source_location(self):
        return SourceLocation(self.path, self.index, self.line, self.column)

    def get(self):
        return self.ch

    def adv(self):
        self.ch = self.stream.read(1)
        self.index += 1
        self.column += 1
        if self.ch == '\n':
            self.line += 1
            self.column = 0
        if self.ch == '':
            raise EOFError()
