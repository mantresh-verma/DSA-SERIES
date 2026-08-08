# Square Pattern
def char_square_pattern(n: int):
    print("=========Character Square Pattern============")
    for i in range(1, n + 1):
        ch = ord("A")
        for j in range(1, n + 1):
            print(chr(ch), end="")
            ch += 1
        print("")


def num_square_pattern(n: int):
    print("=========Number Square Pattern============")
    num = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(num, end="")
            num += 1
        print("")


def star_triangle_pattern(n: int):
    print("=========Star Triangle Pattern============")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print("")


def num_pyramid_pattern(n: int):
    print("=========Number Pyramid Pattern============")
    for i in range(1, n + 1):
        rev = 1
        print(" " * (n - i), end="")
        for j in range(0, 2 * i - 1):
            if j + 1 <= i:
                print(j + 1, end="")
            else:
                print(j - rev, end="")
                rev = rev + 2
        print("")



def hollow_diamond_pattern(n: int):
    print("=========Hollow Diamond Pattern============")
    # ============= Top Part ==========================
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(0, 2 * i - 1):
            if (j==0) or (j==2*i-2):
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    
    # ============= Bottom Part ========================
    for i in range(n-1, 0, -1):
        print(" " * (n-i), end="")
        for j in range(2*i-1, 0, -1):
            if (j==2*i-1) or (j==1):
                print("*", end="")
            else:
                print(" ", end="")
        print("")

def butterfly_pattern(n: int):
    print("=========Butterfly Pattern============")
    # ============= Top Part ==========================
    for i in range(1, n + 1):
        for j in range(1, (2*n)+1):
            if (j<=i) or (j>2*n-i):
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    # ============= Bottom Part ========================
    for i in range(n, 0, -1):
        for j in range(1, (2*n)+1):
            if (j<=i) or (j>2*n-i):
                print("*", end="")
            else:
                print(" ", end="")
        print("")



# Function Calling
# char_square_pattern(5)
# num_square_pattern(3)
# star_triangle_pattern(5)
# num_pyramid_pattern(5)
# hollow_diamond_pattern(5)
butterfly_pattern(4)
