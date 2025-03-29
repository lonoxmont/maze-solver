from graphics import Line, Point



class Cell:
    def __init__(self, win=None):
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = None
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall == True:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "#d9d9d9")
        if self.has_top_wall == True:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "#d9d9d9")

        if self.has_right_wall == True:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "#d9d9d9")
        if self.has_bottom_wall == True:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "#d9d9d9")
            
    def draw_move(self, to_cell, undo=False):
    # Set the color based on undo flag
        if undo:
            colour = "grey"
        else:
            colour = "red"
    
    # Calculate the center of the current cell
        current_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
    
    # Calculate the center of the to_cell
        to_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
    
    # Create a Line object
        line = Line(current_center, to_center)
    
    # Draw the line
        self._win.draw_line(line, colour)
    '''def draw_move(self, to_cell, undo=False):
        self.to_cell = to_cell
        self.undo = undo
        self.fill_colour = "black"
        if self.undo == True:
            pass
            #self.line.draw(fill_colour="grey")
        else:
            pass
            #self.line.draw(fill_colour="red")
        # Calculate the center of the current cell
        x_center = (self._x1 + self._x2) / 2
        y_center = (self._y1 + self._y2) / 2
    
        # Calculate the center of the to_cell
        to_x_center = (to_cell._x1 + to_cell._x2) / 2
        to_y_center = (to_cell._y1 + to_cell._y2) / 2
    
        # Draw the line between the centers
        # You'll need to check what method your Window class uses to draw a line
        self._win.draw_line(x_center, y_center, to_x_center, to_y_center, self.fill_colour)'''