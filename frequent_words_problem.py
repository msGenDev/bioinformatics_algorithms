## Python function that finds the most frequent k-mers in a string given a DNA string Text and an integer k.

from collections import Counter

def frequent_words_problem(string, k):

    words = []
    results = []    
    
    for i in range(len(string)):    
        words.append("".join(string[i: i+k]))
                
    tuples = Counter(words).most_common()
    max_count = max([y for (x, y) in tuples])
    
    for (x, y) in tuples:
        if y == max_count:
            results.append(x)
            
    return results

string = "".join(open('frequent_words_problem_text.txt')).split()
frequent_words_problem(string[0], int(string[1]))
