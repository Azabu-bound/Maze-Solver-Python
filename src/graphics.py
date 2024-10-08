from tkinter import Tk, BOTH, Canvas

class Window:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
    self._root = Tk()
    self._root.title("Maze Solver")
    self._root.protocol("WM_DELETE_WINDOW", self.close)
    
    self._canvas = Canvas()
    self._canvas.pack()
    
    self._running = False

  def redraw(self):
    self._root.update_idletasks()
    self._root.update()

  def wait_for_close(self):
    self._running = True
    while self._running:
      self.redraw()

  def draw_line(self, line, fill_color="black"):
    line.draw(self._canvas, fill_color)

  def close(self):
    self._running = False
    

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

class Line():
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2

  def draw(self, canvas, fill_color="black"):
    canvas.create_line(
      self.point1.x,
      self.point1.y,
      self.point2.x,
      self.point2.y,
      fill = fill_color,
      width = 2
    )