from Dictation import Dictation
from GetWord import GetWord
from GenerateList import GenerateList

if __name__ == "__main__":   
    
    getWord = GetWord();
    getWord.getWords();

    generateList = GenerateList();
    generateList.getMyWord();
    generateList.generate();

    dictation = Dictation();
    dictation.getMyWord();
    dictation.playSound();