from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('DSEditor')
root.iconbitmap('/Users/daksh/Downloads/Notion_app_logo.png')
root.geometry("900x490")

global open_status_name
open_status_name = False

def new_file():
    my_text.delete('1.0', END)
    root.title('* Untitled')
    status_bar.config(text='New File    ')
    global open_status_name
    open_status_name = False

def open_file():
    my_text.delete('1.0', END)
    text_file = filedialog.askopenfilename(initialdir='/Users/daksh/Desktop', title='Open File', filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'), ('Python Files', '*.py'), ('All files', '*.*')))
    if text_file:   
        global open_status_name
        open_status_name = text_file
    name = text_file
    status_bar.config(text=name)
    name = name.replace("/Users/daksh/Desktop/", "")
    root.title(f'{name}')

    text_file = open(text_file, 'r')
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

**def bold_it():
    bold_font = font.Font(my_text, my_text.cget('font'))
    bold_font.configure(weight='bold')
    my_text.tag_configure('bold', font=bold_font)
    current_tags = my_text.tag_names("sel.first")
    if 'bold' in current_tags:
        my_text.tag_remove('bold', "sel.first", "sel.last")
    else:
        my_text.tag_add('bold', "sel.first", "sel.last")**


def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir='/Users/daksh/Desktop', filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'), ('Python Files', '*.py'), ('All files', '*.*')))
    if text_file:
        name = text_file
        global open_status_name
        open_status_name = text_file
        status_bar.config(text=f'Saved as - {name}')
        name = name.replace('/Users/daksh/Desktop/', '')
        root.title(f'{name}')
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.config(text=f'Saved - {open_status_name}')
    else:
        save_as_file()

toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width = 97, height = 25, font = ('TkDefaultFont', 16), selectbackground='yellow', selectforeground='black', undo=True, yscrollcommand=text_scroll.set, highlightthickness=0, padx=5)
my_text.pack()

text_scroll.config(command=my_text.yview)

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=save_as_file)
file_menu.add_separator()

edit_menu = Menu(my_menu, tearoff=True)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
edit_menu.add_command(label='Undo')
file_menu.add_command(label='Redo')

status_bar = Label(root, text='Ready      ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W)

root.mainloop()
