import os
from GetVoice import youdao
class GetWord():
    def __init__(self):
        wordList = []
        self._dirRoot = os.path.dirname(os.path.abspath(__file__))

    def getWords(self):
        getVocie = youdao();
        file_object = open('words.txt')
        try:
            text_line = file_object.readlines()
            for line in text_line:
                line=line.strip('\n')
                wordList = line.split(" ")
                for i in range(0, len(wordList)):
                    getVocie.down(wordList[i])
        finally:
            file_object.close()
        
if __name__ == "__main__":   
    getWord = GetWord();
    getWord.getWords();