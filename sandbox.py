principal = 50.0
interest = 1.05
val_after_1year = principal * interest
print val_after_1year
x = 2.5
y=3.2
w = x*y
z=(w**3 + 3*x**2 + 5*y+10)/(5*x +3) 
print z
x=5
y=3
z=1.0+x/y
result = "The result of this is " + str(z)
print result 
print "The result of this is " + str(1.0+5.0/3.0)
its_thursday = True
its_after6 = True
its_before9 = False
if (its_thursday):
    if(its_after6 and its_before9):
        print "You must be in Astronomy Lab!"
    else:
        print "You are not in Astronomy Lab" 
else:
    print "You are not in Astronomy Lab" 

returned_phone_call = False
days_since_call=3
travels_for_work = False

if(returned_phone_call):
    print "Congratulations! He likes you." 
else:
    if(days_since_call<=2 or travels_for_work): 
        print "Give it time...he may still be interested" 
    else: 
        print "He's just not that into you" 

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for planet in planets: 
    print planet 

divis = []
for i in range(1,1000):
    isDivis = False
    if (i%3 == 0 and i%7 == 0):
        isDivis = True 
    if (isDivis):
        divis.append(i)
    
count = len(divis)

print count

from random import random as rand 
x=[]
for i in range(10):
    x.append(rand()*10)
print x 

num_x = len(x)
z= 0
for j in range(num_x):
    if(x[j] > z):
        z= x[j]
print z 


        