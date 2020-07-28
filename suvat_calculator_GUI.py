import tkinter as tk
import math

HEIGHT = 700			  #<-- Changes the height of the window
WIDTH = 550				  #<-- Changes the height of the window

#Colours
PrussianBlue = '#1D3557'
PowderBlue = '#A8DADC'
ImperialRed = '#E63946'
Honeydew = '#F1FAEE'
Xiketic = '#04030F'


#Starting variables with blank values
s = None
u = None
v = None
a = None
t = None

'''
    __  ______    _____   __
   /  |/  /   |  /  _/ | / /
  / /|_/ / /| |  / //  |/ /
 / /  / / ___ |_/ // /|  /
/_/  /_/_/  |_/___/_/ |_/

    ________  ___   ______________________  _   _______
   / ____/ / / / | / / ____/_  __/  _/ __ \/ | / / ___/
  / /_  / / / /  |/ / /     / /  / // / / /  |/ /\__ \
 / __/ / /_/ / /|  / /___  / / _/ // /_/ / /|  /___/ /
/_/    \____/_/ |_/\____/ /_/ /___/\____/_/ |_//____/


'''
#ERRORS
#Creating error message for when input is not a number or blank
def ValueErrorMsg():
    global error
    error = tk.Label(mainframe, text="ERROR: Invalid Input. Enter only a number or leave blank", fg=ImperialRed, bg=PrussianBlue)
    error.place(relx=0, rely=0.7, relheight=0.1, relwidth=1)
    error.config(font=("Helvetica", 12))

def InputErrorMessage():
    global inputerror
    inputerror = tk.Label(mainframe, text="ERROR: Invalid Input. Enter at least 3 variables", fg=ImperialRed, bg=PrussianBlue)
    inputerror.place(relx=0, rely=0.7, relheight=0.1, relwidth=1)
    inputerror.config(font=("Helvetica", 12))


#functions for the clear button to remove all text from entry boxes
def clear():
    s_val.delete(0,"end")
    u_val.delete(0,"end")
    v_val.delete(0,"end")
    a_val.delete(0,"end")
    t_val.delete(0,"end")


def errorclear():
    global error
    global inputerror
    error.destroy()
    inputerror.destroy()


#Storing the values for SUVAT as either a float or a blank
def userinput(input):
	while True:
		try:
			return float(input.get())
		except ValueError:
			if input.get() == "":
				break
			else:
				return ValueErrorMsg()


'''
   ________  ______
  / ____/ / / /  _/
 / / __/ / / // /
/ /_/ / /_/ // /
\____/\____/___/

'''
#Setting the size of the window
root = tk.Tk()
root.configure(bg=PrussianBlue)
root.title("SUVAT Calculator")
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg=PrussianBlue, bd=0, highlightthickness=0)
canvas.pack()


mainframe = tk.Frame(root, bg=PrussianBlue, bd=0)
mainframe.place(relx = 0.05, rely=0.05, relheight=0.9, relwidth=0.9)

#Main title
title = tk.Label(mainframe, text="SUVAT Calculator", fg=Honeydew, bg=PrussianBlue)			#SUVAT Calculator Title
title.place(relx=0, rely=0, relheight=0.15, relwidth=1)
title.config(font=("Helvetica", 44))

#Divider
divider = tk.Label(mainframe, bg='#E63946')
divider.place(relx=0, rely=0.15, relheight=0.005, relwidth=1)

#S
s_text = tk.Label(mainframe, text="s (m) = ", fg=Honeydew, bg=PrussianBlue)
s_text.place(relx=-0.25, rely=0.2, relheight=0.1, relwidth=1)
s_text.config(font=("Helvetica", 32))

s_val = tk.Entry(mainframe, fg=Honeydew, bg=PowderBlue)
s_val.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)
s_val.config(font=("Helvetica", 32))


#U
u_text = tk.Label(mainframe, text="u (m/s) = ", fg=Honeydew, bg=PrussianBlue)
u_text.place(relx=-0.25, rely=0.3, relheight=0.1, relwidth=1)
u_text.config(font=("Helvetica", 32))

u_val = tk.Entry(mainframe, fg=Honeydew, bg=PowderBlue)
u_val.place(relx=0.4, rely=0.3, relheight=0.1, relwidth=0.55)
u_val.config(font=("Helvetica", 32))

#V
v_text = tk.Label(mainframe, text="v (m/s) = ", fg=Honeydew, bg=PrussianBlue)
v_text.place(relx=-0.25, rely=0.4, relheight=0.1, relwidth=1)
v_text.config(font=("Helvetica", 32))

v_val = tk.Entry(mainframe, fg=Honeydew, bg=PowderBlue)
v_val.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.55)
v_val.config(font=("Helvetica", 32))

#A
a_text = tk.Label(mainframe, text='a(m/s^2)=', fg=Honeydew, bg=PrussianBlue)
a_text.place(relx=-0.25, rely=0.5, relheight=0.1, relwidth=1)
a_text.config(font=("Helvetica", 32))

a_val = tk.Entry(mainframe, fg=Honeydew, bg=PowderBlue)
a_val.place(relx=0.4, rely=0.5, relheight=0.1, relwidth=0.55)
a_val.config(font=("Helvetica", 32))

