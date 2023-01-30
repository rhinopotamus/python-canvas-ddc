# gui building!!!
from tkinter import *

root = Tk()

# Adjust size
root.geometry( "200x200" )
  
# Change the label text
def show():
    label.config( text = clicked.get() )
  
# Dropdown menu options
courseTitles =  [
    "MATH 202", 
    "PHYS 309"
]

# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Choose your course" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *courseTitles )
drop.pack()
  
# Create button, it will change label text
button = Button( root , text = "Submit" , command = show ).pack()
  
# Create Label
label = Label( root , text = " " )
label.pack()
  
# Execute tkinter
root.mainloop()