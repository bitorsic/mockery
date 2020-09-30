normal = input("Enter a word/sentence to be converted to mock case: ")

def even(num):
	if num % 2 == 0:
		return True
		
count = 0
list = []

def mock_case():
	global count, list
	while count != len(normal):
		if even(count):
			uppers = normal[count].upper()
			list.append(uppers)
		else:
			lowers = normal[count].lower()
			list.append(lowers)
		count += 1
	print(''.join(list))

mock_case()