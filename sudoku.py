from  tkinter import *
from tkinter import messagebox
def exit():
    window.destroy()                       # assigning exit function to remove that window    
window=Tk()                                # creating a window
window.title("sudoku")                     # giving title to the window 
window.geometry("400x400")                 # giving size to the window
window.config(bg='skyblue')                # giving background color to the window
s=[]                                        
g=globals()                                # creating a global variable and empty list for our convenience 
def submit():
    for i in range (9): 
        for j in range(9):
            s.append(g[f'var{i}{j}'].get())   # appending the values of the entry boxes to the list s
    rows=[]
    coloums=[]
    check_rows=[]
    check_coloums=[]
    b1=[]
    boxes=[]                                   # creating empty lists for checking the rows,coloums and boxes
    for i in range (0,81,9):
        check_rows.append(len(set(s[i:i+9])))
        rows.append(s[i:i+9])
    for j in range (0,9):
        check_coloums.append(len(set(s[j::9])))
        coloums.append(s[j::9])                # appending rows and coloums to the list and len of set checkrows and checkcolumns
    for k in range(0,9,3):
        for l in range(0,9,3):
            for i in range (0+k,3+k):
                for j in range(0+l,3+l):
                    b1.append(rows[i][j])      
    for i in range (0,81,9):
        boxes.append(len(set(b1[i:i+9])))       # appending len of set of boxes to the list boxes
    if (9 in check_rows and len(set(check_rows))==1) and (9 in check_coloums and len(set(check_coloums))==1) and (9 in boxes  and len(set(boxes))==1):
        messagebox.showinfo('game over','you won the game')
    else:
        messagebox.showinfo('game over','you lost the game')
def formation_hard():
    frame=Frame(window,bd=(7))                  # creating a frame for the entry boxes
    frame.pack()     
    for i in range (9):
        for j in range (9):
            g[f'var{i}{j}']=Entry(frame,width=4,bg='gold')        # creating entry boxes
            g[f'var{i}{j}'].grid(row=i,column=j)                    # packing  the entry boxes in a frame
            if i==0 and j==1:
                g[f'var{i}{j}'].insert(0,8)                         # assigning the entry value with its index value
                g[f'var{i}{j}'].config(state=DISABLED)              # disabling the entry box to avoid the changes 
            elif i==0 and j==2:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==2:
                g[f'var{i}{j}'].insert(0,1)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==0 and j==4:
                g[f'var{i}{j}'].insert(0,1)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==0 and j==7:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==0 and j==8:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==3:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==8:
                g[f'var{i}{j}'].insert(0,2)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==3 and j==1:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==3 and j==6:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==4:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==6:
                g[f'var{i}{j}'].insert(0,2)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==0:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==3:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==7:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==8:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==1:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==4:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==7:
                g[f'var{i}{j}'].insert(0,8)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==8:
                g[f'var{i}{j}'].insert(0,1)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==7 and j==6:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==8 and j==0:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==8 and j==5:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
    exit_button=Button(window,text="exit",command=exit)             
    exit_button.pack(side=LEFT)
    submit_button=Button(window,text="submit",command=submit)
    submit_button.pack(side=RIGHT)                      # giving the commands to the buttons and its position in the window
    frame_1.destroy()                                   # destroying the previous frame which shows the level of game          
def formation_medium():
    frame=Frame(window,bd=(7))
    frame.pack()
    for i in range (9):
        for j in range (9):
            g[f'var{i}{j}']=Entry(frame,width=4,bg='gold')
            g[f'var{i}{j}'].grid(row=i,column=j)
            if i==0 and j==0:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==0 and j==8:
                g[f'var{i}{j}'].insert(0,2)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==0:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==2:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==4:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==5:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==2:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==3:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==4:
                g[f'var{i}{j}'].insert(0,8)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==7:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==3 and j==0:
                g[f'var{i}{j}'].insert(0,8)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==3 and j==1:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==3 and j==8:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==0:
                g[f'var{i}{j}'].insert(0,1)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==1:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==4:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==5:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==6:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==7:
                g[f'var{i}{j}'].insert(0,2)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==8:
                g[f'var{i}{j}'].insert(0,8)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==0:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==1:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==3:
                g[f'var{i}{j}'].insert(0,8)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==4:
                g[f'var{i}{j}'].insert(0,1)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==5:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==6:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==7:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==3:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==4:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==6:
                g[f'var{i}{j}'].insert(0,2)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==8:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==7 and j==0:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==7 and j==6:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==7 and j==7:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==8 and j==2:
                g[f'var{i}{j}'].insert(0,8)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==8 and j==5:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
    exit_button=Button(window,text="exit",command=exit)
    exit_button.pack(side=LEFT)
    submit_button=Button(window,text="submit",command=submit)
    submit_button.pack(side=RIGHT)
    frame_1.destroy()
def formation_easy():
    frame=Frame(window,bd=(7))
    frame.pack()
    for i in range (9):
        for j in range (9):
            g[f'var{i}{j}']=Entry(frame,width=4,bg='gold')
            g[f'var{i}{j}'].grid(row=i,column=j)
            if i==0 and j==4:
                g[f'var{i}{j}'].insert(0,8)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==0 and j==5:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==0 and j==8:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==0:
                g[f'var{i}{j}'].insert(0,1)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==1:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==4:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==7:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==1 and j==8:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==0:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==2:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==4:
                g[f'var{i}{j}'].insert(0,1)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==5:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==2 and j==7:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==3 and j==0:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==3 and j==4:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==3 and j==5:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==2:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==3:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==4 and j==8:
                g[f'var{i}{j}'].insert(0,1)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==0:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==1:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==4:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==6:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==7:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==5 and j==8:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==0:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==2:
                g[f'var{i}{j}'].insert(0,4)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==4:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==5:
                g[f'var{i}{j}'].insert(0,8)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==6 and j==7:
                g[f'var{i}{j}'].insert(0,2)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==7 and j==0:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==7 and j==1:
                g[f'var{i}{j}'].insert(0,6)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==7 and j==4:
                g[f'var{i}{j}'].insert(0,2)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==7 and j==5:
                g[f'var{i}{j}'].insert(0,9)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==7 and j==7:
                g[f'var{i}{j}'].insert(0,5)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==8 and j==1:
                g[f'var{i}{j}'].insert(0,2)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==8 and j==6:
                g[f'var{i}{j}'].insert(0,3)
                g[f'var{i}{j}'].config(state=DISABLED)
            elif i==8 and j==8:
                g[f'var{i}{j}'].insert(0,7)
                g[f'var{i}{j}'].config(state=DISABLED)
    exit_button=Button(window,text="exit",command=exit)
    exit_button.pack(side=LEFT)
    submit_button=Button(window,text="submit",command=submit)
    submit_button.pack(side=RIGHT)
    frame_1.destroy()
def start_game():
    global frame_1                                              #frame_1 is the frame which contains the buttons of the levels
    frame_1=Frame(window)
    frame_1.pack()
    hard=Button(frame_1,text="hard level",command=formation_hard)
    hard.grid(row=0,column=0)
    medium=Button(frame_1,text="medium level",command=formation_medium)
    medium.grid(row=1,column=0)  
    easy=Button(frame_1,text="easy level",command=formation_easy)
    easy.grid(row=2,column=0)                                     # giving the buttons their positions and commands  
    start_button.destroy()                                        # destroying the start button frame after pressing it
start_button=Button(window,text="start game",command=start_game)
start_button.pack()                                               # giving the start button its position
window.mainloop()                                                  # mainloop is used to keep the window open