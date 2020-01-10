from playsound import playsound
import time
import os
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
            soundPath = "Speech_US\\"+str(word)+".mp3"
            playsound(soundPath)
            time.sleep(5);

if __name__ == "__main__": 
    dictation = Dictation();
    dictation.getMyWord();
    dictation.playSound();
