#Assignment 1
#Priyanshu Sivamurthy Gangavati
#22B2165

from tkinter import *
import datetime
from winotify import Notification

n = 0

root = Tk()

def function_delete():
        select = listbox.curselection()
        listbox.delete(select[0])

def function_add():

        def add():
                input_task = t_entry.get()
                input_date = d_entry.get()
                input_time = time_entry.get()
                newstr = input_time + "  " + input_date + "  " + input_task
                listbox.insert(END, newstr)
                root2.destroy()

                time2 = Today_date_time.strftime("%H:%M:%S")
                date2 = Today_date_time.strftime("%d/%m/%Y")

                check2 = time2 + " " + date2
                print(newstr[:19])
                print("Check = ",check2)
                if(newstr[:19] == check2):
                        toast = Notification(app_id="To Do List Organiser",
                                             title = "You have a new task",
                                             msg=input_task,
                                             duration = "short")
                        toast.show()


                        
        root2 = Tk()
                
        root2.geometry("500x200")
        root2.minsize(500,200)
        root2.maxsize(500,200)
        root2.title("Add task:-")
        root2.config(bg = "lavender")

        task = Label(root2,text = "Enter Task : ", pady = 5,font = "arial 12",
                      bg = "lavender", fg = "black")
        user_date = Label(root2, text = "Enter Date :\nEg- 24/11/2003 ", 
                        pady = 5, font = "arial 12", bg = "lavender", fg = "black")
        user_time = Label(root2, text = "Enter time(24 hr format) :\nEg- 09:31:48 ",
                        pady = 5,font = "arial 12", bg = "lavender", fg = "black")
        task.grid(row = 1)
        user_date.grid(row=3)
        user_time.grid(row=5)

        t_val = StringVar()
        d_val = StringVar()
        time_val = StringVar()

        t_entry = Entry(root2, textvariable=t_val, font = "arial 15")
        d_entry = Entry(root2, textvariable=d_val,font = "arial 15")
        time_entry = Entry(root2, textvariable=time_val,font = "arial 15")

        t_entry.grid(row = 1, column = 3)
        d_entry.grid(row = 3, column = 3)
        time_entry.grid(row = 5, column = 3) 
        
        b = Button(root2,text = "Add",fg = "red", font = "arial 13", pady = 2,
                    command = add).grid(row = 10, column = 2)
        Today_date_time = datetime.datetime.now()

        root2.mainloop()


root.geometry("400x700")
root.minsize(200,350)
root.maxsize(400,700)
root.title("To Do List Organiser")

l = Label(text = "Welcome",font = "algerian 20 italic",bg = "white", 
          fg = "dark turquoise", pady = 10, padx = 200).pack(side = TOP)

root.config(bg = "lavender")

f = Frame(root, borderwidth = 10).pack()

b3 = Button(f,bg = "light blue",fg = "black", text = "- Delete task",
font = "Bahnschrift 15 italic", padx = 130, pady = 10, command=function_delete).pack(side = BOTTOM)

b1 = Button(f,bg = "light blue",fg = "black", text = "+ Add task",
font = "Bahnschrift 15 italic", padx = 140, pady = 10, command = function_add).pack(side = BOTTOM)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill = Y)
listbox=  Listbox(root,bg = "lavender", fg = "black",height=650, width = 350,
                  font = "Bahnschrift 15 italic" ,yscrollcommand=scrollbar.set)
listbox.pack()
scrollbar.config(command=listbox.yview)

root.mainloop()