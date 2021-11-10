# Python program for KMP Algorithm
def find_kmp(P, T):
	m = len(P)
	n = len(T)

	# create lps[] that will hold the longest prefix suffix
	# values for pattern
	lps = [0]*m
	j = 0 # index for P[]

	# Preprocess the pattern (calculate lps[] array)
	compute_LPS_array(P, m, lps)

	i = 0 # index for T[]
	while i < n:
		if P[j] == T[i]:
			i += 1
			j += 1

		if j == m:
			print("Found pattern at index " + str(i-j))
			j = lps[j-1]

		# mismatch after j matches
		elif i < n and P[j] != T[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def compute_LPS_array(P, m, lps):
	len = 0 # length of the previous longest prefix suffix

	#lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to m-1
	while i < m:
		if P[i]== P[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1


with open("/Users/temporaryadmin/github-classroom/dci-dh-python-e21-01/python-algorithmic_thinking-algorithm_efficiency-SyncopatedPandemonium/src/sample.txt") as f:
    sample_text = f.read()

find_kmp("dolor", sample_text)