from graphics import Window, Point, Line

def main():
    win = Window(640, 480)
    
    # Create some points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    
    # Create lines between these points
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    
    # Draw the lines with different colors
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    
    win.wait_for_close()


if __name__ == "__main__":
    main()