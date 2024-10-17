#Example-1

def Table():
    n = int(input("Enter the number: "))
    for i in range(1,11):
        print(f"{n} X {i} = {n * i}")

Table()
print("-------------------------------------------")
def reverse_table():
    n = int(input("Enter the number: "))
    for i in range(1,11):
        print(f"{n} X {11-i} = {n * (11-i)}")

reverse_table()

print("-------------------------------------------")
#Example-2

def avg():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))
    d = int(input("Enter the number: "))

    average = (a + b + c + d) / 3
    print("Average is: ",average)

avg()
