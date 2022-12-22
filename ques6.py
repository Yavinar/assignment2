"""For any three lengths, there is a simple test to see if it is possible to form a
triangle. If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
converts them to integers, and to check whether the given input lengths can
form a triangle or not (Print : “Yes” or “No”)."""
len1 = float(input("Enter length of side 1: "))
len2 = float(input("Enter length of side 2: "))
len3 = float(input("Enter length of side 3: "))
if len1 + len2 > len3 and len2 + len3 > len1 and len1 + len3 > len2:
    print("Yes")
else:
    print("No")