""" TODO: cosmetics
- change background color of each step
- change title bar to be transparent / same color as window
- OR remove title bar and replace with frame [open step-count close]
- OR remove open button and keep os title bar
- *OR keep open button and keep os title bar AND don't space out the buttons
"""

""" TODO: functionality
- open current file in default text editor
- skip to step
- text resizing / zoom
	- remember text size / zoom on close
- open file from url
- copy button for codeblocks and code
- remember file and step on close
- remember window position and size on close
- color preferences
- help window
- add hotkeys / key bindings
	- open file
	- next
	- previous
	- go to??? would need to put in a number as well - extra menu
	- help menu for hotkeys
	- close
"""

"""TODO: non-functionality
- Readme
- Help / tutorial default first open md file
- Example md instruction files
- Add license
"""

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


class StickySteps:

	root = Tk()
	root.title("Sticky Steps")
	width = 300
	height = 200
	y = 10
	ss = None

	def __init__(self):

		# make the sticky sized window appear in the top right corner
		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()
		
		x = screen_width - self.width - 10
		
		self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, x, self.y))

		# add gui elements
		self.counter = Label(self.root, text = "")
		self.counter.pack()

		self.html_label = HTMLLabel(self.root, html="")
		self.html_label.pack(fill="both", expand=True)
		self.html_label.fit_height()

		self.bottomButtons = Frame(self.root)
		self.bottomButtons.pack(side = BOTTOM)

		# make buttons to paginate through step list
		self.prev_button = Button(self.bottomButtons, text="<", command=self.prev_step)
		self.prev_button.grid(row = 0, column = 0)
		self.open_button = Button(self.bottomButtons, text="o", command=self.open_file)
		self.open_button.grid(row = 0, column = 1)
		self.next_button = Button(self.bottomButtons, text=">", command=self.next_step)
		self.next_button.grid(row = 0, column = 2)

		

	def open_file(self):
		sourcefile = filedialog.askopenfilename(filetypes=[("markdown files", "*.md")])
		self.ss = StepSource(sourcefile)
		self.html_label.set_html(self.ss.step_html)
		self.update_counter()

	def update_counter(self):
		self.counter.config(text = "%d / %d" % (self.ss.step_number, self.ss.step_count))

	def prev_step(self):
		if self.ss is None:
			return
		self.html_label.set_html(self.ss.prev())
		self.update_counter()

	def next_step(self):
		if self.ss is None:
			return
		self.html_label.set_html(self.ss.next())
		self.update_counter()

	def run(self):
		self.root.mainloop()


stickysteps = StickySteps()
stickysteps.run()