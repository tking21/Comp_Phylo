#saves nucleotide sequence to the variable DNAseq
DNAseq = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"

#prints DNAseq, and a sentence stating the length of the sequence
print(DNAseq)
print ("This DNA sequence is " + str(len(DNAseq)) + "bp long.") 

#replaces all t to u to covert the DNA sequence to RNA, saves a sequence to the variable RNAseq and prints it 
RNAseq = DNAseq.replace( "t", "u")
print("The RNA sequence is "+ RNAseq) 


def reverseComplement ( seq ):
#a function that generates the reverse complament of a sequence that is passed to it
	compSeq = seq.replace("a", "x").replace("t", "a").replace("x", "t")
	compSeq = compSeq.replace("g", "x").replace("c", "g").replace("x", "c")
	
	revSeq = compSeq[::-1]
	
	print("The reverse complement is "+ revSeq)
	
#extracts and prints the bases corresponding to the 13th and 14th codon of DNAseq
print("The bases corresponding to the 13th and 14th codons are " +DNAseq[39:42]+ " and " +DNAseq[42:45]+ " respectively.") 

#list used to match codons to their corresponding AA
nuc = ["ttt", "ttc", "tta", "ttg", "tct", "tcc", "tca", "tcg", "tat", "tac", "taa", "tag", "tgt", "tgc", "tga", "tgg", "ctt", "ctc", "cta", "ctg", "cct", "ccc", "cca", "ccg", "cat", "cac", "caa", "cag", "cgt", "cgc", "cga", "cgg", "att", "atc", "ata", "atg", "act", "acc", "aca", "acg", "aat", "aac", "aaa", "aag", "agt", "agc", "aga", "agg", "gtt", "gtc", "gta", "gtg", "gct", "gcc", "gca", "gcg", "gat", "gac", "gaa", "gag", "ggt", "ggc", "gga", "ggg"]
AA = ["F", "F", "L", "L", "S", "S", "S", "S", "Y", "Y", "*", "*", "C", "C", "W", "W", "L", "L", "L", "L", "P", "P", "P", "P" ,"H", "H", "Q", "Q", "R", "R", "R", "R", "I", "I", "M", "M", "T", "T", "T", "T", "N", "N", "K", "K", "S", "S", "*", "*", "V", "V", "V", "V", "A", "A", "A", "A", "D", "D", "E", "E", "G", "G", "G", "G"]
 
	
def translate ( nucDNA ):
#translates DNA to protein using the mitochondrial genetic code
	AAseq = " "
	for num in range(0, len(nucDNA), 3): #for and if statements used to extract every 3 bps
		if num < len(nucDNA):
			codon = nucDNA[num:num+3]
			if len(codon) < 3: #if the codon is less than 3 bp, print the sequence (at the end of the sequence)
				print("The corresponding amino acid sequence is " + AAseq + "and it is " + str(len(AAseq))+ " amino acids long") 
				return(AAseq)
			#identify the index of the codon in the list of nucleotides, use this index to the find the corresponding amino acid in the list AA	
			codonIndex = nuc.index(codon) 
			AAseq = AAseq + AA[codonIndex]
			print(AAseq)
		elif num >= len(nucDNA): #another instance to signify reaching the end of the sequence
			print("The corresponding amino acid sequence is " + AAseq) 
			return(AAseq)
			
		
reverseComplement(DNAseq)
translate(DNAseq)	

	