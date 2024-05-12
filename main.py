import tkinter as tk
from fcfs import FCFS
from c_look import C_look
from Second_Chance_Algorithm import Second_Chance
from ipynb.fs.full.LRU import LRU # type: ignore
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced OS Project")
        self.geometry("800x600")
        self.resizable(False, False)
        self.create_widgets()
    def draw_graph(self, path,num, page_faults = 0, totalMovement = 0, history = []):
        self.clear_wndow()
        canvas = tk.Canvas(self, width=800, height=600)
        canvas.pack()
        if num == 1 or num == 2:
            sorted_path = sorted(path)
            for i, val in enumerate(sorted_path):
                x = (i * 40) + 10  
                canvas.create_line(x, 20, x, 400)
                label = str(val)
                canvas.create_text(x, 10, text=label) 

            for i in range(len(path)):
                x1 = (sorted_path.index(path[i]) * 40) + 10
                y1 = (i*20) + 20
                if i < len(path) - 1:
                    x2 = (sorted_path.index(path[i + 1]) * 40) + 10
                    y2 = (i*20) + 20 + 20
                    if (num == 2 and x1 < x2) or num != 2:
                        self.after(i * 2000 // len(path), canvas.create_line, x1, y1, x2, y2)
                radius = 5
                self.after(i * 2000 // len(path), self.create_oval_with_fill(canvas, x1, y1, radius))
            canvas.create_text(400, 500, text="Total Head Movement: " + str(totalMovement), font=("Arial", 16,"bold"))
        else:
            self.update()
            rect_width = self.winfo_width() // len(path)
        for i, val in enumerate(path):
            x1 = i * rect_width
            y1 = 0
            x2 = (i + 1) * rect_width
            y2 = 50  
            canvas.create_rectangle(x1, y1, x2, y2, fill='beige')
            canvas.create_text(x1 + rect_width // 2, y1 + 25, text=str(val), font=("Arial", 16))

    
        max_len = max(len(lst) for lst in history)
        rect_height = 400 // max_len  
        for i, lst in enumerate(history):
            x1 = i * rect_width
            x2 = (i + 1) * rect_width
            for j, val in enumerate(lst):
                if j == 0:
                    y1 = 100 + j * rect_height
                else:
                    y1 = 50 + j * rect_height  
                y2 = 50 + (j + 1) * rect_height
                canvas.create_rectangle(x1, y1, x2, y2)
                canvas.create_text(x1 + rect_width // 2, y1 + rect_height // 2, text=str(val),font=("Arial", 16) )  
        canvas.create_text(400, 500, text="Total Page Faults: " + str(page_faults), font=("Arial", 16,"bold"))
        self.BackButton = tk.Button(self, text="Back", command=lambda:self.create_widgets_buttons(1))
        self.BackButton.place(x=10, y=500)

    def create_oval_with_fill(self, canvas, x, y, radius):
        return lambda: canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='red')
    
    
    def PerformAlgorithm(self, num):
        if num == 1:
            self.path , self.totalMovement = FCFS(self.req_queue_list, self.head_start_value)
            self.draw_graph(self.path,num,totalMovement=self.totalMovement)
        elif num == 2:
            self.path , self.totalMovement = C_look(self.req_queue_list, self.head_start_value)
            self.draw_graph(self.path,num,totalMovement=self.totalMovement)
        elif num == 3:
            self.history, self.page_faults = LRU(self.req_queue_list, self.head_start_value)
            self.draw_graph(self.req_queue_list,num,page_faults=self.page_faults,history=self.history)
        elif num == 4:
            self.history, self.page_faults = Second_Chance(self.req_queue_list, self.head_start_value)
            self.draw_graph(self.req_queue_list,num,page_faults=self.page_faults,history=self.history)
    def create_widgets_buttons(self,pos):
        if pos == 0:
            self.head_start_value = self.head_start.get()
            self.req_queue_value = self.req_queue.get()
            self.req_queue_list = self.req_queue_value.split(",")
            if self.head_start_value.isdigit() == False:
                self.clear_wndow()
                self.create_widgets()
                return
            elif all(i.isdigit() for i in self.req_queue_list) == False:
                self.clear_wndow()
                self.create_widgets()
                return
            else:
                self.req_queue_list = list(map(int, self.req_queue_list))
                self.head_start_value = int(self.head_start_value)
        self.clear_wndow()
        self.FCFSButton = tk.Button(self, text="FCFS", command=lambda: self.PerformAlgorithm(1), bg='black', fg='white', width = 110)
        self.FCFSButton.place(x=10, y=10)
        self.C_LookButton = tk.Button(self, text="C-Look", command=lambda: self.PerformAlgorithm(2), bg='black', fg='white' , width = 110)
        self.C_LookButton.place(x=10, y=50)
        self.LRUButton = tk.Button(self, text="LRU", command=lambda: self.PerformAlgorithm(3), bg='black', fg='white' , width = 110)
        self.LRUButton.place(x=10, y=90)
        self.SecondChanceButton = tk.Button(self, text="Second Chance", command=lambda: self.PerformAlgorithm(4), bg='black', fg='white' , width = 110)
        self.SecondChanceButton.place(x=10, y=130)
        self.BackButton = tk.Button(self, text="Back", command=self.create_widgets, bg='black', fg='white', width = 50)
        self.BackButton.place(x=225, y=170)
        print(self.req_queue_list)
        print(self.head_start_value)
    def create_widgets(self):
        self.clear_wndow() 
        self.label = tk.Label(self, text="Enter the initial head start position or number of frames: ")
        self.label.pack()
        self.head_start = tk.Entry(self)
        self.head_start.pack()
        self.label = tk.Label(self, text="Enter the disk queue: ")
        self.label.pack()
        self.req_queue = tk.Entry(self)
        self.req_queue.pack()
        self.start_btn = tk.Button(self, text="Start", command=lambda:self.create_widgets_buttons(0), bg='black', fg='white', width = 50)
        self.start_btn.pack()
    def clear_wndow(self):
        for widget in self.winfo_children():
            widget.destroy()

def main():
    app = App()
    app.mainloop()
    
if __name__ == "__main__":
    main()