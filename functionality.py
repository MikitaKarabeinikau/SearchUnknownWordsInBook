import os 
import random

'''
    What to do next? 
    TODO:
        - Make a Gui to print words
        - Comunication with user to separates known and unknown words
        - SEPARATES BY KNOWN AND UNKNOWN 

'''

TEST_FILE = str(os.getcwd() + '\\test.txt')


def inVacabulary(file,word):
    return True if word in get_arr_of_words(file) else False

def add_new_words(file,args):
    with open(file,'a') as f:
        for word in args:
            f.write(word + '\n')
            print(f'New word ->{word} added')


def add_to_vacabulary(wordsDict,filename):
      with open(filename,'+a',encoding='utf-8') as file:
        for number, word in enumerate(sorted(wordsDict.keys())):
            if word.isnumeric():
                print(f'Numeric -- {number}' )
            else:
                file.write(word + "\n")

def get_vacabulary_list(filename):
    with open(filename,'r') as file:
        words = []
        for row in file.readlines():
            words.append(row.strip())
        return words
    

#Find dir of book
def find_file(filename,search_path):
    for root, dir , files in os.walk(search_path):
        # print(f'{root} -- {dir} -- {files}')
        if filename in files:
            print(f'Book: {filename} was founded at :{dir} root: {root}')
            return os.path.join(root, filename)

    return  None

BOOK_NAME = find_file("Window.txt",os.getcwd())

def get_words_from_book(book):
    words = []
    puncs = ['\(','!','.',',','\'','\'','\"','?','`',';',':',"\[","\]",'/','•','-','—','“','”','\‘','\’','\(','\)',')','_','_','@','\(','\[','\(','\)','\]','#','*','%','$']
    with open(BOOK_NAME,'r',encoding="utf8",errors='ignore') as book:
        for row in book.readlines():
            if row == '\n': continue
            else:
                for punc in puncs:
                    row = row.strip()
                    row = row.replace(punc,' ')
                words.append(row.split(" "))
            
    lastArr=[]
    for i in range(0,len(words)):
        if len(words[i]) > 1:
            for x in range(0,len(words[i])):
                # print(red[i][x].issymbol())
                # print(f'i:{i} -- x:--{x}')
                if words[i][x] != '':
                    lastArr.append(words[i][x].lower())
        
        
    print(f'len:{len(lastArr)}')

    wordsDict = {}
    for word in lastArr:
        if word in wordsDict.keys():
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    print(wordsDict)
    print(len(wordsDict.keys()))
    print(sorted(wordsDict.keys()))
    return sorted(wordsDict.keys())
    # print(get_vacabulary_list(BOOK_NAME))
    # print(find_file('words.txt', os.getcwd()))

def print_file(file):
    with open(file,'r') as f:
        for line in f.readlines():
            print(line)

def delete_word_from_file(file, word_to_delete):
    with open(file,'r') as f:
        words = [word.strip() for word in f.readlines()]
        print(words)
        while (word_to_delete in words): 
            words.remove(word_to_delete)
    with open(file,'w+') as f:
        for word in words:
            f.write(word+ '\n') 
    return word_to_delete

def get_arr_of_words(file)-> list:
    with open(file,'r') as f:
        return [words.strip() for words in f.readlines()]

def get_N_random_words(N,file):
    arr = []
    for i in range (N):
        choosen_word = random.choice(get_arr_of_words("words.txt"))
        arr.append(choosen_word) if choosen_word not in arr else "Array contain choosen word "
        print(f'Random choosen words: {arr}')
    return arr

if __name__ == "__main__":
    add_new_words(str(os.getcwd()) + '\\words.txt',get_words_from_book(BOOK_NAME))
    
    

