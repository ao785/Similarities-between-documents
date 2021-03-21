#Task 2

import re
import sys

def task2(input_stemming_file):
    # Open text file of pre-processed document and create TDIM.txt and InvIndex.txt file
    f_input_stemming = open(input_stemming_file, "r")
    f_TDIM = open('TDIM.txt',"w+")
    f_inverted_index = open('InvIndex.txt ', "w+")

    list_lines = f_input_stemming.readlines() # list of lines of pre-processed document
    list_words = [] # list of words of the pre-processed document
    list_documents = [] # list of documents where the word appeared
    list_number_words = [] # Matrix of numbers of occurence for each word and document
    list_documents_names = [] #list of document names

    for i in range(len(list_lines)):

        list_documents_names.append(list_lines[i].split()[0]) # Start to fill the list of document names
        list_lines[i] = re.sub(r'\s', " ", list_lines[i]) # remove all \n and \t

        # loop to fill all the list with appropriated values
        for j in list_lines[i].split()[1:]:
            if j not in list_words:
                list_words.append(j)
                list_documents.append(list_documents_names[i])
                list_number_words.append([0]*len(list_lines))
                list_number_words[-1][i] = 1
            else:
                position_word_in_list = list_words.index(j)
                list_number_words[position_word_in_list][i] = list_number_words[position_word_in_list][i] + 1
                if list_documents_names[i] not in list_documents[position_word_in_list].split():
                    list_documents[position_word_in_list] = list_documents[position_word_in_list] + " "+list_documents_names[i]
    # Write in the inverted index file
    for i in range(len(list_words)):
        f_inverted_index.write(list_words[i]+"\t")
        for j in list_documents[i].split():
            f_inverted_index.write(j+"\t")
        f_inverted_index.write("\n")

    # Write in the TDIM file
    f_TDIM.write("\t")
    # Write the name of each documents on the top of the TDIM file
    for i in range(len(list_lines)):
        if i < len(list_lines)-1:
            f_TDIM.write(list_documents_names[i]+"\t")
        else:
            f_TDIM.write(list_documents_names[i]+"\n")
    # Write all the words and the number of occurence for each document and word
    for i in range(len(list_words)):
        f_TDIM.write(list_words[i]+"\t")
        for j in range(len(list_lines)):
            if j < len(list_lines)-1:
                f_TDIM.write(str(list_number_words[i][j])+"\t")
            else:
                 f_TDIM.write(str(list_number_words[i][j])+"\n")

    # Close all the files.
    f_input_stemming.close()
    f_inverted_index.close()
    f_TDIM.close()

task2(sys.argv[1])