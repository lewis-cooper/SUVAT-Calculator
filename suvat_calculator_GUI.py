import tkinter as tk
import math
import time

s = None
u = None
v = None
a = None
t = None

def user_input():
    while True:
        try:
            inpt = input("")                                        #Stores user input in inpt variable
            return float(inpt)                                      #Tries to convert input to a float
        except ValueError:                                          #Checks if user input fails to convert to a float
            if inpt == (""):                                        #If user input fails to convert to float and is empty the program carries on
                return
            else:                                                   #If user input fails to convert to float and isn't empty then the program asks for a new value
                print("Input only accepts decimal numbers.")

def s():
	while True:
		try:
			return float(s_val.get())
		except ValueError:
			if s_val == None:
				return
			else:
				return

def u():
	while True:
		try:
			return float(u_val.get())
		except ValueError:
			if u_val == None:
				return
			else:
				return

def v():
	while True:
		try:
			return float(v_val.get())
		except ValueError:
			if v_val == None:
				return
			else:
				return

def a():
	while True:
		try:
			return float(a_val.get())
		except ValueError:
			if a_val == None:
				return
			else:
				return

def t():
	while True:
		try:
			return float(t_val.get())
		except ValueError:
			if t_val == None:
				return
			else:
				return





HEIGHT = 700			#<-- Changes the height of the window
WIDTH = 550				#<-- Changes the height of the window






#Setting the size of the window
base = tk.Tk()
base.configure(bg='#1D3557')
base.title("SUVAT Calculator")
base.minsize(WIDTH, HEIGHT)
base.maxsize(WIDTH, HEIGHT)

canvas = tk.Canvas(base, height=HEIGHT, width=WIDTH, bg='#1D3557', bd=0, highlightthickness=0)
canvas.pack()


mainframe = tk.Frame(base, bg='#1D3557', bd=0)
mainframe.place(relx = 0.05, rely=0.05, relheight=0.9, relwidth=0.9)

#Main title
title = tk.Label(mainframe, text="SUVAT Calculator", fg='#F1FAEE', bg='#1D3557')			#SUVAT Calculator Title
title.place(relx=0, rely=0, relheight=0.15, relwidth=1)
title.config(font=("Helvetica", 44))

#Divider
divider = tk.Label(mainframe, bg='#E63946')
divider.place(relx=0, rely=0.15, relheight=0.005, relwidth=1)

#S
s_text = tk.Label(mainframe, text="s (m) = ", fg='#F1FAEE', bg='#1D3557')
s_text.place(relx=-0.25, rely=0.2, relheight=0.1, relwidth=1)
s_text.config(font=("Helvetica", 32))

s_val = tk.Entry(mainframe, fg='#F1FAEE', bg='#A8DADC')
s_val.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.5)
s_val.config(font=("Helvetica", 32))


#U
u_text = tk.Label(mainframe, text="u (m/s) = ", fg='#F1FAEE', bg='#1D3557')
u_text.place(relx=-0.25, rely=0.3, relheight=0.1, relwidth=1)
u_text.config(font=("Helvetica", 32))

u_val = tk.Entry(mainframe, fg='#F1FAEE', bg='#A8DADC')
u_val.place(relx=0.4, rely=0.3, relheight=0.1, relwidth=0.5)
u_val.config(font=("Helvetica", 32))

#V
v_text = tk.Label(mainframe, text="v (m/s) = ", fg='#F1FAEE', bg='#1D3557')
v_text.place(relx=-0.25, rely=0.4, relheight=0.1, relwidth=1)
v_text.config(font=("Helvetica", 32))

v_val = tk.Entry(mainframe, fg='#F1FAEE', bg='#A8DADC')
v_val.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.5)
v_val.config(font=("Helvetica", 32))

#A
a_text = tk.Label(mainframe, text='a(m/s^2)=', fg='#F1FAEE', bg='#1D3557')
a_text.place(relx=-0.25, rely=0.5, relheight=0.1, relwidth=1)
a_text.config(font=("Helvetica", 32))

