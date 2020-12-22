import sys

def dog():
	print("WOOF")

def main():
	if sys.argv[1] == "dog":
		dog()
	else:
		print("Hello")

if __name__ == '__main__':
	main()

