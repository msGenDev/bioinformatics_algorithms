## Python function to find all starting positions where Pattern appears as a substring of Text with at most d mismatches
## given strings Pattern and Text along with an integer d.

def approximate_pattern_matching_problem(pattern, text , d):
        
    the_index = []
    
    for index in range(len(text)):
        partition = text[index: index+len(pattern)]
        
        if len(partition) == len(pattern): 
            matches = 0
            mismatches = 0
        
            for i in range(len(pattern)):
                if pattern[i] == partition[i]:
                    matches += 1                        
                else:
                    mismatches += 1
                    
            if mismatches <= d:
                the_index.append(index)
                
    return " ".join(map(str, the_index))
    
string =  "".join(open("approximate_match_data.txt")).split()
approximate_pattern_matching_problem(string[0], string[1], int(string[2]))
