# hello.py
#The Application / a simple script that acts as your core application logic
def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}! Welcome to MLOps UAT Environment."

if __name__ == "__main__":
    print(greet("Developer"))
    print(f"Sum: {add(5, 3)}")