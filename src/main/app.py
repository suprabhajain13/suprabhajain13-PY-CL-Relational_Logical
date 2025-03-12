from lab import (
    equal_to,
    greater_than,
    less_than,
    greater_than_or_equal_to,
    less_than_or_equal_to,
    not_equal_to,
    logical_and,
    logical_or,
    logical_not
)

if __name__ == "__main__":
    # Relational operators
    print("Relational Operators:")
    print("Enter the values for a and b")
    a=int(input())
    b=int(input())
    print(f"{a} == {b}: ", equal_to(a, b))
    print(f"{a} > {b}: ", greater_than(a, b))
    print(f"{a} < {b}: ", less_than(a, b))
    print(f"{a} >= {b}: ", greater_than_or_equal_to(a, b))
    print(f"{a} <= {b}: ", less_than_or_equal_to(a, b))
    print(f"{a} != {b}: ", not_equal_to(a, b))
    
    # Logical operators
    print("\nLogical Operators:")
    print("True and False: ", logical_and(True, False))
    print("True or False: ", logical_or(True, False))
    print("Logical not True: ", logical_not(True))
