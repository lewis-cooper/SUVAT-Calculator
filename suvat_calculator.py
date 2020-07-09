import math
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
            inpt = input("")                                #Stores user input in inpt variable
            return float(inpt)                              #Tries to convert input to a float
        except ValueError:                                  #Checks if user input fails to convert to a float
            if inpt == (""):                                #If user input fails to convert to float and is empty the program carries on
                return print("")
            else:                                           #If user input fails to convert to float and isn't empty then the program asks for a new value
                print("Input only accepts decimal numbers.")


#Storing values for each of the SUVAT variables
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

#Result messages
s_result = 'The value of s is %.3f m'
u_result = 'The value of u is %.3f m/s'
v_result = 'The value of v is %.3f m/s'
a_result = 'The value of a is %.3f m/s^2'
t_result = 'The value of t is %.3f s'
'''
   _________    __    ________  ____    ___  __________  ____ 
  / ____/   |  / /   / ____/ / / / /   /   |/_  __/ __ \/ __ \
 / /   / /| | / /   / /   / / / / /   / /| | / / / / / / /_/ /
/ /___/ ___ |/ /___/ /___/ /_/ / /___/ ___ |/ / / /_/ / _, _/ 
\____/_/  |_/_____/\____/\____/_____/_/  |_/_/  \____/_/ |_|  
                                                             
'''

#SUVAT EQUATIONS
#When s == None
if s == None and u == None:
    u = v - a*t
    print(u_result % u)

elif s == None and v == None:
    v = u + a*t
    print(v_result % v)

elif s == None and a == None:
    a = (v-u)/t
    print(a_result % a)

elif s == None and t == None:
    t = (v-u)/a
    print(t_result % t)

if s == None:
    s=(u+v)*t*0.5
    print(s_result % s)


#When v == None
if v == None and u == None:
    u=(s/t)-0.5*a*t
    print(u_result % u)

elif v == None and a == None:
    a = (2*(s-t*u))/t**2
    print(a_result % a)
    
elif v == None and t == None:
    try:
        t = (math.sqrt(2*a*s+u**2)-u)/a
        print(t_result % t)
    except ValueError:
        print("")

if v == None:
    try:
        v = u+a*t
        print(v_result % v)
    except TypeError:
        print("No real roots for v")


#When a == None
if a == None and u == None:
    u = ((2*s)/t)-v
    print(u_result % u)

elif a == None and t == None:
    t = (2*s)/(u+v)
    print(t_result % t)

if a == None:
    a = (v-u)/t
    print(a_result % a)
    
#When t == None
if t == None and u == None:
    try: 
        u = math.sqrt((v**2)-(2*a*s))
        print(u_result % u)
    except ValueError:
        print("No real roots for u")
        

if t == None:
    try:
        t = (v-u)/a
        print(t_result % t)
    except TypeError:
        print("Can not solve for t")
  
    
    
    
#In memory of David Rogers
