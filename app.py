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
                print
                add_new_words(self.unchecked,words)
            else:
                with open(i,'w') as file:
                    file.write('') 
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
            with open(i,'r'):
                sizes.append(len(get_vacabulary_list(i)))
        return sizes
    
    def sizeOfFiles(self):
        print(f'Known:{self.sizes[0]} -- Unknown: {self.sizes[1]} -- Trash: {self.sizes[2]} -- Unchecked: {self.sizes[3]}')
    
    def updateSizes(self):
        self.size = self.get_sizes()


if __name__ == "__main__":
    meta = MetaVacFiles()
    meta.sizeOfFiles()
    while True:
        meta.sizeOfFiles()
        if keyboard.read_key() == 'esc':
            break
        # Take words
        try:
            vac_list = get_vacabulary_list(meta.unchecked)
        except Exception as e:
            print(e)
        #Choose random word
        word = random.choice(vac_list)
        print(word)
        #Do you know this words
        #If know -> to Known else unknow 
        newFilePass = {
            "y" : add_new_words(meta.known,word),
            "n" : add_new_words(meta.unknown,word),
            "d" : add_new_words(meta.unchecked,word),
            "r" : meta.resetFiles()
        }
        print(f'Do you know this word :{word}\n y/n/d  ')
        if keyboard.read_key() in newFilePass.keys():

            newFilePass[keyboard.read_key()]
            #Update first file
            vac_list.remove(word)
            with open(meta.unchecked,'w') as file:
                file.writelines(vac_list)
            meta.updateSizes()
            meta.sizeOfFiles()
        else: print("Unknown command")