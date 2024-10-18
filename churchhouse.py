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

# Left side building (Move closer, reduce x position from 100 to 120)
context.rectangle(120, 387, 80, 113)  # Adjusted position, closer to main house
context.fill_preserve()
context.stroke()

# Right side building (Move closer, reduce x position from 420 to 400)
context.rectangle(400, 387, 80, 113)  # Adjusted position, closer to main house
context.fill_preserve()
context.stroke()

# Left roof (polygon roof with right angles)
context.set_source_rgb(0, 0, 0)  # Black color for left roof
context.move_to(120, 387) # Left corner of the left roof
context .move_to(100,387)
context.line_to(120, 337)  # Left peak of the left roof
context.line_to(200, 337)  # Right peak of the left roof
context.line_to(200, 387)  # Right corner of the left roof
context.close_path()
context.fill_preserve()
context.stroke()

# Right roof (polygon roof with right angles)
context.set_source_rgb(0, 0, 0)  # Black color for right roof
context.move_to(400, 387)# Left corner of the right roof

context.line_to(400, 337)  # Left peak of the right roof
context.line_to(480, 337)  # Right peak of the right roof
context.line_to(500,387)
context.line_to(480, 387)# Right corner of the right roof


context.close_path()
context.fill_preserve()
context.stroke()

# Left windows
context.set_source_rgb(1, 1, 1)  # White windows
context.rectangle(130, 407, 20, 20)  # Left window 1
context.fill_preserve()
context.stroke()

context.rectangle(170, 407, 20, 20)  # Left window 2
context.fill_preserve()
context.stroke()

# Right windows
context.rectangle(410, 407, 20, 20)  # Right window 1
context.fill_preserve()
context.stroke()

context.rectangle(450, 407, 20, 20)  # Right window 2
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

# Small white circle above the door
context.set_source_rgb(1, 1, 1)  # White color for circle
context.arc(300, 390, 10, 0, 2 * math.pi)  # Small circle above door
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
context.set_line_width(3)  # Reduced line width to make the cross thinner
context.move_to(300, 90)  # Vertical part of cross
context.line_to(300, 120)
context.move_to(290, 105)  # Horizontal part of cross
context.line_to(310, 105)
context.stroke()

# Finalize and save image
surface.write_to_png("church_house_with_polygon_roofs_corrected.png")
print("Image saved as church_house_with_polygon_roofs_corrected.png")
