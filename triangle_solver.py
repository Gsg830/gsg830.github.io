"The hypotenuse of a right triangle is 65cm. The sum of the other two sides is 79cm. Find the lengths of the other two sides of the rectangle. (16cm,63cm)"

a = int(input("enter a + b value: ")) #max value imput
b = 0 #min value
r = int(input("enter 'c' value: ")) # enter 'c' value
c = r*r
d = 1
print()
print()

for x in range(0,a):
  if a < 0 :
    print("Not possible")
  elif a > 0:
    print("group " + str(d) + ": ")
    print("a = " + str(a))
    print("b = " + str(b) + "\n")
  if a**2+b**2 == c:
    print("Answer is group " + str(d))
  b +=1
  a -=1
  d +=1
  
  
