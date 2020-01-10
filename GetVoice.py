import os
import urllib.request


class youdao():
    def __init__(self, type=0, word='hello'):
        '''
        youdao API
        type = 0：US
        type = 1：EN
        '''
        word = word.lower()  
        self._type = type  
        self._word = word  

        # root
        self._dirRoot = os.path.dirname(os.path.abspath(__file__))
        if 0 == self._type:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_US')  # US
        else:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_EN')  # EN

        # if US is exist
        if not os.path.exists('Speech_US'):
            os.makedirs('Speech_US')
        if not os.path.exists('Speech_EN'):
            os.makedirs('Speech_EN')

    def setAccent(self, type=0):
        '''
        type = 0：US
        type = 1：EN
        '''
        self._type = type

        if 0 == self._type:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_US')
        else:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_EN')

    def getAccent(self):
        return self._type

    def down(self, word, accent):
        self.setAccent(accent)
        word = word.lower()
        tmp = self._getWordMp3FilePath(word)
        if tmp is None:
            self._getURL()
            urllib.request.urlretrieve(self._url, filename=self._filePath)
            print('%s.mp3 done' % self._word)
        else:
            print('%s.mp3 exist, no need to download' % self._word)
        
        return self._filePath

    def _getURL(self):
        self._url = r'http://dict.youdao.com/dictvoice?type=' + str(
            self._type) + r'&audio=' + self._word

    def _getWordMp3FilePath(self, word):
        word = word.lower()
        self._word = word
        self._fileName = self._word + '.mp3'
        self._filePath = os.path.join(self._dirSpeech, self._fileName)

        if os.path.exists(self._filePath):
            return self._filePath
        else:
            return None


if __name__ == "__main__":

    getVoice = youdao()
    getVoice.down('hello')