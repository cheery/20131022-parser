class EOFError(Exception):
    pass

class CharacterStream(object):
    def __init__(self, stream):
        self.stream = stream
        self.adv()

    def get(self):
        return self.ch

    def adv(self):
        self.ch = self.stream.read(1)
        if self.ch == '':
            raise EOFError()
