from playsound import playsound
import time
import os
import random
# playsound("Speech_US\desert.mp3")
class Dictation():
    def __init__(self):
        self.wordList = []
        self._dirRoot = os.path.dirname(os.path.abspath(__file__))

    def getMyWord(self):
        file_object = open('newWordList.txt')
        try:
            text_line = file_object.readlines()
            for line in text_line:
                line=line.strip('\n')
                self.wordList.extend(line.split(" "))
        finally:
            file_object.close()
        
    def playSound(self):
        for word in self.wordList:
            accent = random.randint(0, 100)
            if accent%2 == 0:
                soundPath = "Speech_US\\"
            else:
                soundPath = "Speech_EN\\"
            soundPath += str(word)+".mp3"
            print(str(accent%2))
            playsound(soundPath)
            time.sleep(3);

if __name__ == "__main__": 
    dictation = Dictation();
    dictation.getMyWord();
    dictation.playSound();
