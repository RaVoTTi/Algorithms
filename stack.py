def bye():
    print("ok bye!!")

def greeter2(name):
    print("How are " + name)

def greeter(name):
    print("Hello World!" + name)
    greeter2(name)
    print("Hello World again!")
    bye()



if __name__ == "__main__":
    greeter('Valen')