a_val = tk.Entry(mainframe, fg='#F1FAEE', bg='#A8DADC')
a_val.place(relx=0.4, rely=0.5, relheight=0.1, relwidth=0.5)
a_val.config(font=("Helvetica", 32))

#T
t_text = tk.Label(mainframe, text="t (s) = ", fg='#F1FAEE', bg='#1D3557')
t_text.place(relx=-0.25, rely=0.6, relheight=0.1, relwidth=1)
t_text.config(font=("Helvetica", 32))

t_val = tk.Entry(mainframe, fg='#F1FAEE', bg='#A8DADC')
t_val.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.5)
t_val.config(font=("Helvetica", 32))

def calculate():
	global s
	global u
	global v
	global a
	global t

	s = s()
	u = u()
	v = v()
	a = a()
	t = t()

	if s == None and u == None:
	    u = v - a*t
	    print(u)	

	elif s == None and v == None:
	    v = u + a*t
	    print(v)	

	elif s == None and a == None:
	    a = (v-u)/t
	    print(a)	

	elif s == None and t == None:
	    t = (v-u)/a
	    print(t)	

	if s == None:
	    s=(u+v)*t*0.5
	    print(s)	
	

	#When v == None
	if v == None and u == None:
	    u=(s/t)-0.5*a*t
	    print(u)	

	elif v == None and a == None:
	    a = (2*(s-t*u))/t**2
	    print(a)
	    
	elif v == None and t == None:
	    try:
	        t = (math.sqrt(2*a*s+u**2)-u)/a                             #Checks whether the calculation is possible
	        print(t)                                         #If calculation is possible, the value is printed
	    except ValueError:                                              #If calculation is impossible, error message is printed
	        print("")	

	if v == None:
	    try:                                                            #Checks whether the calculation is possible
	        v = u+a*t
	        print(v)                                         #If calculation is possible, the value is printed
	    except TypeError:
	        print("No real roots for v")                                #If calculation is impossible, error message is printed	
	

	#When a == None
	if a == None and u == None:
	    u = ((2*s)/t)-v
	    print(u)	

	elif a == None and t == None:
	    t = (2*s)/(u+v)
	    print(t)	

	if a == None:
	    a = (v-u)/t
	    print(a)
	    
	#When t == None
	if t == None and u == None:
	    try: 
	        u = math.sqrt((v**2)-(2*a*s))                               #Checks whether the calculation is possible
	        print(u)                                         #If calculation is possible, the value is printed
	    except ValueError:
	        print("No real roots for u")                                #If calculation is impossible, error message is printed
	        	

	if t == None:
	    try:                                                            #Checks whether the calculation is possible
	        t = (v-u)/a                                                 #If calculation is possible, the value is printed
	        print(t)
	    except TypeError:
	        print("Can not solve for t")                                #If calculation is impossible, error message is printed


button = tk.Button(mainframe, text = "GO!", fg='#F1FAEE', bg='#1D3557', command=lambda: calculate())
button.place(relx=0.4, rely=0.8, relheight = 0.15, relwidth=0.25)
button.config(font=("Helvetica", 32))

base.mainloop()





'''
   _________    __    ________  ____    ___  __________  ____ 
  / ____/   |  / /   / ____/ / / / /   /   |/_  __/ __ \/ __ \
 / /   / /| | / /   / /   / / / / /   / /| | / / / / / / /_/ /
/ /___/ ___ |/ /___/ /___/ /_/ / /___/ ___ |/ / / /_/ / _, _/ 
\____/_/  |_/_____/\____/\____/_____/_/  |_/_/  \____/_/ |_|  
                                                             
'''





#BUTTON
# def s():
# 	s = float(s_val.get())
# 	print(s)


# button = tk.Button(mainframe, text = "GO!", fg='#F1FAEE', bg='#1D3557', command=lambda: s())
# button.place(relx=0.4, rely=0.8, relheight = 0.15, relwidth=0.25)
# button.config(font=("Helvetica", 32))

# base.mainloop()