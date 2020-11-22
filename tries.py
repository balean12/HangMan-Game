# import unittest
# from ControllerHangMan import Controller
# class Teste(unittest.TestCase):
#     def setUp(self):
#         self.sentences = Controller(["anna has apples", "marta has gems"])
#     def test_Createetcetc(self):
#         self.assertEqual(self.sentences[0], "anna has apples")
#
modifying = "anna han apples and goes"
checkLetters = str(modifying[0]) + str(modifying[len(modifying)-1])
for i in range(1, len(modifying)):
    if modifying[i] == " " and modifying[i-1] not in checkLetters:
        checkLetters = checkLetters + modifying[i-1]
    if modifying[i] == " " and modifying[i+1] not in checkLetters:
        checkLetters = checkLetters + modifying[i + 1]
for i in range(1, len(modifying)-1):
      if modifying[i] not in checkLetters and modifying[i] != " ":
          new = list(modifying)
          new[i]= "_"
          modifying = "".join(new)
      continue
print (modifying)
print (checkLetters)

