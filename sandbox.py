f = open("correct_sample.in","r");
lines = f.readlines();

atoms = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]





def molCheck(variable):
	for i in range(len(variable)):
		groupCheck(variable[:i])
		molCheck(variable[i:])


def groupCheck(variable):
	for i in range(variable):
		ATOMCheck( variable[:i])

		#eller
		ATOMCheck( variable[:i])
		numCHeck( variable[i:])

		#eller
		molCheck( variable[:i])
		numCheck( variable[i:])


def ATOMCheck(variable):
	varLength = len(variable)
	if varLength > 1:
		return False
	if varLength == 1:
		if LETTERCheck(variable[0]):
			return True
	if varLength == 2:
		if LETTERCheck(variable[0]) and letterCheck(variable[1]):
			return True


def numCheck(variable):
	if int(variable) > 0:
		return True
	return False

