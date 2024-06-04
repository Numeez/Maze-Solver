from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,height,width) -> None:
       self.height = height
       self.width = width
       self.root = Tk()
       self.root.title("Maze Solver")
       self.root.geometry(f"{self.height}x{self.width}")
       self.canvas = Canvas()
       self.canvas.pack()
       self.is_running = False
       self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_running=True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running=False

    def draw_line(self,line,fill_color:str):
        line.draw(self.canvas,fill_color)


class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self,point1,point2) -> None:
        self.point1 = point1
        self.point2 = point2
    
    def draw(self,canvas,fill_color):
        canvas.create_line(self.point1.x,self.point1.y,self.point2.x,self.point2.y,fill = fill_color,width=2)



        

        
        
    

        

    

def main():
   
    win = Window(1000, 1000)

    win.wait_for_close()


if __name__ == '__main__':
    main()
    