import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 300)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.9, 0.9, 0.9)  # Light gray background
ctx.paint()

ctx.set_line_width(2)

# The part below the cross
ctx.move_to(180, 92)
ctx.line_to(212, 92)
ctx.line_to(200, 48)
ctx.line_to(190, 48)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill()

# Joining the two parts
ctx.move_to(190, 48)
ctx.line_to(200, 48)
ctx.line_to(195, 42)  #  for slight alteration
ctx.line_to(190, 48)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill()

# The cross
ctx.move_to(195, 48)
ctx.line_to(195, 12)
ctx.move_to(185, 22)
ctx.line_to(205, 22)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.stroke()

# The bar below the cross
ctx.rectangle(158, 93, 74, 8)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Shell
# Side rectangles
ctx.rectangle(48, 218, 82, 38)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()
ctx.rectangle(258, 218, 82, 38)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Small white rectangles
ctx.rectangle(62, 228, 18, 12)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(92, 228, 18, 12)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(282, 228, 18, 12)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.rectangle(312, 228, 18, 12)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Trapeziums
ctx.move_to(78, 192)
ctx.line_to(128, 192)
ctx.line_to(128, 220)
ctx.line_to(38, 220)
ctx.close_path()
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

ctx.move_to(258, 192)
ctx.line_to(308, 192)
ctx.line_to(358, 220)
ctx.line_to(258, 220)
ctx.close_path()
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Center
ctx.move_to(128, 172)
ctx.line_to(128, 268)
ctx.line_to(258, 268)
ctx.line_to(258, 172)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

ctx.rectangle(158, 218, 34, 47)
ctx.rectangle(196, 218, 34, 47)
ctx.fill()

ctx.move_to(158, 218)
ctx.curve_to(168, 208, 178, 208, 194, 208)
ctx.line_to(194, 218)
ctx.close_path()
ctx.fill()

ctx.move_to(196, 208)
ctx.curve_to(210, 208, 220, 208, 228, 218)
ctx.line_to(196, 218)
ctx.close_path()
ctx.fill()

# Structure of center block
ctx.move_to(128, 172)
ctx.line_to(128, 268)
ctx.line_to(258, 268)
ctx.line_to(258, 172)
ctx.line_to(238, 158)
ctx.line_to(148, 158)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Structure of center roof
ctx.move_to(118, 180)
ctx.line_to(148, 158)
ctx.line_to(238, 158)
ctx.line_to(268, 180)
ctx.line_to(268, 170)
ctx.line_to(238, 150)
ctx.line_to(148, 150)
ctx.line_to(118, 170)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Center block window
ctx.arc(193, 175, 10, math.radians(0), math.radians(360))
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Roof above the door
ctx.move_to(148, 220)
ctx.line_to(193, 200)
ctx.line_to(238, 220)
ctx.line_to(238, 210)
ctx.line_to(193, 190)
ctx.line_to(148, 210)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Doors
ctx.rectangle(158, 218, 30, 44)
ctx.rectangle(196, 218, 30, 44)
ctx.fill()

ctx.move_to(158, 218)
ctx.curve_to(168, 208, 178, 208, 194, 208)
ctx.line_to(194, 218)
ctx.close_path()
ctx.fill()

ctx.move_to(196, 208)
ctx.curve_to(210, 208, 220, 208, 228, 218)
ctx.line_to(196, 218)
ctx.close_path()
ctx.fill()

# Top part
ctx.rectangle(172, 102, 48, 48)
ctx.set_source_rgb(0.1, 0.1, 0.1)
ctx.set_line_width(1)
ctx.fill_preserve()
ctx.stroke()

ctx.move_to(180, 122)
ctx.line_to(180, 145)
ctx.line_to(210, 145)
ctx.line_to(210, 122)
ctx.arc(195, 122, 15, math.pi, 0)
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(1)
ctx.fill_preserve()
ctx.stroke()

# Finalize and save image
surface.write_to_png("church_house.png")
print("Image saved as church_house.png")
