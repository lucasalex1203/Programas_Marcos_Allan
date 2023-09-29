conjunto_A = A = {1, 2, 3, 4, 5}
conjunto_B = B = {2, 4}
print(conjunto_A)
print(conjunto_B)
if conjunto_B.issubset(conjunto_A):
    print("B é um subconjunto de A")
if conjunto_A.issuperset(conjunto_B):
    print("A é um subconjunto de B")
