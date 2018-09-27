def FitstVerse(n):
    print(n, "bottles of beer on the wall,", n, ",bottles of beer")


def StandardVerse(n):
    print("Take one down pass it around,", n, "bottles of beer on the wall.")
    print(n, "bottles of beer on the wall,", n, ",bottles of beer")


def TwoBottles(n):
    print("Take one down pass it around, 2 bottles of beer on the wall.")
    print("2 bottles of beer on the wall, 2 bottles of beer.")


def OneBottle(n):
    print("Take one down pass it around, 1 bottle of beer on the wall.")
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, no more bottles of beer on the wall.")


def NoBottles(n):
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store, buy some more, 99 bottles of beer on the wall.")

# for n in range(10, 0, -1):
#     if n == 10:
#         FitstVerse(n)
#     elif n > 1:
#         StandardVerse(n)
#     elif n == 1:
#         OneBottle(n)
#     else:  # n == 0
#         NoBottles(n)


[FitstVerse(n) for n in range(10, 0, -1) if n == 10]
[StandardVerse(n) for n in range(10, 0, -1) if 10 > n > 1]
[OneBottle(n) for n in range(10, 0, -1) if n == 1]
[NoBottles(n) for n in range(10, 0, -1) if n == 0]
