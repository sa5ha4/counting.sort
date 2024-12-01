import tkinter


#loga veidošana
rows = 25
cols = 25
tile_size = 30

window_width = tile_size * cols
window_height = tile_size * rows

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = tkinter.Tk()
window.title("Counting Sort")
window.resizable(False, False)

#Canvas veidošana, lai parādītu skaitļus
canvas = tkinter.Canvas(window, bg="black", width = window_width, height = window_height)
canvas.pack()
window.update()

#Logs parādās centrā (nestrāda)
def center_window(window):
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")

#Skaitīšanas kārtošanas funkcija (Counting Sort)
def counting_sort(numbers):
    if len(numbers) == 0:
        return []

    #maksimālās un minimālās vērtības

    max_num = max(numbers)
    min_num = min(numbers)

    range_of_elements = max_num - min_num + 1
    count = [0] * range_of_elements
    output = [0] * len(numbers)

    for num in numbers:
        count[num - min_num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(numbers) - 1, -1, -1):
        output[count[numbers[i] - min_num] - 1] = numbers[i]
        count[numbers[i] - min_num] -= 1

    return output

#Funkcija skaitļu parādīšanai uz canvas
def display_numbers(original_numbers, sorted_numbers):
    canvas.delete("all")
    canvas.create_text(20, 10, text="Numbers:", fill="#c26bbc", font = "System 20", anchor="nw")
    for index, num in enumerate(original_numbers):
        canvas.create_text(30, 50 + index * 30, text=num, fill="#ab5e95", font = "System 18", anchor="nw")
    
    #Parādīt sakārtotus skaitļus

    canvas.create_text(20, 80 + len(original_numbers) * 20 + 20, text="Sorted data:", fill="#8bc26b",  font = "System 20", anchor="nw")
    for index, num in enumerate(sorted_numbers):
        canvas.create_text(30, 90 + len(original_numbers) * 30 + index * 30 + 20, text=num, fill="#83ab5e",  font = "System 18", anchor="nw")

#Funkcija skaitļu šķirošanai
def sort_numbers():
    input_numbers = entry.get().split(",")
    input_numbers = [num.strip() for num in input_numbers]
    
    valid_numbers = []
    for num_str in input_numbers:
        try:
            num = int(num_str)
            valid_numbers.append(num)
        except ValueError:
            canvas.create_text(20, 20, font = "System 20", text="Incorrect data", fill="white", anchor="nw")
            print(f"Incorrect data: {num_str}")
    
    sorted_numbers = counting_sort(valid_numbers)
    display_numbers(valid_numbers, sorted_numbers)

#Datu ievade
entry = tkinter.Entry(window, width=50)
entry.pack()

#Poga skaitļu šķiršanai
sort_button = tkinter.Button(window, text="Sort data", command=sort_numbers)
sort_button.pack()

window.mainloop()