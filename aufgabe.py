from random import randint
import sys
n = int(sys.argv[1])
a = []

for i in range (0,n):
    a.append(randint(1,6))

b = sum(a)
print("Summe Der Zahlen:" + str(b))

c = b/n
print("Mittelwert:" + str(c))
