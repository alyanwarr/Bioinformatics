"""
Passed all Tests (even E.Coli)
Solves E.Coli problem. Yeah!
"""
def ClumpFinding(seq,k,l,t):
    kmers_dict = {}
    valid_kmers = []

    for i in range(l-k+1):
        kmer = seq[i:i+k]
        if kmer in kmers_dict.keys():
            kmers_dict[kmer] += 1
            if kmers_dict[kmer] >= t and kmer not in valid_kmers:
                valid_kmers.append(kmer)
        else:
            kmers_dict[kmer] = 1

    for i in range(l-k+1,len(seq)-k+1):
        in_kmer = seq[i:i+k] 
        out_idx = i-l+k-1
        out_kmer = seq[out_idx:out_idx+k]

        kmers_dict[out_kmer] -= 1   # substract kmer going out of window
        if in_kmer in kmers_dict.keys(): 
            kmers_dict[in_kmer] += 1
            if kmers_dict[in_kmer] >= t and in_kmer not in valid_kmers:
                valid_kmers.append(in_kmer)
        else:
            kmers_dict[in_kmer] = 1
        
        if kmers_dict[out_kmer] == 0:
            kmers_dict.pop(out_kmer, None)  # remove kmer from dict if count reaches 0
    
    return valid_kmers


