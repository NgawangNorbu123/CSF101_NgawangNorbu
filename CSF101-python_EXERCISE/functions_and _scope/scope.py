x = 10 # Global variable
def print_x():
    x =20 
    print(f"Local x: {x}")

print_x()
print(f"Global x: {x}")

count = 0 
def increment():
    global count
    count += 1
    print(f"Count: {count}")

increment()
increment()
increment()
print(f"Final count: {count}")

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print(f"Inner x: {x}")

    inner()
    print(f"outer x: {x}")
outer()