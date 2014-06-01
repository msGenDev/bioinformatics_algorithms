## Python function to find all starting positions where Pattern appears as a substring of Text with at most d mismatches
## given strings Pattern and Text along with an integer d.

def find_pattern(p, q, d):
    count = 0
    for x, y in zip(p,q):
        if x != y: 
            count = count + 1
        if count > d:
            return False
    return True
	
def approximate_pattern_matching_problem(pattern, genome, d):
    pos = []
    k = len(pattern)
    l = len(genome)
    for i in range(l-k):
        if appmatchpat(pattern, genome[i:i+k], d):
            pos = pos + [i]
    return pos
    
string =  "".join(open("approximate_match_data.txt")).split()
approximate_pattern_matching_problem(string[0], string[1], int(string[2]))