#T
t_text = tk.Label(mainframe, text="t (s) = ", fg=Honeydew, bg=PrussianBlue)
t_text.place(relx=-0.25, rely=0.6, relheight=0.1, relwidth=1)
t_text.config(font=("Helvetica", 32))

t_val = tk.Entry(mainframe, fg=Honeydew, bg=PowderBlue)
t_val.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.55)
t_val.config(font=("Helvetica", 32))

#Errors
error = tk.Label(mainframe, text="ERROR: Invalid Input. Enter only a number or leave blank", fg=ImperialRed, bg=PrussianBlue)
inputerror = tk.Label(mainframe, text="ERROR: Invalid Input. Enter at least 3 variables", fg=ImperialRed, bg=PrussianBlue)
'''
   _________    __    ________  ____    ___  __________  ____
  / ____/   |  / /   / ____/ / / / /   /   |/_  __/ __ \/ __ \
 / /   / /| | / /   / /   / / / / /   / /| | / / / / / / /_/ /
/ /___/ ___ |/ /___/ /___/ /_/ / /___/ ___ |/ / / /_/ / _, _/
\____/_/  |_/_____/\____/\____/_____/_/  |_/_/  \____/_/ |_|

'''
def calculate():
        global s
        global u
        global v
        global a
        global t

        s = userinput(s_val)
        u = userinput(u_val)
        v = userinput(v_val)
        a = userinput(a_val)
        t = userinput(t_val)

        if s == None and u == None and v == None:
            return InputErrorMessage()
        elif s == None and u == None and a == None:
            return InputErrorMessage()
        elif s == None and u == None and t == None:
            return InputErrorMessage()
        elif s == None and v == None and a == None:
            return InputErrorMessage()
        elif s == None and v == None and t == None:
            return InputErrorMessage()
        elif s == None and a == None and t == None:
            return InputErrorMessage()
        elif u == None and v == None and a == None:
            return InputErrorMessage()
        elif u == None and v == None and t == None:
            return InputErrorMessage()
        elif u == None and a == None and t == None:
            return InputErrorMessage()
        elif v == None and a == None and t == None:
            return InputErrorMessage()


        if s == None and u == None:
            u = v - a*t
            u_val.insert(0, '%.3f' % u)

        elif s == None and v == None:
            v = u + a*t
            v_val.insert(0, '%.3f' % v)

        elif s == None and a == None:
            a = (v-u)/t
            a_val.insert(0, '%.3f' % a)

        elif s == None and t == None:
            t = (v-u)/a
            t_val.insert(0, '%.3f' % t)

        if s == None:
            s=(u+v)*t*0.5
            s_val.insert(0, '%.3f' % s)


	#When v == None
        if v == None and u == None:
            u=(s/t)-0.5*a*t
            u_val.insert(0, '%.3f' % u)

        elif v == None and a == None:
            a = (2*(s-t*u))/t**2
            a_val.insert(0, '%.3f' % a)

        elif v == None and t == None:
            try:
                t = (math.sqrt(2*a*s+u**2)-u)/a             #Checks whether the calculation is possible
                t_val.insert(0, '%.3f' % t)                 #If calculation is possible, the value is printed
            except ValueError:                              #If calculation is impossible, error message is printed
                t_val.insert(0, "")

        if v == None:
            try:                                            #Checks whether the calculation is possible
                v = u+a*t
                v_val.insert(0, '%.3f' % v)                 #If calculation is possible, the value is printed
            except TypeError:
                v_val.insert(0, "No real roots for v")      #If calculation is impossible, error message is printed


	#When a == None
        if a == None and u == None:
            u = ((2*s)/t)-v
            u_val.insert(0, '%.3f' % u)

        elif a == None and t == None:
            t = (2*s)/(u+v)
            t_val.insert(0, '%.3f' % t)

        if a == None:
            a = (v-u)/t
            a_val.insert(0, '%.3f' % a)

	#When t == None
        if t == None and u == None:
            try:
                u = math.sqrt((v**2)-(2*a*s))               #Checks whether the calculation is possible
                u_val.insert(0, '%.3f' % u)                 #If calculation is possible, the value is printed
            except ValueError:
                u_val.insert(0, "No real roots for u")      #If calculation is impossible, error message is printed


        if t == None:
            try:                                            #Checks whether the calculation is possible
                t = (v-u)/a                                 #If calculation is possible, the value is printed
                t_val.insert(0, '%.3f' % t)
            except TypeError:
                t_val.insert(0, "Can't solve for t")        #If calculation is impossible, error message is printed




#Button to calculate values
goButton = tk.Button(mainframe, text = "GO!", fg=Xiketic, bg=PrussianBlue, command=lambda: [errorclear(), calculate()])     #<-- Go button runs calculate() function
goButton.place(relx=0.55, rely=0.8, relheight = 0.15, relwidth=0.25)
goButton.config(font=("Helvetica", 32))

#Button to clear values
clearButton = tk.Button(mainframe, text = "Clear", fg=Xiketic, bg=PrussianBlue, command=lambda: [errorclear(), clear()])  #<-- Clear button runs clear() function
clearButton.place(relx=0.2, rely=0.8, relheight = 0.15, relwidth=0.25)
clearButton.config(font=("Helvetica", 32))


root.mainloop()



#In memory of David Rogers (1943-2020)
