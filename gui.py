import tkinter as tk
import main

window = tk.Tk()
window.title("Binary Number Search")
window.geometry("400x400")

times_played = 0
lists_generated = 0
lists_shown = 0

label1 = tk.Label()
label1.grid(column=0, row=0)

label3 = tk.Label()
label3.grid(column=0, row=6)


def gen_list():
    global generated_list
    global label1
    global lists_generated
    generated_list = main.list_gen(20, 100, 1, 100)
    label1.config(text=f"This program just generated a list of {len(generated_list)} random integers from {generated_list[0]} to {generated_list[-1]}.")
    lists_generated += 1

gen_list()

label3.config(text=f"You have searched for {times_played} numbers and generated {lists_generated} lists.")

def execute(): 
    global user_response
    global num_index
    global generated_list
    user_response = int(entry1.get())
    entry1.delete(0, len(entry1.get())+1)
    num_index = main.search(generated_list, user_response)

def display_index():
    global times_played
    execute()
    answer = main.respond(num_index, user_response)
    display = tk.Text(master=window, width=30, height=2, exportselection=False, wrap="word")
    display.grid(column=0, row=4)
    display.insert(tk.END, answer)
    times_played += 1
    
    label3.config(text=f"You have searched for {times_played} numbers and generated {lists_generated} lists.")

def show_list():
    global lists_shown
    global generated_list
    display2 = tk.Text(master=window, width=30, height=10, exportselection=False, wrap="word")
    display2.grid(column=0, row=8)
    display2.insert(tk.END, generated_list)
    lists_shown += 1
    
def button2_pressed():
    gen_list()
    global lists_shown
    if lists_shown > 0: show_list()

label2 = tk.Label(text="What number would you like to search for in the list?")
label2.grid(column=0, row=1)

entry1 = tk.Entry(exportselection=False)
entry1.grid(column=0, row=2)

button1 = tk.Button(text="Search for number", command=display_index)
button1.grid(column=0, row=3)

button2 = tk.Button(text="Generate new list", command=button2_pressed)
button2.grid(column=0, row=5)

button3 = tk.Button(text="Show list", command=show_list)
button3.grid(column=0, row=7)

window.mainloop()