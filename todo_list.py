from tkinter import *
from tkinter import ttk 

class ToDo :
    def __init__(self,root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry('650x410+300+150')

        self.label1 = Label(self.root, text = "To-Do-List", font = 'Gadugi, 24 bold' , width=12, bd=4, bg = "Black" , fg = "White")
        self.label1.pack(side="top", fill = BOTH)

        self.label2 = Label(self.root, text = "Add Tasks", font = 'Gadugi, 16' , width=12, bd=4, bg = "Black" , fg = "White")
        self.label2.place(x=50,y=54)

        self.label3 = Label(self.root, text = "Tasks", font = 'Gadugi, 16' , width=12, bd=4, bg = "Black" , fg = "White")
        self.label3.place(x=400,y=54)

        self.main_text = Listbox(self.root, height = 10 , bd = 5 ,width = 23 , font = "Gadugi, 18 italic bold" )
        self.main_text.place(x=310,y=100)

        self.text = Text(self.root, height = 2, bd = 4, width = 32 , font = "Gadugi, 8 ")
        self.text.place(x=34, y=100)

        #***ADD TASK***
        
        def add():
            content = self.text.get(1.0,END)
            self.main_text.insert(END, content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        #***DELETE TASK***
            
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt','r+')as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line :
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)  

        with open('data.txt','r') as file :
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        self.button1 = Button(self.root, text = 'Add', font = 'sarif, 18 bold italic', width = 12, bd = 4, bg = 'Black', fg = 'White', command = add)
        self.button1.place(x=35, y = 150)
        self.button2 = Button(self.root, text = 'Delete', font = 'sarif, 18 bold italic', width = 12, bd = 4, bg = 'Black', fg = 'White', command = delete)      
        self.button2.place(x=35 , y = 220)

def main():

    root = Tk() 
    ui = ToDo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
