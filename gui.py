import tkinter as tk
from tkinter import ttk
import functionality as fw
import functionality
from app import MetaVacFiles,wordTransferBetweenTwoFiles
import random
import os 

'''
    TODO:
        Functionality:
            - add new words 
            - choose "Do You Know  This Words"
            - Check new text on known and unknown words
            - add description
            - learn words 
            - print Word 
            - show Words Base
            - edit Word in Words Base

    Structer of Words Base
        - Known
        - Unknown
        - Learning

        
    Structer of word:
        - Part of speech
        - Short description
        - Examples
        - Synonyms
        - Antonyms
        - Russian Translation
        META:
            - KNOWN ->TRUE/FALSE
            - INLEARN -> TRUE/FALSE if  KNOWN: FALSE
            - LASTREPET:NONE -> TIME
            - NEXTREPET:NONE -> LASTREPET + TIME
            
        
    FRAMES:
        MAIN:
            LEARN->Button->Change frame on LEARNINGFRAME
            ADD->Button-> reveal extra frame ADDWORD
            SHOWVACABULARY -> Change frame on VACABULARY

        ADDWORD:

        SHOWVACABULARY:
'''
class Word:
    def __init__(self,meta,word = None,words_set=functionality.get_vacabulary_list(str(os.getcwd())+'\\files\\words_1.txt')) -> None:
        self.word = word
        self.word_set = words_set
        if self.word == None:
            self.word = random.choice(self.word_set)
            self.word_set.remove(self.word)
        self.meta = meta

    


    def nextWord(self):
        self.word = random.choice(self.word_set)
        self.word_set.remove(self.word)
        meta.updateSizes()


if __name__ == "__main__":
    
    def print_contents(self,event):
        print("Hi. The current entry content is:", self.contents.get())

        
    def changeLabel(root,word,l):
        
        l["text"] = word
        l.pack()
        
        
    

    root = tk.Tk()
    root.geometry("300x300")
    meta = MetaVacFiles()
    # functionality.fillWordsBaseIfItEmpty()
    word = Word(meta=meta)


    l = tk.Label(root, text=word.word,font=100,padx=15,pady=15)
    b1 = tk.Button(root, text = "Known",command=lambda:[wordTransferBetweenTwoFiles(meta.unchecked,meta.known,word.word),word.nextWord(),changeLabel(root,word.word,l)])
    b2 = tk.Button(root, text = "Unknown",command=lambda:[wordTransferBetweenTwoFiles(meta.unchecked,meta.unknown,word.word),word.nextWord(),changeLabel(root,word.word,l)])
    b3 = tk.Button(root, text = "Delete",command= lambda:[wordTransferBetweenTwoFiles(meta.unchecked,meta.trash,word.word),word.nextWord(),changeLabel(root,word.word,l)])
    b4 = tk.Button(root, text = "EXIT", command=root.destroy)
    b5 = tk.Button(root, text = "RESET FILES",command=lambda:meta.resetFiles())
    next = tk.Button(root,text= 'NEXT WORD',command=lambda:changeLabel(root,word,l))
    l.pack()

    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    b5.pack()
    next.pack()
    tk.mainloop()