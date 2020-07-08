
import math as math
import time as time
'''
   __  _______ __________     _____   ______  __  ________
  / / / / ___// ____/ __ \   /  _/ | / / __ \/ / / /_  __/
 / / / /\__ \/ __/ / /_/ /   / //  |/ / /_/ / / / / / /   
/ /_/ /___/ / /___/ _, _/  _/ // /|  / ____/ /_/ / / /    
\____//____/_____/_/ |_|  /___/_/ |_/_/    \____/ /_/    

'''
def user_input() -> float:
    while True:
        try:
            inpt = input("")
            return float(inpt)
        except ValueError:
            if inpt == (""):
                return print("")
            else:
                print("Input only accepts decimal numbers.")


print('please enter a value for s:')
s = user_input()
print('please enter a value for u:')
u = user_input()
print('please enter a value for v:')
v = user_input()
print('please enter a value for a:')
a = user_input()
print('please enter a value for t:')
t = user_input()

s_i = s
u_i = u
v_i = v
a_i = a
t_i = t

'''
   _________    __    ________  ____    ___  __________  ____ 
  / ____/   |  / /   / ____/ / / / /   /   |/_  __/ __ \/ __ \
 / /   / /| | / /   / /   / / / / /   / /| | / / / / / / /_/ /
/ /___/ ___ |/ /___/ /___/ /_/ / /___/ ___ |/ / / /_/ / _, _/ 
\____/_/  |_/_____/\____/\____/_____/_/  |_/_/  \____/_/ |_|  
                                                             
'''

#SUVAT EQUATIONS
# V=U+AT
if type(u)==float and type(a)==float and type(t)==float:
    v=u+a*t

elif type(v)==float and type(a)==float and type(t)==float:
    u = v - (a*t)

elif type(v)==float and type(u)==float and type(a)==float:
    t = (v-u)/a

elif type(u)==float and type(v)==float and type(t)==float:
    a = (v-u)/t


#S=UT+1/2AT^2
if type(u)==float and type(t)==float and type(a)==float:
    s = u*t + 0.5*a*t**2

elif type(s)==float and type(t)==float and type(a)==float:
    u=(s/t)-0.5*a*t

elif type(s)==float and type(t)==float and type(u)==float:
    a = (2(s-t*u))/t**2
    
elif type(s)==float and type(u)==float and type(a)==float:
    t = (math.sqrt(2*a*s+u**2)-u)/a


#V^2=U^2+2AS
if type(u)==float and type(a)==float and type(s)==float:
    v=math.sqrt(u**2+(2*a*s))

elif type(v)==float and type(u)==float and type(a)==float:
    s = (v**2 - u **2)/2*a
    
elif type(v)==float and type(a)==float and type(s)==float:
    u=math.sqrt(v**2-2*a*s)
    
elif type(v)==float and type(u)==float and type(s)==float:
    a = (v**2 - u**2)/2*s

#S=(U+V)T/2
if type(u)==float and type(v)==float and type(t)==float:
    s=(u+v)*t*0.5

elif type(s)==float and type(u)==float and type(v)==float:
    t= (2*s)/(u+v)

elif type(v)==float and type(t)==float and type(s)==float:
    u = ((2*s)/t)-v

elif type(u)==float and type(t)==float and type(s)==float:
    v= ((2*s)/t)-u

'''
    ____  ___________ __  ____  ___________
   / __ \/ ____/ ___// / / / / /_  __/ ___/
  / /_/ / __/  \__ \/ / / / /   / /  \__ \ 
 / _, _/ /___ ___/ / /_/ / /___/ /  ___/ / 
/_/ |_/_____//____/\____/_____/_/  /____/  

'''
print("Calculating...\n")
time.sleep(1)

if s_i == None:
    print ("The value for s is: %.3f m\n" % s)

if u_i == None:
    print ("The value for u is: %.3f m/s\n" % u)
    
if v_i == None:
    print ("The value for v is: %.3f m/s\n" % v)

if a_i == None:
    print ("The value for a is: %.3f m/s^s\n" % a)

if t_i == None:
    print ("The value for t is: %.3f s\n" % t)

      
      
#In memory of David Rogers
