from tkinter import *
PRICE=0
charges=0
win=Tk()
x=StringVar()
def month():
    s=int(E1.get())
    s1=int(E2.get())
    
    if s==1 or s==2 or s==3:
        PRICE=80
    elif s==4 or s==5 or s==6:
        PRICE=90
    elif s==7 or s==8 or s==9:
        PRICE=120
    else:
        PRICE=100
    charges=s1*PRICE
    charge=str(charges)
    charge=charge+"$"
    x.set(charge)
    #print("THIS WILL CHARGE YOU {}$".format(charges))
    
    
win.geometry('400x400')
L1=Label(win,text="ENTER THE MONTH IN NUMBER ")
L1.grid(row=0,column=0,pady=10)
E1=Entry(win)
E1.grid(row=0,column=1,pady=10)




L1=Label(win,text="ENTER THE NUMBER OF NIGHTS ")
L1.grid(row=1,column=0,pady=10)
E2=Entry(win)
E2.grid(row=1,column=1,pady=10)



B1=Button(win,text="CALCULATE PRICE",command=month)
B1.grid(row=2)

L3=Label(win,text="TOTAL PRICE ")
L3.grid(row=3,column=0,pady=10)
E3=Entry(win,textvariable=x)
E3.grid(row=3,column=1,pady=10)


L3=Label(win,text='''   MonthsRate
1 – 3 (Jan – Mar) $80/night
4 – 6 (Apr – Jun) $90/night
 7 – 9 (Jul – Sept)$120/night
  10 – 12 (Oct – Dec) $100/night ''')
L3.grid(row=4,column=0,pady=20)




win.mainloop()
