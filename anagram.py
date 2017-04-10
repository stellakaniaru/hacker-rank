'''Given a a string which is a concatation of two substrings,
determine if the two are anagrams of each other'''

def anagram(word):
	'''Should find out if a given word is an anagram or not'''

	#check if the word can be divided into equal substrings
	#return -1 if the word cant be divided into two equal strings
	if len(word) % 2 == 0:
		a,b = word[:len(word)/2], word[len(word)/2:]

		#sort the substrings to get them in list format
		a1 = sorted(a)
		b1 = sorted(b)
		c = []

		#loop through to check if elements in both substrings are equal
		#return the elements not in both lists in a new list and output the length of the list
		for i in a1:
			if i not in b:
				c.append(i)
		return len(c)
	return '-1'


# Tests = input('')

# for i in range(Tests):
# 	print anagram(str(input()))