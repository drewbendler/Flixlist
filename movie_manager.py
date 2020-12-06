from tkinter import *
from tkinter import messagebox
from tkinter import IntVar
from db import Database

db = Database('flixlist.db')


def populate_list():
    movie_list.delete(0, END)
    for row in db.fetch():
        movie_list.insert(END, row)


def clear_txt():
    movie_title_entry.delete(0, END)
    genre_label_entry.delete(0, END)
    cinematography_label_entry.delete(0, END)
    set_design_label_entry.delete(0, END)
    music_label_entry.delete(0, END)
    dialogue_label_entry.delete(0, END)
    plot_label_entry.delete(0, END)
    acting_label_entry.delete(0, END)


def add_item():
    entries = [
        cinematography_txt.get(),
        set_design_txt.get(),
        music_txt.get(),
        dialogue_txt.get(),
        plot_txt.get(),
        acting_txt.get()
    ]
    avg = sum(entries) / len

    if movie_txt.get() == '' or genre_txt.get(
    ) == '' or cinematography_txt.get() == '' or set_design_txt.get(
    ) == '' or music_txt.get() == '' or dialogue_txt.get(
    ) == '' or plot_txt.get() == '' or acting_txt.get == '':
        messagebox.showerror('Required field', 'Please include all fields')
        return
    db.insert(movie_txt.get(), genre_txt.get(), cinematography_txt.get(),
              set_design_txt.get(), music_txt.get(), dialogue_txt.get(),
              plot_txt.get(), acting_txt.get())
    movie_list.delete(0, END)
    movie_list.insert(END, (movie_txt.get(), genre_txt.get()))
    movie_list.insert(int(avg))
    clear_txt()
    populate_list()

    print(avg)


def select_item(event):
    try:
        global selected_item
        index = movie_list.curselection()[0]
        selected_item = movie_list.get(index)

        movie_title_entry.delete(0, END)
        movie_title_entry.insert(END, selected_item[1])

        genre_label_entry.delete(0, END)
        genre_label_entry.insert(END, selected_item[2])

        cinematography_label_entry.delete(0, END)
        cinematography_label_entry.insert(END, selected_item[3])

        set_design_label_entry.delete(0, END)
        set_design_label_entry.insert(END, selected_item[4])

        music_label_entry.delete(0, END)
        music_label_entry.insert(END, selected_item[5])

        dialogue_label_entry.delete(0, END)
        dialogue_label_entry.insert(END, selected_item[6])

        plot_label_entry.delete(0, END)
        plot_label_entry.insert(END, selected_item[7])

        acting_label_entry.delete(0, END)
        acting_label_entry.insert(END, selected_item[8])
    except IndexError:
        pass


def delete_item():
    db.remove(selected_item[0])
    clear_txt()
    populate_list()


def update_item():
    db.update(selected_item[0], movie_txt.get(), genre_txt.get(),
              cinematography_txt.get(), set_design_txt.get(), music_txt.get(),
              dialogue_txt.get(), plot_txt.get(), acting_txt.get())
    populate_list()


# create window
app = Tk()

# Title
movie_txt = StringVar()
movie_title = Label(app, text='Title:', font=('bold', 14), pady=10)
movie_title.grid(row=0, column=0, sticky=W)
movie_title_entry = Entry(app, textvariable=movie_txt)
movie_title_entry.grid(row=0, column=1)

# Genre
genre_txt = StringVar()
genre_label = Label(app, text='Genre:', font=('bold', 14))
genre_label.grid(row=0, column=2, sticky=W)
genre_label_entry = Entry(app, textvariable=genre_txt)
genre_label_entry.grid(row=0, column=3)

# Cinematography
cinematography_txt = DoubleVar()
cinematography_label = Label(app, text="Cinematography:", font=('bold', 14))
cinematography_label.grid(row=1, column=0, stick=W)
cinematography_label_entry = Entry(app, textvariable=cinematography_txt)
cinematography_label_entry.grid(row=1, column=1)

# Set Design
set_design_txt = DoubleVar()
set_design_label = Label(app, text="Set Design:", font=('bold', 14))
set_design_label.grid(row=0, column=4, sticky=W)
set_design_label_entry = Entry(app, textvariable=set_design_txt)
set_design_label_entry.grid(row=0, column=5)

# Acting
acting_txt = DoubleVar()
acting_label = Label(app, text="Acting:", font=('bold', 14), pady=20)
acting_label.grid(row=2, column=2, sticky=W)
acting_label_entry = Entry(app, textvariable=acting_txt)
acting_label_entry.grid(row=2, column=3)

# Music/Sound
music_txt = DoubleVar()
music_label = Label(app, text="Music/Sound:", font=('bold', 14))
music_label.grid(row=1, column=2, sticky=W)
music_label_entry = Entry(app, textvariable=music_txt)
music_label_entry.grid(row=1, column=3)

# Dialogue
dialogue_txt = DoubleVar()
dialogue_label = Label(app, text="Dialogue:", font=('bold', 14))
dialogue_label.grid(row=1, column=4, sticky=W)
dialogue_label_entry = Entry(app, textvariable=dialogue_txt)
dialogue_label_entry.grid(row=1, column=5)

# Plot
plot_txt = DoubleVar()
plot_label = Label(app, text="Plot:", font=('bold', 14))
plot_label.grid(row=2, column=0, sticky=W)
plot_label_entry = Entry(app, textvariable=plot_txt)
plot_label_entry.grid(row=2, column=1)

# movieList
movie_list = Listbox(app, height=8, width=100, border=1)
movie_list.grid(row=5, column=0, columnspan=8, rowspan=6, pady=20, padx=5)

# scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=5, column=8)
# set scrollbar to listbox
movie_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=movie_list.yview)

# Bind select
movie_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Movie', width=12, command=add_item)
add_btn.grid(row=4, column=1, pady=20)

delete_btn = Button(app, text='Delete Movie', width=12, command=delete_item)
delete_btn.grid(row=4, column=2)

update_btn = Button(app, text='Edit Movie', width=12, command=update_item)
update_btn.grid(row=4, column=3)

clear_btn = Button(app, text='Clear fields', width=12, command=clear_txt)
clear_btn.grid(row=4, column=4)

# populate data
populate_list()

app.title('FlixList')
app.geometry('950x750')

# start program
app.mainloop()
