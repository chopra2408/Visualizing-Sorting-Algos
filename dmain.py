from tkinter import *
import customtkinter 
from tkinter import ttk
import random
from colors import *

# Importing algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
# Main window
''' 
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)'''
root = customtkinter.CTk()
root.geometry("1000x700")
root.title("Sorting with GUI")
#style = ttk.Style(root)
#style.configure('lefttab.TNotebook', tabposition='wn',)

algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = ['Fast', 'Medium', 'Slow']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    root.update_idletasks()


# Randomly generate array
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    else:
        counting_sort(data, drawData, timeTick)


### User interface ###
#rframe = Frame(root, width= 900, height=300)
#rframe.grid(row=0, column=0, padx=10, pady=5)
label1 = customtkinter.CTkLabel(root, text="Algorithm: ")
label1.grid(column=0, row=0,padx=10,pady=5)
algo_menu = ttk.Combobox(root, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

label2 = customtkinter.CTkLabel(root,text="Sorting Speed ")
label2.grid(column = 10, row=1)
speed_menu = ttk.Combobox(root, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = customtkinter.CTkCanvas(root, width=800, height=400)
canvas.grid(row=1, column=0, padx=10, pady=5)

button1 = customtkinter.CTkButton(root,text="Sort",command=sort)
button1.grid(row=2, column=1, padx=5, pady=5)

button2 = customtkinter.CTkButton(root,text="Generate Array",command=generate)
button2.grid(row=2, column=0, padx=5, pady=5)
'''
master = Frame(root,width= 900, height=300)
master.grid(row=0,column=0)#,relx=10,rely=5)
l1 = customtkinter.CTkLabel(master=root,text="Algorithm: ")
l1.grid(row=0, column=0,relx=10,rely=5,sticky=W)
algo_menu = ttk.Combobox(master=root, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, relx=5, rely=5)
algo_menu.current(0)
l2 = customtkinter.CTkLabel(master=root, text="Sorting Speed: ")
l2.grid(row=1, column=0, relx=10, rely=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)
'''
'''
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)
'''
'''
b1 = customtkinter.CTkButton(master=root,text = "Sort", command=sort )
b1.place(relx=0.5, rely=0.5,anchor=E)
b3 = customtkinter.CTkButton(master=root,text="Generate Array",command=generate)
b3.place(relx=0.5,rely=0.5,anchor = W)
self.label = customtkinter.CTkLabel(master)
'''
root.mainloop()