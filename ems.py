from customtkinter import *
from PIL import Image
from tkinter import ttk
from tkinter import ttk,messagebox
import databases


#functions

def delete_all():
    result=messagebox.askyesno('Confirm','Do you really want to delete all the record?')
    if result:
        databases.deleteall_records()
    

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchbox.set('search by')

def search_employee():
   if searchEntry.get()=='':
       messagebox.showerror('Error','Enter value to search')    
   elif searchbox.get()=='Search By':
       messagebox.showerror('Error','please select an option')
   else:
       search_data=databases.search(searchbox.get(),searchEntry.get())
       tree.delete(*tree.get_children())
       for employee in search_data:
         tree.insert('',END,values=employee)
       

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete')
    else:
        databases.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Error',' Data is deleted')
        

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        databases.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','data is updated')

def selection(event):
    selected_items=tree.selection()
    if selected_items:
        row=tree.item(selected_items)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        rolebox.set(row[3])
        genderbox.set(row[4])
        salaryEntry.insert(0,row[5])


def clear(value=False):
    if value :
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    rolebox.set('web developer')
    genderbox.set('Male')
    salaryEntry.delete(0,END)

def treeview_data():
     employees=databases.fetch_employees()
     tree.delete(*tree.get_children())
     for employee in employees:
         tree.insert('',END,values=employee)





def add_employee():
      if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
         messagebox.showerror('Error','All field are required')
      elif databases.id_exists(idEntry.get()):
         messagebox.showerror('Error', 'Id already exists')
      elif not idEntry.get().startswith('EMP'):
          messagebox.showerror('Error', "Invalid Id format use 'EMP' followed by a number..(e.g.,'EMP1')")
          



      else:
         databases.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),genderbox.get(),salaryEntry.get())
         treeview_data()
         clear()
         messagebox.showinfo('Success', 'data is added')


w=CTk()
w.geometry('1150x680+100+10')
w.resizable(False,False)
w.title('Employee Management System')
w.configure(fg_color='black')
logo=CTkImage(Image.open('images.jpg'),size=(1150,180))
logolabel=CTkLabel(w,image=logo,text='')
logolabel.grid(row=0,column=0,columnspan=2)


leftframe=CTkFrame(w,fg_color='black')
leftframe.grid(row=1,column=0,pady=15)

idlabel=CTkLabel(leftframe,text='ID',font=('arial',18,'bold'),text_color='white')
idlabel.grid(row=0,column=0,padx=20)

idEntry=CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
idEntry.grid(row=0,column=1,pady=15,sticky='w')

namelabel=CTkLabel(leftframe,text='Name',font=('arial',18,'bold'),text_color='white')
namelabel.grid(row=1,column=0,padx=20)

nameEntry=CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
nameEntry.grid(row=1,column=1,pady=15,sticky='w')

phonelabel=CTkLabel(leftframe,text='Phone',font=('arial',18,'bold'),text_color='white')
phonelabel.grid(row=2,column=0,padx=20)

phoneEntry=CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
phoneEntry.grid(row=2,column=1,pady=15,sticky='w')

rolelabel=CTkLabel(leftframe,text='Role',font=('arial',18,'bold'),text_color='white')
rolelabel.grid(row=3,column=0,padx=20)
role_options=['web developer','python developer','technical writer',
              'data scientist','IT consultant','UI/UX designer']
rolebox=CTkComboBox(leftframe,values=role_options,width=180,
                    font=('arial',18,'bold'),state='readonly')
rolebox.grid(row=3,column=1)

genderlabel=CTkLabel(leftframe,text='Gender',font=('arial',18,'bold'),text_color='white')
genderlabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_option=['Male','Female']

genderbox=CTkComboBox(leftframe,values=gender_option,width=180,
                    font=('arial',18,'bold'),state='readonly')
genderbox.grid(row=4,column=1)

salarylabel=CTkLabel(leftframe,text='Salary',font=('arial',18,'bold'),text_color='white')
salarylabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')


salaryEntry=CTkEntry(leftframe,font=('arial',18,'bold'),width=180)
salaryEntry.grid(row=5,column=1)




rightframe=CTkFrame(w)
rightframe.grid(row=1,column=1)

search_options=['Id','name','Phone','Role','Gender','Salary']
searchbox=CTkComboBox(rightframe,values=search_options
                    ,state='readonly')
searchbox.grid(row=0,column=0)
searchbox.set('saerch by')

searchEntry=CTkEntry(rightframe)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightframe,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightframe,text='Show All',width=100,command=show_all)
showallButton.grid(row=0,column=3)

tree=ttk.Treeview(rightframe,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')
tree.heading('Id',text='ID')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Gender',text='Gender')
tree.heading('Role',text='Role')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=140)
tree.column('Phone',width=160)
tree.column('Role',width=200)
tree.column('Gender',width=100)
tree.column('Salary',width=140)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',14,'bold'))
style.configure('Treeview',font=('arial',15,'bold'),rowheight=30,background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonframe=CTkFrame(w,fg_color='black')
buttonframe.grid(row=2,column=0,columnspan=2)

newbutton=CTkButton(buttonframe,text='New Employee',font=('arial',14,'bold'),width=160,corner_radius=15,command=lambda: clear(True))
newbutton.grid(row=0,column=0,pady=5)

addbutton=CTkButton(buttonframe,text='Add Employee',font=('arial',14,'bold'),width=160,corner_radius=15,command=add_employee)
addbutton.grid(row=0,column=1,pady=5,padx=5)

updatebutton=CTkButton(buttonframe,text='Update Employee',font=('arial',14,'bold'),width=160,corner_radius=15,command=update_employee)
updatebutton.grid(row=0,column=2,pady=5,padx=5)

deletebutton=CTkButton(buttonframe,text='Delete Employee',font=('arial',14,'bold'),width=160,corner_radius=15,command=delete_employee)
deletebutton.grid(row=0,column=3,pady=5,padx=5)

deleteallbutton=CTkButton(buttonframe,text='DeleteAll',font=('arial',14,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallbutton.grid(row=0,column=4,pady=5,padx=5)



treeview_data()

w.bind('<ButtonRelease>',selection)

w.mainloop()
