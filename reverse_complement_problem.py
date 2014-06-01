## Python function that finds the reverse complement of a DNA string given a DNA string Pattern. 

def reverse_complement_problem(string):
    
    dictionary = {"A":"T", "T":"A", "C":"G", "G":"C"}
    output = [dictionary[x] for x in string[::-1]]
    return "".join(output)
    
string = "".join(open('reverse_complement_problem_text.txt'))
reverse_complement_problem(string)
