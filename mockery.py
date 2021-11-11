count = 0
list = []

normal = input("Enter a word/sentence to be converted to mock case: ")

def even(num):
	if num % 2 == 0:
		return True

while count != len(normal):
	if even(count):
		uppers = normal[count].lower()
		list.append(uppers)
	else:
		lowers = normal[count].upper()
		list.append(lowers)
	count += 1

print(''.join(list))
