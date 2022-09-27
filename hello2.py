import sys

def hello():
	if sys.argv[1] == "mars":
		hellomars()
	else:
		helloworld()

def hellomars():
	print("Hello, Mars")

def helloworld():
	print("Hello, World")
