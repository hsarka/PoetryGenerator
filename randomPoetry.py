import random

vocabulary = open("common_english_words.txt").readlines()
words = [word.rstrip() for word in vocabulary]
#print(words)
writePoem = random.SystemRandom()
#print(writePoem)

with open("Random Poetry.txt", "w") as text_file:
	newPoem = writePoem.choice(words)
	print(newPoem.upper())
	print(newPoem.upper(), file = text_file)
	
	count = 0
	while (count < 9):
		count += 1
		writingPoem = writePoem.choice(words)
		if count%3 == 1:
			print(writingPoem.capitalize(), end = " ")
			print(writingPoem.capitalize(), end = " ", file = text_file)
		else:
			print(writingPoem, end = " ")
			print(writingPoem, end = " ", file = text_file)
		if count%3 == 0:
			print()
			print(file = text_file)