## Python function that finds all integer(s) i minimizing Skew(Prefixi (Text)) 
## over all values of i (from 0 to |Genome|) given a DNA string Genome.

def skew(genome):
            
    output = [0]
    count = 0
    
    for x in genome:
        if x == "G": 
            count = count + 1
        if x == "C":
            count = count - 1
        output = output + [count]
        
    return output

def minimum_skew_problem(string):
            
    t = skew(string)
    minimum_skew = [i for i,n in enumerate(t) if n == min(t)]
            
    return minimum_skew

string = "".join(open("minimum_skew_data.txt")).split()            
minimum_skew_problem(string[0])
