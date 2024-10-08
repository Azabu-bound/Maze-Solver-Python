from graphics import Line, Point

class Cell():
  def __init__(self, window):
    self.has_wall_left = True
    self.has_wall_right = True
    self.has_wall_top = True
    self.has_wall_bottom = True

    self._x1 = None
    self._y1 = None
    self._x2 = None
    self._y2 = None

    self._window = window

  def draw(self, x1, y1, x2, y2):
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2

    if self.has_wall_left:
      line = Line(Point(x1, y1), Point(x2, y2))
      self._window.draw_line(line)
    
    if self.has_wall_right:
      line = Line(Point(x1, y1), Point(x2, y2))
      self._window.draw_line(line)

    if self.has_wall_top:
      line = Line(Point(x1, y1), Point(x2, y2))
      self._window.draw_line(line)

    if self.has_wall_bottom:
      line = Line(Point(x1, y1), Point(x2, y2))
      self._window.draw_line(line)