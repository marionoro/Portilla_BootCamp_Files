# Python Code
# Creating a full inverted index (reference to document and location in document)
import os
import re
from multiprocessing import Pool

def insert_file(myfile):
    myfile = open(myfile, 'r')
    text = myfile.read()
    text = text.lower()
    text = re.findall("[^!;.?,\" —:\n]+", text)
    return text

def word_location(word_list):
    mydict = {}
    for i in range(len(word_list)):
        if word_list[i] in mydict.keys():
            mydict[word_list[i]].append(i)
        else:
            mydict[word_list[i]] = [i]
    return mydict


def create_index(file_folder):
#    P = len(file)
#    with Pool(P) as p:
    os.chdir(file_folder)
    file_list = os.listdir()
    master_index = {}
    for x in range(len(file_list)):
        file_name = re.split('.txt', file_list[x])[0]
        myfile = insert_file(file_list[x])
        myfile = word_location(myfile)
        for i in myfile:
            if i in master_index.keys():
                master_index[i].append((file_name, myfile[i]))
            else:
                master_index[i] = [(file_name, myfile[i])]
    return master_index

inverted_index = create_index('H:/Staff/Share/Regional Teams/Northeast/Paul/Portilla/inverted index files')
print('Inverted Index Search')
while True:
    lookup_word = input('Word Search: ')
    if lookup_word in inverted_index:
        text_files = []
        for i in range(len(inverted_index[lookup_word])):
            text_files.append(inverted_index[lookup_word][i][0])
        print(text_files)
        question1 = input('Do you want to see the word positions as well? ')
        if question1 == 'yes' or question1 == 'y':
            for j in range(len(inverted_index[lookup_word])):
                print(inverted_index[lookup_word][j][0], ' : ', inverted_index[lookup_word][j][1])
    else:
        print('Sorry that word is not in our files.')
    question2 = input("Enter '/' if you want to end your word search. ")
    if question2 == '/' and question2 == '/':
        break

