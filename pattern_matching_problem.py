def pattern_matching_problem(string_1, string_2):
    
    pos = []
    k = len(string_1)
        
    for i in range(len(string_2)):
        if string_1 == string_2[i: i+k]:
            pos.append(str(i))
            
    return " ".join(pos)
    
string = open('pattern_matching_problem_text.txt').read().split()
pattern_matching_problem(string[0], string[1])
