"""For a given input string “Python is a case sensitive language”. Write python
code for the following:
a. Find the length of the input string.
b. Reverse the order of the string in one line code.
c. Using Slice function store “a case sensitive” in new string.
d. Replace “a case sensitive” with “object oriented”.
e. Find index of substring “a” in the given input string.
f. Remove the white spaces from the given input string."""

a="python is a case sensitive language"
print("length of string=",len(a))
print(a[::-1])
b=a[10:26:1]
print(b)
replaced=a.replace("a case sensitive","object oriented")
print(replaced)
print(a.index("a"))
print(a.replace(" ",""))


