import math

a = 9704
b = 13896
n = 17389
o = 1242

m = math.floor(o ** 0.5) + 1
B = pow(a, m, n)

print("m =", m)

print("big")
for u in range(1, m + 1):
    print(u, pow(B, u, n))
print()
print("small")
for v in range(1, m + 1):
    print(v, (b * pow(a, v, n)) % n)
print()
