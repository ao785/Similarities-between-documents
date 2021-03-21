#Task 1

from porterstemmer import PorterStemmer
from string import digits
import string
import re
import sys

def task1(input_file_name, output_file_name, stop_words_list):

    # open the input file and the list of stop words and create output file
    f_input = open(input_file_name,"r")
    f_output = open(output_file_name, "w+")
    f_stop_words = open(stop_words_list, "r")

    list_lines = f_input.readlines()
    #list of stop words
    list_stop_words = f_stop_words.readlines()
    list_stop_words = list(map(lambda x:x.strip(), list_stop_words))

    #list of document names
    list_documents = []

    ps = PorterStemmer()

    for i in range(len(list_lines)):
        list_words = [] #list of words for a line
        list_words_stemming = [] #list of stemming words for a line

        list_documents.append(list_lines[i].split()[0])

        #remove all the \t and \n
        list_lines[i] = re.sub(r'\s', " ", list_lines[i])
        #change upper cases to lower cases
        list_lines[i] = list_lines[i].lower()
        #remove numbers
        list_lines[i] = list_lines[i].translate(str.maketrans('', '', digits))
        #remove punctuations
        list_lines[i] = re.sub(r'[^a-zA-Z0-9\s]', '', list_lines[i])

        for w in list_lines[i].split()[1:]:
            if w not in list_stop_words:
                list_words.append(w)

        for y in list_words :
            list_words_stemming.append(ps.stem(y,0,len(y)-1))

        # Write the document name in front of the content in the output file
        f_output.write(list_documents[i]+"\t")
        # Write the content of the document in the output file
        for z in list_words_stemming:
            f_output.write(z + " ")
        f_output.write("\n")

    # Close all the file
    f_output.close()
    f_input.close()
    f_stop_words.close()

# function which takes all the input arugments
task1(sys.argv[1],sys.argv[2], sys.argv[3])

