# Task 3
import re
import sys
import math

def task3(input_TDIM, doc1, doc2):
    f_TDIM = open(input_TDIM,"r")
    list_lines = f_TDIM.readlines()

    list_name_documents = []
    list_words = []
    matrix_number_occurences = []

    for i in range(len(list_lines)):
        list_lines[i] = re.sub(r'\s', " ", list_lines[i]) # remove all \n and \t
        if i == 0:
            for j in list_lines[i].split():
                list_name_documents.append(j)
        else:
            list_words.append(list_lines[i].split()[0])
            list_occurence_in_document = [] #list of number of occurence for each document
            for j in list_lines[i].split()[1:]:
                list_occurence_in_document.append(j)
            matrix_number_occurences.append(list_occurence_in_document)

    # TF operation

    for j in range(len(matrix_number_occurences[0])):
        max_occurence = int(matrix_number_occurences[0][j])
        for i in range(1,len(matrix_number_occurences)):
            if max_occurence < int(matrix_number_occurences[i][j]):
                max_occurence = int(matrix_number_occurences[i][j])
        for i in range(len(matrix_number_occurences)):
            matrix_number_occurences[i][j] = int(matrix_number_occurences[i][j])/max_occurence

    #IDF operation

    DF = [0]*len(matrix_number_occurences)
    Nn = [0]*len(matrix_number_occurences)
    N = len(list_name_documents)
    IDF = [0]*len(matrix_number_occurences)

    for i in range(len(matrix_number_occurences)):
        for j in range(len(matrix_number_occurences[i])):
            if matrix_number_occurences[i][j] > 0:
                DF[i] = DF[i] + 1

        Nn[i] = N/DF[i]
        IDF[i] = math.log10(Nn[i])

    #multiple TF with IDF
    for i in range(len(matrix_number_occurences)):
        for j in range(len(matrix_number_occurences[i])):
            matrix_number_occurences[i][j] = matrix_number_occurences[i][j]*IDF[i]

    # Calculate length of each vectors

    length_vectors = [0]*len(list_name_documents)

    for j in range(len(matrix_number_occurences[0])):
        for i in range(len(matrix_number_occurences)):
            length_vectors[j] = length_vectors[j] + matrix_number_occurences[i][j]**2
        length_vectors[j] = math.sqrt(length_vectors[j])

    # Close the file
    f_TDIM.close()

    # Calculate the similarity between two documents
    index_document1 = list_name_documents.index(doc1)
    index_document2 = list_name_documents.index(doc2)

    denominator = length_vectors[index_document1] * length_vectors[index_document2]
    numerator = 0
    for i in range(len(matrix_number_occurences)):
        numerator = numerator + matrix_number_occurences[i][index_document1]*matrix_number_occurences[i][index_document2]
    similarity = numerator/denominator

    return similarity

print("Cosinus Score = ", task3(sys.argv[1],sys.argv[2],sys.argv[3]))