def TestCases():
    # CGACA GAAGA
    print Clump('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 5, 50, 4)
    # AAACCAGGTGG
    print Clump('GCGGTTATGCACCGTTCAAATTAGCAAACCACTAAGCGACGTAGTCTGGATTGATTTCTCCCTACCAGTGACCCAAGACGCGTTAGTGAGTTAAGTTCATATCCAGTACCTGCCGCCCTCTGTACTTGGGCGTCCGATTCGCATGCTTACTCAGGTGGAGGACACGATAATCTGATTAAACTGAGCTAAACCAGGTGGAACCAGAAACCAGGTGGGGAGTCTCGCTTCAAGCCGTTCTTGCGATCAAACCAGGTGGTCCATTATGAAACCAGGTGGCTAAACCAGGTGGTCCAGATCCTCGAATGATGTCGGTGCACATCAAAACCAGGTGGGGTGGTGGAACGTAAAACCAGGTGGCATAAACCAGGTGGGCCGGTTCGTAAACCAGGTGAAACCAGGTGGGGTGGAAACCAGGTGGGTTACAAATTACGTTGAGATGGCCCAAACCAGGTGGTGGGCTTCACCCATGTCAACAAACCACCCTATGGAACTAAACCAGGTGGAACCAGGTGGTGAAGGCTTATCCTCAGGAAAAACCAGGTGGAGGTGGTGAAATAAAACCAGGTGGACCAGGTGGATAACCCTCGCCTCGCTTCTCAACCGAGACCTGGATAAACCAGGTGGGGTGGTCCACCGATTTTTGAGACACTAGAAACCAGGTGGGCGGGGAAACCAGGTGGCAAACCAGGTGGGGTGGACGGAAACCAGGTGGATATGTCATAAAACCAAACCAGGTGGTGCACCCCCATGGTGTGTCTTATCCGTGCGTATAAACCAGGTGGTCGCACGGCTTCCACTTGCTGAGAATAGGCCCGCAGGGTCAGTGCCATGCCCTCCGTCACTCGATATGTGTTGTAAGAGTGGTTACCCCTTCATTGAAGTCGCCCACAGCCCCACCTGCATTGCTAGACTATCACCCTACAGTAGGCCTTTTCGCCTTCTTCAAGCAGCAATCTCTTATCCGCGGATGGGCGCGGCGAGCGTGGCGTCCCCGAACATTTTTACCTAACGTGTTTTGTTGGCCGCAAGCCTTCCCTCTAGTCCACCTCAGCCATTCAGCCTAGTAGCTTTCAAGCCGAGCCTTCCATATCTAATGGACCGTCCAGAATTTCACACGTTTCACAGGGCTGTGTTCGACCGCCCGTAATGCTGTTTCACAGGCGATCGCCTTGCGGTTTTTTCACAGATCGCAGCCGATGGACATGCCAACTCGATTTTCACAGAGTTTTTCACAGCGGTTTCACAGCACAGCAGTGATTGTTTCACAGCAATTTTCACTTTCACAGGGGCCCTTTTCACAGCTCAGGGCTCTTTTCACTTTCACAGTTTCACAGCGCTCCTTTCACAGAGCGGGGAAATTTAAGGGAACACTCAAGGGAACAAGGGAACACACAAAGGGAACACAACACAACACATAAGGGAACACTTTCACAGAACACAAAAGTCCGAAATCATCAGCGGCGAAGGGATTTCACAGACAGACACTTTCACAGCGCATTTCACAGATACGTACTTTCACAGGCGTACTTTCACAGACTTTCACAGAGGACAAGCTCAATTTTCACAGACAGGCTGGATAAATTTCACAGCGGTAAGGGTTTCACAGCACACATAAGGGAACACGAATTTCACAGCAGGGAACACCTCTACGAGTAATCTATTACTCTACCTACTGAAGGGAACACACCGAAGACCTACTATTACCTATTACTCTTAAAGGGAACACATTACAAGGGAACACACTCTCTCGTCATATCTCACCTCTCTATTACTCTTAAGGGAACACCTTCTCGATCAACCTATTACTCTATGGAGATAGAGATATTCCAGACATATGGAGATAACATGGAGATATGGAGATAATGGAGATGGAGATAGCTCTTATATTTATCCTATGGAGATATGATACTATTAATGGAGATAATTCTAATGGAGATATAATTACTCTAAGAGGATGGGATCTCGGGCTATTACTCTAATGGAGATAAGCACTATTACTCTAGGAAATGGAGATATGTCAATGGAGATATGTAATGGAGATAGAGGGAGATGGAGTCGCCATTTCATAATCGCCATTTCATAGTTCAGGAATCGCCATTTCCGCCATTTCTAAGATGGAGTCGCCATTTCTACGTATGGAGATAGGATCGCCATTTCATACGACCCGTTGGATATCGCCATTTCCTCGCCATTTCTGGTGACATTTCTCGCCATTTCATTTCTGGAGATAGATGGATCTCGCCATTTCATAGGAATCGCCATTTCCACGTAGGGGGGGCCACAATCCGTAGGTCGGAATTCAGACTCGCCATTTCCCATCGCCATTTCTTCACCTGTATGCCGATCCCTTCGCCATTTCTCATGGAGATAACTCTCTCTCGCCATTTCTCGCCATTTCCATTTCACTCTCATTCGCCATCGCCATTTCCATTCGCCATTTCATCGCCATTTCTTCAGGATAAGATATCGCCATTTCGACTCTCATTCGCATACTGACTCTCATTCTCATCTCGCCATTTCTCATCTGACTCTCATCCTGGGGGAAACTTGCGACTCTCATCACACTTCCGTCGACTCTCATACTGGCGGATAGCATAGGAGCCATTTAAAGACTCTCATTCTCATTCGAGACTCTCATTCAAATCCTACGAGGACTCTCATATAGACTCTCATATCATTACGAGGACTCTCATATACGAGCCATGCATGTGGCGACGACTCTCATCTACGAGCCATGCAAGCAGAATCTACGAGCGACTCTCATTACGAGCCATGTGACCGTACGAGCCATGCATGCATGCCATGCTGACTCTCATCGAGTACGAGCCATGGAAGTTCTTGTTGGTTCGTAGCCCAAGAGCTGAAGTTACGAGCCTACGAGCCATGAAGTTACTTTTACGAGCCATGAAGCTTACGATACGAGCCATGCGAGCCATGCATCCGCGCTACGAGCCATGTTCCAGTACGAGCCATGTTAGTTGCTGAAGTTAAGTTTGGCGCTGAAGTTTGTACGAGCCATGTGCCCGCTGAAGTTTGTTGTACGAGCCATGCATGCTGAAGTTAATGGCTGAAGTTAGCGTTTGCGGGCAGATCCTCATTCTACGATACGAGCCATGCCATGCAGCTGAAGTTAAGTTGGGTTACGAGCCATGCGAGCCATGTGAAGTACGAGCCATGCTGGCTGAAGTTGTTTGTGCTGCTGAAGTTGCTCTTGTCTCTAGCTGAAGTTGCCAACAGGGCTGAAGCTGAAGTTTAAGCTGAAGTTGCGAGCAGGCTGAAGTTATCGGATTGGGGCTGAAGTTCAACCTCCCGTCCCCCCACACTATATTCCCGTCCCCCCCCGCGCACGCGCCGTCTCCCGTCCCCCCTATCCCGTGCGCACGCGACGCGATCCCGTCCCCCCAGAGTGCGCGCACGCGTCCCCCTTCCCGTCCCCCTCTCCCGGGCGCACGCGTCGCTCAACATTTCCGCGCACGCGTCGCGCACGCGGGCGCACGCGGGTCCCGTCCCCCCCCCTCTTCGGCGCACGCGGAATTCCCGTCGCGCACGCGTCCCGTCCCGCGCACGCGTCGCGCACGCGACTGCCCTAACCAACAGTGCGCACGCGCCGGTAACCCGGTAACCCGGTAACCGCGCACGCGGGCGCACGCGCGTAACCCGCGCACGCGCCGCGCACGCGGCCCGGTTCCCGTCCCCCCCGGTAACCCGGTAACTCCCGTCCCCCGTAACCCGGTGCGCACGCGCCCGGCGCACGCGGAGCGCACGCGCCCCCCCCGGTAATAGCGCACGCGCCCGGGCGCACGCGCCCGGTAACCCGGTAACCCGGGCGCGCGCACGCGGCGGCGCACGCGGCGCACGCGGCGCACGCG',11,566,18)
    # AA   FAILS
    print Clump('AAAACGTCGAAAAA',2,4,2)
    # A C G T
    print Clump('ACGTACGT',1,5,2)
    # AAA CAG CAT CCA GCC TTC
    print Clump('CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG',3,25,3)
    # Ecoli sequence must be loaded from file

    
# Change the function called by main to the desired one. 
def main(args):
    ClumpFinding(*args)


# from console, arguments must be passed inside a list formatted as string: 
# python template.py "['hello', 5, {'age': 30}, [1, 2, 3, 4]]"
if __name__ == '__main__':
    import sys, ast
    if len(sys.argv) == 2 and type(sys.argv[1]) is str:
        try:
            args = ast.literal_eval(sys.argv[1])
        except:
            print "ERROR evaluating input parameters"
            sys.exit()
        main(args)
    else:
        print "Incorrect argument syntax." 
        print "There must be only one argument formatted as string with double quotes"
        print "This string must contain a list with all parameters in the correct format"
        print "Exampe:"
        print "   python template.py \"['hello', 5, {'age': 30}, [1, 2, 3, 4]] \" "
