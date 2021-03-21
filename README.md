# Similarities-between-documents

1. This project is built under Python (version 3.8.2)
2. You have to put all your files in the same folder and make sure to put the folder path in your console.

The goal of this project is to show the similarity between documents using differents methods. You can find a small description of the code just below.

The 1st step (task1.py) preprocesses the documents. (Gathering, tokenization, stopword removal, stemming (Poter algorithm) and index creation). The 2nd step (task2.py) creates the TDIM (Term-Document incident Matrix) and the inverted index matrix. The 3rd step calculates the similarity between 2 documents using cosinus similarity.

You can find in the project some examples of inputs but you can also use your own documents.

Use the command just below to run your programms

#######################################################################
############################ Task 1 ###################################
#######################################################################

3 arguments:
- input file
- name of the output file
- list of stop words 

returns:
- text file of pre-processed documents

#######################################################################
#######################################################################

cmd: 
python3 task1.py <input_file> <output_file> <stopword_list>

example: 
python3 task1.py "input_file.txt" "output_file.txt" "stopword_list.txt"

#######################################################################
############################ Task 2 ###################################
#######################################################################

1 argument:
- text file of pre-processed documents

returns:
- TDIM named "TDIM.txt"
- Inverted index named "InvIndex.txt"

#######################################################################
#######################################################################

cmd:
python3 task2.py <stemming_input_file>

example: 
python3 task2.py "output_file.txt"

#######################################################################
############################ Task 3 ###################################
#######################################################################

3 arguments:
- TDIM
- document title
- document title

returns:
- similarity between documents passed as arguments 

#######################################################################
#######################################################################

cmd:
python3 task3.py <TDIM> <doc> <doc>

example:
python3 task3.py "TDIM.txt" "D1" "D2"
