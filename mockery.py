count = 0
list = []

normal = input("Enter a word/sentence to be converted to mock case: ")

def even(num):
	if num % 2 == 0:
		return True

while count != len(normal):
	if even(count):
		lowers = normal[count].lower()
		list.append(lowers)
	else:
		uppers = normal[count].upper()
		list.append(uppers)
	count += 1

print(''.join(list))
