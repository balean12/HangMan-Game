from ControllerHangMan import Controller
from RepoHangMan import RepoError, SentenceTextFileRepo


class UI:
    def __init__(self, controller):
        self._controller = controller
        self.startgame = False

    def giveLetter(self, sentence, sentenceWithUnder):
        try:
            letter = input("Give Letter: ")
            return self._controller.checkLetter(letter, sentence, sentenceWithUnder)
        except ValueError as ve:
            print (str(ve))
    def takeCurrentSentence(self):
        sentence = self._controller.getSentence()
        return sentence

    def start(self):
        sentence = self.takeCurrentSentence()
        sentenceWithUnder = self._controller.createTheUnderScoreCopy(sentence)
        while not self.startgame:
            cmd = input("Choose 1 to Add a sentence. Choose 2 to play the game: ")
            if int(cmd) == 1:
                try:
                    sentence = input("Give Sentence (lowercase): ")
                    self._controller.addSentence(sentence)
                except RepoError as re:
                    print(str(re))
                except ValueError as ve:
                    print(str(ve))
            else:
                self.startgame = True
                self.run(sentence, sentenceWithUnder)

    def run(self, sentence, sentenceWithUnder):
        # sentence = self.takeCurrentSentence()
        # sentenceWithUnder = self._controller.createTheUnderScoreCopy(sentence)
        print (sentenceWithUnder)
        GameOver = False
        while not GameOver:
            sentenceWithUnder = self.giveLetter(sentence, sentenceWithUnder)
            print (sentenceWithUnder)
            if sentenceWithUnder[len(sentenceWithUnder)-1] == "g":
                GameOver = True
                print ("You Died!")
            elif "_" not in sentenceWithUnder:
                GameOver = True
                print ("You're a smartie")
            else:
                continue

repo = SentenceTextFileRepo("Sentences.txt")
controller = Controller(repo)
ui = UI(controller)
ui.start()

