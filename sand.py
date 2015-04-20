f = open("correct_sample.in","r")
lines = f.readlines()
line = lines[0].rstrip("\n")

atomList = ["Ag", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]

states = ["number", "startParent", "endParent", "bigChar", "smallChar"]

def identifier(char):

	if char.isdigit():
		return "number"

	if char == "(":
		return "startParent"

	if char == "(":
		return "endParent"

	if char.isupper():
		return "bigChar"

	if char.islower():
		return "smallChar"


def formelCheck(variable):
	try:
		molCheck(0, variable)
		print("Formeln är syntaktiskt korrekt")

	except Exception as error:
		error = str(error)
		index = int(error[-1:])
		text = error[:-1]
		print(text + " vid radslutet " + variable[index:])


def molCheck(position, variable ):
	print("molCheck!", variable, position)

	if(len(variable)) == 0:
		return 0

	index = groupCheck(position, variable)
	molCheck(position + index, variable[index:])


def groupCheck(position, variable):
	print("groupCheck", variable, position)

	if(variable[0] == "("):
		index = molCheck(position +1, variable[1:])
		if variable[index + position:] == ")":
			print("bra!")



	indexOne = atomCheck(position, variable)
	if indexOne > 0:
		indexTwo = numCheck(position, variable[indexOne:])
		if indexTwo > 0:
			return indexOne + indexTwo
		else:
			return indexOne

	return 0



def atomCheck(position, variable):
	print("atomCheck", variable, position)

	if len(variable) == 0:
		return 0

	index = 0

	first = identifier(variable[0])

	if first == "bigChar":
		second = identifier(variable[1])
		if second == "smallChar":
			index = 2					#Number if chars in the "atom"
		else:
			index = 1					#Number of chars in the "atom"

	if variable[:index] in atomList:
		return index

	else:
		raise Exception("Okänd atom" + str(position))



def numCheck(position, variable):
	print("numCheck", variable, position)
	if len(variable) == 0:
		return 0			

	for i in range(len(variable)):

		identity = identifier( variable[i])

		if not identity == "number":
			if i == 0:					#There were no numbers at all!
				return i
			else:
				break

	if i == 0 and int(variable[0]) < 2: #It's only one character and that is a 1 or 0.
		raise Exception("För litet tal" + str(position))
	return i +1



formelCheck("Na33Au")






