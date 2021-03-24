from tkinter import *
from tkinter import filedialog
from tkhtmlview import HTMLLabel
import markdown

class StepSource:
	def __init__(self, location):
		md_file = open(location)
		md_text = md_file.read()
		md_file.close()
		html = markdown.markdown(md_text)
		self.step_list = html.split("<hr />")
		self.step_count = len(self.step_list)
		self.step_number = 1
		self.step_html = self.step_list[0]

	def goto_step(self, step_number):
		# if requested step number is invalid, return the current step
		if step_number in range(1, self.step_count + 1):
			self.step_number = step_number
			self.step_html = self.step_list[step_number - 1]

		return self.step_html

	def next(self):
		return self.goto_step(self.step_number + 1)

	def prev(self):
		return self.goto_step(self.step_number - 1)



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

# TODO: create button and function for opening a file
# TODO: figure out how to separate / organize the buttons, root, and functions
# like seriously, how does this mainloop thing work???
ss = None
def open_file():
	sourcefile = filedialog.askopenfilename(filetypes=[("markdown files", "*.md")])
	# Open the test file
	global ss
	ss = StepSource(sourcefile)
	html_label = HTMLLabel(root, html=ss.step_html)

def next_step():
	global ss
	html_label.set_html(ss.next())

html_label = HTMLLabel(root, html="")
html_label.pack(fill="both", expand=True)
html_label.fit_height()

# make buttons to paginate through step list
next_button = Button(root, text="Next", command=next_step)
next_button.pack()

open_button = Button(root, text="Open", command=open_file)
open_button.pack()

root.mainloop()