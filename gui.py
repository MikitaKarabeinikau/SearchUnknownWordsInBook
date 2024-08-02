import tkinter as tk
from tkinter import ttk
import functionality as fw
import functionality
from app import MetaVacFiles,wordTransferBetweenTwoFiles
import random

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


class App(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents =  tk.StringVar()
        self.contents.set("This is variable")
        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>',self.print_contents)
        

    def print_contents(self,event):
        print("Hi. The current entry content is:", self.contents.get())

# root = Tk()
# frm = ttk.Frame(root,padding=100)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0,row=0)
# ttk.Button(frm,text="Quit", command=root.destroy).grid(column=1,row=0)


if __name__ == "__main__":
    # root.mainloop()
    # btn = ttk.Button(frm)
    # print(btn.configure.keys())
    # cnt = 0
    # def next_word():
    #         cnt+=1
        
        
    # window = tk.Tk()

    # frameright =tk.Frame(master=window,width=200,height=500)
    # frameright.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)
    
    # frameleft =tk.Frame(master=window,width=200,height=500,bg="blue")
    # frameleft.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

    # framemidle =tk.Frame(master=window,width=500,height=500,bg="red")
    # framemidle.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

    # btn = tk.Button(master=frameright,text="right",command=next_word)
    # btn.pack()
    
    # btn.bind("Next Word",next_word)
    # arr = fw.get_vacabulary_list()

    # lbl = tk.Label(master=framemidle,text=arr[cnt])
    # lbl.pack()

    # window.mainloop()

    root = tk.Tk()
    root.geometry("300x300")
    meta = MetaVacFiles()
    # functionality.fillWordsBaseIfItEmpty()
    words = functionality.get_vacabulary_list('words_1.txt')
    randWord = random.choice(words)

    l = tk.Label(root, text=randWord)
    b1 = tk.Button(root, text = "Known",command=wordTransferBetweenTwoFiles(meta.unchecked,meta.known,randWord))
    b2 = tk.Button(root, text = "Unknown")
    b3 = tk.Button(root, text = "Delete")
    b4 = tk.Button(root, text = "EXIT", command=root.destroy)

    l.pack()
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    tk.mainloop()