''''Given a string that is not more than 1000 characters,check if its a panagram or not.If its a panagram,print out "panagram" else "not panagram".A panagram is a string that contains all letters of the alphabet.'''

#List the alphabet and convert it to a set
alphabet = set(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'))

#Ask user to enter string and covert it to a string comprising lower case elements
string =set(str(raw_input('').lower())) 

#Compare the two sets to check if all elements in one are in the other
#Check if the length of the string is less than 1000
if len(string) <= 1000:
	if alphabet.issubset(string):
		print ('pangram')
	else:
		print ('pangram')