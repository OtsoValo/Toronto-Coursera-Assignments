# Code written for Python 3

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


# print(get_length('ATCGAT'))
# print(get_length('ATCG'))


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)


# print(is_longer('ATCG', 'AT'))
# print(is_longer('ATCG', 'ATCGGA'))


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)


# print(count_nucleotides('ATCGGC', 'G'))
# print(count_nucleotides('ATCTA', 'G'))


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """

    return dna2 in dna1


# print(contains_sequence('ATCGGC', 'GG'))
# print(contains_sequence('ATCGGC', 'GT'))


def is_valid_sequence(sequence):
	""" (str) -> bool

	Return True if and only if the DNA sequence is valid (that is, it contains
	no characters other than 'A', 'T', 'C' and 'G').

	>>> is_valid_sequence('CTG')
	True
	>>> is_valid_sequence('ACGTACG')
	True
	>>> is_valid_sequence('GGGGGG')
	True
	>>> is_valid_sequence('tGCtAG')
	False
	"""

	for char in sequence:
		if char not in 'ATCG':
			return False
	return True		


# print(is_valid_sequence('CTG'))
# print(is_valid_sequence('ACGTACG'))
# print(is_valid_sequence('GGGGGG'))
# print(is_valid_sequence('tGCtAG'))


def insert_sequence(dna1, dna2, index):
	""" (str, str, int) -> str

	Return the DNA sequence obtained by inserting the second DNA sequence into
	the first DNA sequence at the given index. (You can assume that the index
	is valid.)

	>>> insert_sequence('TCG', 'A', 0)
	'ATCG'
	>>> insert_sequence('CCGG', 'AT', 2)
	'CCATGG'
	>>> insert_sequence('GGG', 'TTT', 3)
	'GGGTTT'
	"""

	return dna1[:index] + dna2 + dna1[index:]


# print(insert_sequence('TCG', 'A', 0))
# print(insert_sequence('CCGG', 'AT', 2))
# print(insert_sequence('GGG', 'TTT', 3))


def get_complement(nucleotide):
	""" (str) -> str

	The first parameter is a nucleotide ('A', 'T', 'C', or 'G'). Return the
	nucleotide's complement.

	>>> get_complement('A')
	'T'
	>>> get_complement('T')
	'A'
	>>> get_complement('C')
	'G'
	>>> get_complement('G')
	'C'
	"""

	if nucleotide == 'A':
		return 'T'
	elif nucleotide == 'T':
		return 'A'
	elif nucleotide == 'C':
		return 'G'
	return 'C'


# print(get_complement('A'))
# print(get_complement('T'))
# print(get_complement('C'))
# print(get_complement('G'))


def get_complementary_sequence(sequence):
	""" (str) -> str

	The parameter is a DNA sequence. Return the DNA sequence that is
	complementary to the given DNA sequence.

	>>> get_complementary_sequence('AT')
	'TA'
	>>> get_complementary_sequence('ACGTACG')
	'TGCATGC'
	>>> get_complementary_sequence('AAAAA')
	'TTTTT'
	"""

	comp_seq = ''
	for char in sequence:
		comp_seq += get_complement(char)
	return comp_seq


# print(get_complementary_sequence('AT'))
# print(get_complementary_sequence('ACGTACG'))
# print(get_complementary_sequence('AAAAA'))