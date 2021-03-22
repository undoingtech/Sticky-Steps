from tkinter import *
from tkhtmlview import HTMLLabel
import markdown

root = Tk()
root.title("Sticky Steps")

# this is the important one - make it sticky sized
# make the window appear in the top right corner
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 300
height = 200
x = screen_width - width - 10
y = 10
root.geometry("%dx%d+%d+%d" % (width, height, x, y))


# need to open the test document - test.md
# load the md in the tkinter window
# now need to either convert to html and display
md = open("./test.md")
test_text = md.read()
md.close()
html = markdown.markdown(test_text)
# make a list of steps by splitting on horizontal rules
step_list = html.split("<hr />")
html_label = HTMLLabel(root, html=step_list[1])
html_label.pack(fill="both", expand=True)
html_label.fit_height()

# TODO: make buttons to paginate through step list

root.mainloop()
