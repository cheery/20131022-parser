class SourceLocation(object):
    def __init__(self, path, index, line, column):
        self.path = path
        self.index = index
        self.line = line
        self.column = column

    def __repr__(self):
        return "%s:%i:%i" % (self.path, self.line, self.column)
