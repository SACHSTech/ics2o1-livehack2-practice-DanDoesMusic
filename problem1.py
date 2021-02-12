####inputs for mesurements#######

base = int(input("What is the length of the base: "))
side = int(input("What is the length of the second side: "))
hyp = int(input("What is the length of the hypotenose (longest side) : " ))

#### calculating#########

m1 = base**2
m2 = side**2
m3 = hyp**2

###done########

if (m1+m2 == m3) or (m1+m3 == m2) or (m2+m3 == m1):
    print("A triangle with lengths " + str(base) + ", " +
    str(side) + ", and " + str(hyp) + " forms a right-angled triangle.")

else:
    print("A triangle with lengths " + str(base) + ", " +
    str(side) + ", and " + str(hyp) + " does not form a right-angled triangle.")
