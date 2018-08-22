
def greeting():
	print ('--------------------------------')
	print ('         MY JOURNAL APP')
	print ('--------------------------------')
	print("Welcome to your journal")
	print('')

def get_choice():
	print("Please select one of the following operations:")
	choice = input("(L)ist entries, (A)dd an entry, (Q)uit :")
	return choice.lower()

if __name__ == "__main__":
    greeting()

