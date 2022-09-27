
import sys 

def hello():
	if sys.argv[1] == "Jupiter":
		hellojupiter()
	elif sys.argv[1] == "Mars":
		hellomars()

def helloworld():
	print("Hello, World")

def hellojupiter():
	print("Hello, Jupiter")

if __name__ == "__main__":
	hello()
 
def hellomars():
	print("Hello, Mars")
