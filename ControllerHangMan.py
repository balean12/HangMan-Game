from random import randint
class Controller():
    def __init__(self, sentences):
         self._sentences = sentences
         self.idx = 0
         self.idx2= 0

    def addSentence(self, sentence):
        sentence_list = sentence.split(" ")
        if len(sentence_list) == 1:
            raise ValueError("Sentence too short!")
        for word in sentence_list:
            if len(word) < 2:
                raise ValueError("Words too short")
        self._sentences.add(sentence)
    def getSentence(self):
        x = randint(0, int(len(self._sentences.getAll()))-1)
        self.idx = x
        return self._sentences.getAll()[x]

    def createTheUnderScoreCopy(self, sentence):
        modifying = sentence
        # k=0
        # for letter in modifying:
        #     if letter == " ":
        #         k+=1
        # if k==0:
        #     raise ValueError("Sentence hasn't enough words!")
        checkLetters = str(modifying[0]) + str(modifying[len(modifying) - 1])
        for i in range(1, len(modifying)):
            if modifying[i] == " " and modifying[i - 1] not in checkLetters:
                checkLetters = checkLetters + modifying[i - 1]
            if modifying[i] == " " and modifying[i + 1] not in checkLetters:
                checkLetters = checkLetters + modifying[i + 1]
        for i in range(1, len(modifying) - 1):
            if modifying[i] not in checkLetters and modifying[i] != " ":
                new = list(modifying)
                new[i] = "_"
                modifying = "".join(new)
            continue
        return modifying

    def checkLetter(self, letter, sentence, sentencewithunder):
        hang = [" h","a","n","g"]
        ok = False
        if letter < "a" or letter > "z":
            raise ValueError("Only lowercase letters allowed!")
        #sentenceWithUnder = self.createTheUnderScoreCopy(sentence)
        #sentence = self._sentences.getAll()[self.idx]
        for j in range(0, len(sentence)-1):
            if sentence[j] == letter:
                new = list(sentencewithunder)
                new[j] = letter
                sentencewithunder = "".join(new)
                ok = True
        if ok == False:
            sentencewithunder = sentencewithunder + hang[self.idx2]
            self.idx2+=1
        return sentencewithunder

# baba = Controller(["anna goes", "sdau merges"])
# try:
#     print (baba.checkLetter("v"))
# except ValueError as ve:
#     print(str(ve))



