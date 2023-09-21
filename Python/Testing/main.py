answer = input("Play? y/n")
a = input("Number 1: ")
b = input("Number 2 : ")

while True:
    if answer == "y".lower():
        try:
            c = float(a) / float(b)
        except TypeError:
            print("Cannot divide by zero")
        finally:
            print("HEBDBBEIB")
            
    elif answer == "n".lower():
        break



















