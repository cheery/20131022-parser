class EOFError(Exception):
    pass

class CharacterStream(object):
    def __init__(self, stream):
        self.stream = stream
        self.index = -1
        self.adv()

    def get(self):
        return self.ch

    def adv(self):
        self.ch = self.stream.read(1)
        self.index += 1
        if self.ch == '':
            raise EOFError()
