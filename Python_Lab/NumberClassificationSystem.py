#Number Classification System
def classify(num):
    if num > 0:
        print("Positive", end=", ")
    elif num < 0:
        print("Negative", end=", ")
    else:
        print("Zero", end=", ")

    if num != 0:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

nums = [int(x) for x in input("Enter numbers: ").split()]

for n in nums:
    classify(n)
