from functionality import *
import random
import keyboard
import os 

'''
 TODO:
    #RESET ALL FILES
    
'''


def wordTransferBetweenTwoFiles(frm, to, word):
        meta = MetaVacFiles()
        oldVac = get_vacabulary_list(frm)
        try:
            oldVac.remove(word)
        except Exception as e:
            print(e)
        createNewWordsFile(oldVac,frm)
        add_new_words(to,word)
        meta.updateSizes()
        
        print(f'Word {word} was added to {to} and removed from {frm}')
        meta.sizeOfFiles()



class MetaVacFiles():
    def __init__(self) -> None:
        self.known = str(os.getcwd())+'\\files\\known.txt'
        self.unknown = str(os.getcwd())+'\\files\\unknown.txt'
        self.trash = str(os.getcwd())+'\\files\\tash.txt'
        self.unchecked = str(os.getcwd())+'\\files\\words_1.txt'
        self.files = [self.known,self.unknown,self.trash,self.unchecked]
        self.checkOnExistens()
        self.sizes = self.get_sizes()

    def resetFiles(self):
        for i in self.files:
            if i == self.unchecked:
                words = get_words_from_book(str(os.getcwd() + '\\books\\The_Murders_in_the_Rue_Morgue-Edgar_Allan_Poe.txt'))
                createNewWordsFile(words,self.unchecked)
            else:
                with open(i,'w') as file:
                    file.write('') 
        print(f'FILES WERE RESETED!')
        self.sizeOfFiles()



    def checkOnExistens(self):
        for file in self.files:
            if  os.path.exists(file):
                print(f'File {file} exists')
            else:
                with open(file,'w'):
                    print(f'File {file} was created!')
                    continue

    def get_sizes(self):
        sizes = []
        for i in self.files:
            sizes.append(len(get_vacabulary_list(i)))
        return sizes
    
    def sizeOfFiles(self):
        print(f'Known:{self.sizes[0]} -- Unknown: {self.sizes[1]} -- Trash: {self.sizes[2]} -- Unchecked: {self.sizes[3]}')
    
    def updateSizes(self):
        self.size = self.get_sizes()


if __name__ == "__main__":
    meta = MetaVacFiles()
    meta.resetFiles()
    meta.sizeOfFiles()