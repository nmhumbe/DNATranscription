import sys

dnaSequence = open(sys.argv[1], "r")
codonsConvKey = open(sys.argv[2], "r")

def makesCodonDict():
    codonDict = {} # creates empty dictionary to store codon to amino acid mapping
    for line in codonsConvKey:
        line = line.strip() # removes whitespace from line
        if line: # makes sure line is not empty
            codon, aminoAcid = line.split()[:2] # splits line into codon and amino acid
            codonDict[codon.lower()] = aminoAcid.lower() # lowers keys to match DNA sequence
    return codonDict

def makesDNAString(DNA): # reads in file and converts DNA sequence into one string
    fullDNAString = ""
    for line in DNA: # goes through each line in DNA sequence
        line = line.strip () # removes whitespace
        if not line.startswith(">"): # skips header lines
            fullDNAString = fullDNAString + line
    fullDNAString = fullDNAString.lower()
    return fullDNAString

def makesRevComp(DNAString): # creates reverse compliment DNA string
    reverseString = ""
    DNAString = DNAString[::-1] # reverses DNA string
    for char in DNAString: # changes to complementary base pair
        if (char == 'c'):
            reverseString += 'g'
        if (char == 'g'):
            reverseString += 'c'
        if (char == 'a'):
            reverseString += 't'
        if (char == 't'):
           reverseString += 'a'
    return reverseString

def translateIndexes(DNAString, codonDict):
    finalList = []
    DNAString = DNAString.lower()
    for dnaSequence in range(0,3): # iterates over the possible reading frames (index 0, 1, 2)
        for i in range(dnaSequence, len(DNAString), 3): # iterates over nucleotides in steps of 3
            codon = DNAString[i:i+3] # extracts current codon from sequence
            if codon == "atg": # checks for start codon
                nextNucleotide = i # stores start codon index
                subset = DNAString[nextNucleotide:] # creates a string witout the previous codon
                for next in range(nextNucleotide, len(DNAString), 3):
                    newCodon = DNAString[next:next+3] # extracts next codon
                    if (next+3 >= len(DNAString) or newCodon in {"tag", "taa", "tga"}): # checks for stop codon or end of sequence
                        nextsubset = DNAString[nextNucleotide:next+3] # extratcs nucleotides from start to stop codon
                        aminoAcids = makeList(nextsubset, codonDict) # translates to amino acids using makelist function
                        finalList.append(aminoAcids) # adds amino acid sequence to final list
                        break # exist loop because stop codon found
    return finalList

def makeList(DNA, codonDict):
    aminoAcidList = ""
    for char in range(0, len(DNA), 3): # iterates over DNA sequence to store translated amino acid
        codons = DNA[char:char+3] # extracts current codon
        aminoAcid = codonDict.get(codons, codons)
        aminoAcidList = aminoAcidList + aminoAcid.upper() # returns upper case amino acids
    return aminoAcidList


codonDict = makesCodonDict()
fullDNAString = makesDNAString(dnaSequence)
reverseString = makesRevComp(fullDNAString)

# transalate DNA sequence into amino acids
translatedSequence = translateIndexes(fullDNAString, codonDict)
translatedReverse = translateIndexes(reverseString, codonDict)

# combines both amino acid lists into one
combinedTranslated = translatedSequence + translatedReverse

# prints each item in list
for value in combinedTranslated:
    print(value)
