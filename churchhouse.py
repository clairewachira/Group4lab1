import cairo
import math

# Set up the canvas dimensions
WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

# Main Building
context.set_source_rgb(0, 0, 0)  # Black color
context.rectangle(200, 300, 200, 200)  # Main house
context.fill_preserve()
context.stroke()

# Triangle roof of the main building
context.move_to(180, 300)  # Left corner of the roof
context.line_to(300, 200)  # Peak of the roof
context.line_to(420, 300)  # Right corner of the roof
context.close_path()
context.fill_preserve()
context.stroke()

# Left side building
context.rectangle(100, 350, 140, 150)
context.fill_preserve()
context.stroke()

# Right side building
context.rectangle(400, 350, 110, 150)
context.fill_preserve()
context.stroke()

# Left windows
context.set_source_rgb(1, 1, 1)  # White windows
context.rectangle(110, 370, 20, 20)  # Left window 1
context.fill_preserve()
context.stroke()

context.rectangle(150, 370, 20, 20)  # Left window 2
context.fill_preserve()
context.stroke()

# Right windows
context.rectangle(430, 370, 20, 20)  # Right window 1
context.fill_preserve()
context.stroke()

context.rectangle(470, 370, 20, 20)  # Right window 2
context.fill_preserve()
context.stroke()

# Door
context.rectangle(270, 400, 60, 100)  # Door frame
context.fill_preserve()
context.stroke()

# Arch for door
context.arc(300, 400, 30, math.pi, 2 * math.pi)  # Semi-circle for door arch
context.fill_preserve()
context.stroke()

# Tower
context.set_source_rgb(0, 0, 0)  # Black color for tower
context.rectangle(270, 180, 60, 100)  # Main tower
context.fill_preserve()
context.stroke()

context.rectangle(280, 120, 40, 60)  # Upper tower part
context.fill_preserve()
context.stroke()

# Cross on top of the tower
context.set_source_rgb(0, 0, 0)  # Black cross
context.set_line_width(5)
context.move_to(300, 90)  # Vertical part of cross
context.line_to(300, 120)
context.move_to(290, 105)  # Horizontal part of cross
context.line_to(310, 105)
context.stroke()

# Finalize and save image
surface.write_to_png("church_house.png")
print("Image saved as church_house.png")
