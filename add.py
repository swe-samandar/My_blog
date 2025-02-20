def add(a, b):
    if a == 0:
        return b
    
    if b == 0:
        return a
    
    return a + b

if __name__ == "__main__":
    print(add(1, 3))