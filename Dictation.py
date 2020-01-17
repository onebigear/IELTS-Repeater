from playsound import playsound
import time
import os
import random
import platform

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
        if platform.system().lower() == 'windows':
            os_slash = '\\'
        else:
            os_slash = '/'
        for word in self.wordList:
            accent = random.randint(0, 100)
            if accent%2 == 0:
                soundPath = "Speech_US" + os_slash
            else:
                soundPath = "Speech_EN" + os_slash
            soundPath += str(word)+".mp3"
            print(str(accent%2))
            playsound(soundPath)
            time.sleep(3);

if __name__ == "__main__": 
    dictation = Dictation();
    dictation.getMyWord();
    dictation.playSound();
