## 1. [clump_finding_problem.py](https://github.com/noelnamai/bioinformatics_algorithms/blob/master/clump_finding_problem.py)

Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval of Genome of length L in which Pattern appears at least t times. For example, TGCA forms a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAaTGCAtgacaagccTGCAgttgttttac

### Clump Finding Problem

Find patterns forming clumps in a string.

**Given:** A string Genome, and integers k, L, and t.

**Return:** All distinct k-mers forming (L, t)-clumps in Genome.

### Sample Dataset

```
CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
5 75 4
```

### Sample Output

```
CGACA GAAGA AATGT
```

=========================================================

## 2. frequent_words_problem.py

This is the first problem in a collection of "code challenges" to accompany Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau &amp; Pavel Pevzner.

A k-mer is a string of length k. We define Count(Text, Pattern) as the number of times that a k-mer Pattern appears as a substring of Text. For example,

```
Count(ACAACTATGCATACTATCGGGAACTATCCT,ACTAT)=3
```

We note that Count(CGATATATCCATAG, ATA) is equal to 3 (not 2) since we should account for overlapping occurrences of Pattern in Text.

We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".

### Frequent Words Problem

Find the most frequent k-mers in a string.

**Given:** A DNA string Text and an integer k.
    
**Return:** All most frequent k-mers in Text (in any order).

### Sample Dataset

```
ACGTTGCATGTCGCATGATGCATGAGAGCT
4
```

### Sample Output

```
CATG GCAT
```

=========================================================

## 3. minimum_skew_problem.py

Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of G and C in Genome. Let Prefixi (Genome) denote the prefix (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefixi ("CATGGGCATCGGCCATACGCC")) are:

0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

### Minimum Skew Problem

Find a position in a genome minimizing the skew.

**Given:** A DNA string Genome.

**Return:** All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).

### Sample Dataset

```
CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG
```

### Sample Output

```
53 97
```

=========================================================

## 4. pattern_matching_problem.py

Recall from that different occurrences of a substring can overlap with each other. For example, ATA occurs three times in CGATATATCCATAG.

### Pattern Matching Problem

Find all occurrences of a pattern in a string.

**Given:** Strings Pattern and Genome.

**Return:** All starting positions in Genome where Pattern appears as a substring.

### Sample Dataset

```
ATAT
GATATATGCATATACTT
```

### Sample Output

```
1 3 9
```

=========================================================

## 5. reverse_complement_problem.py

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide p, we denote its complementary nucleotide as p. The reverse complement of a string Pattern = p1…pn is the string Pattern = pn … p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string.

For example, the reverse complement of Pattern = "GTCA" is Pattern = "TGAC".

### Reverse Complement Problem

Find the reverse complement of a DNA string.

**Given:** A DNA string Pattern.

**Return:** Pattern, the reverse complement of Pattern.

### Sample Dataset

```
AAAACCCGGT
```

### Sample Output

```
ACCGGGTTTT
```

=========================================================
