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

		"""# TODO: add elements
		- step counter on top (1/10)
		- get rid of open button? why have open button when you can use keyboard?
		- or put open button inbetween prev and next
		"""

		""" TODO: add hotkeys
		- open file
		- next
		- previous
		- go to??? would need to put in a number as well - extra menu
		- help menu for hotkeys
		- close
		"""

		# add gui elements
		self.html_label = HTMLLabel(self.root, html="")
		self.html_label.pack(fill="both", expand=True)
		self.html_label.fit_height()

		# make buttons to paginate through step list
		self.prev_button = Button(self.root, text="prev", command=self.prev_step)
		self.prev_button.pack()
		self.next_button = Button(self.root, text="Next", command=self.next_step)
		self.next_button.pack()

		self.open_button = Button(self.root, text="Open", command=self.open_file)
		self.open_button.pack()

	def open_file(self):
		sourcefile = filedialog.askopenfilename(filetypes=[("markdown files", "*.md")])
		self.ss = StepSource(sourcefile)
		self.html_label.set_html(self.ss.step_html)

	def prev_step(self):
		if self.ss is None:
			return
		self.html_label.set_html(self.ss.prev())

	def next_step(self):
		if self.ss is None:
			return
		self.html_label.set_html(self.ss.next())

	def run(self):
		self.root.mainloop()


stickysteps = StickySteps()
stickysteps.run()