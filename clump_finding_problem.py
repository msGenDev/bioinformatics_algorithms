## Python function to find all distinct k-mers forming (L, t)-clumps in Genome given string Genome, and integers k, L, and t.

from collections import Counter

def frequent_words_problem(string, k):

    words = []
    results = []    
    
    for i in range(len(string)):  
        word = "".join(string[i: i+k])
        if len(word) == k:
            words.append(word)
                
    return Counter(words).most_common()

#string = "".join(open('frequent_words_problem_text.txt')).split()
#frequent_words_problem(string[0], int(string[1]))

import itertools

def clump_finding_problem(string, k, L, t):
    
    words = []
    
    for i in range(len(string)):
        string_1 = string[i: i+L]
        if len(string_1) == L:            
            words.append(frequent_words_problem(string_1, k))
            
    dummy = list(itertools.chain(*words))
    return [y for y in set([x[0] for x in dummy if x[1] >= t])]
            
k = 11
L = 566
t = 18

string = "".join(open('clump_finding_problem_text.txt')).split()
clump_finding_problem(string[0], int(string[1]), int(string[2]), int(string[3]))
