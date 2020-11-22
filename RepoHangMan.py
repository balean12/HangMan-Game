class Repo(object):
    def __init__(self):
        self._entities = []

    def add(self, value):
        if value in self._entities:
            raise RepoError("Sentence Already Given!\n")
        self._entities.append(value)
    def getAll(self):
        return self._entities[:]

class ValidError(Exception):
    pass

class RepoError(Exception):
    pass

class SentenceTextFileRepo(Repo):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._readFromFile()

    def _readFromFile(self):
        try:
            f = open(self._filename, "r")
            line = f.readline().strip()
            while line!= "":
                super().add(line)
                line = f.readline().strip()
            f.close()

        except IOError as e:
            print("An error occured - " + str(e))
            raise e


    def add(self, object):
        super().add(object)
        self._writeToFile()

    def _writeToFile(self):
        try:
            f = open(self._filename, "w")
            listaProp = super().getAll()
            for element in listaProp:
                f.write(str(element) + "\n")
            f.close()
        except IOError:
            raise RepoError("Error writing")