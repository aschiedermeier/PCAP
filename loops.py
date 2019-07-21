for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

print()
for digit in "0165031806510":
    if digit == "0":
        digit = "x"
        print(digit, end="")
    print(digit, end="")