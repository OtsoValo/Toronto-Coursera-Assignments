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

	>>> is_valid_sequence("CTG")
	True
	>>> is_valid_sequence("ACGTACG")
	True
	>>> is_valid_sequence("GGGGGG")
	True
	>>> is_valid_sequence("tGCtAG")
	False
	"""

	for char in sequence:
		if char not in "ATCG":
			return False
	return True		


# print(is_valid_sequence("CTG"))
# print(is_valid_sequence("ACGTACG"))
# print(is_valid_sequence("GGGGGG"))
# print(is_valid_sequence("tGCtAG"))