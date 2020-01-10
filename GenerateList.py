import os
import random
class GenerateList():
    def __init__(self):
        self.wordList = []
        self._dirRoot = os.path.dirname(os.path.abspath(__file__))

    def getMyWord(self):
        file_object = open('words.txt')
        try:
            text_line = file_object.readlines()
            for line in text_line:
                line=line.strip('\n')
                self.wordList.extend(line.split(" "))
        finally:
            file_object.close()

    def generate(self):
        random.shuffle(self.wordList)
        file = open('newWordList.txt','w+')
        index = 0
        for word in self.wordList:
            index += 1
            file.write(str(word)+"\n");
            if index == 50 :
                break
        file.close()


if __name__ == "__main__": 
    generateList = GenerateList();
    generateList.getMyWord();
    generateList.generate();