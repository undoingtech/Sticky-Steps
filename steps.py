""" TODO: cosmetics
- get rid of the lines from html_label
"""

""" TODO: functionality
- text resizing / zoom
	- remember text size / zoom on close
- open file from url
- copy button for codeblocks and code
- remember file and step on close
- remember window position and size on close
- color preferences
- add step before current step
- add step after current step
- add note to step
"""

"""TODO: bug fixes
"""

"""TODO: non-functionality
- Readme
	- video link
	- description of each file
- Help / tutorial default first open md file
- Example md instruction files
"""

from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from tkhtmlview import HTMLLabel
import markdown
import editor

class Steps:
	def __init__(self, file_location):
		md_file = open(file_location)
		md_text = md_file.read()
		md_file.close()
		html = markdown.markdown(md_text)
		
		# variables that don't change after init
		self.step_list = html.split("<hr />")
		self.step_count = len(self.step_list)
		self.file_location = file_location

		# - blue	#a9edf1 SOURCE: https://www.color-hex.com/color-palette/104537
		# - yellow	#f1f58f SOURCE: https://www.color-hex.com/color-palette/104537
		# - purple	#927ff4
		# - pink	#e095f9
		self.colors = ["#f1f58f", "#a9edf1", "#927ff4", "#e095f9"]
		
		# variables that do change after init
		self.number = 1
		self.html = self.step_list[0]
		self.color = self.colors[0]
		

	def goto_step_number(self, step_number):
		# if requested step number is invalid, return the current step
		if step_number in range(1, self.step_count + 1):
			self.number = step_number
			self.html = self.step_list[step_number - 1]
			self.color = self.get_step_color(step_number)
		return self.html

	def get_step_color(self, step_number):
		color_index = step_number - 1 
		if step_number >= len(self.colors):
			color_index = (step_number - 1) % len(self.colors)
		return self.colors[color_index]


class StickySteps:

	root = Tk()
	root.title("Sticky Steps")
	widgets = dict()
	width = 300
	height = 200
	y = 10
	step = None

	def __init__(self):

		# make the sticky sized window appear in the top right corner
		x = self.root.winfo_screenwidth() - self.width - 10
		self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, x, self.y))

		# add gui elements
		self.widgets["counter"] = Label(self.root, text = "")
		self.widgets["counter"].pack()

		self.widgets["html_label"] = HTMLLabel(self.root, html="")
		self.widgets["html_label"].pack(fill="both", expand=True)
		self.widgets["html_label"].fit_height()

		self.widgets["bottomButtons"] = Frame(self.root)
		self.widgets["bottomButtons"].pack(side = BOTTOM)

		# make buttons to paginate through step list
		self.widgets["prev_button"] = Button(self.widgets["bottomButtons"], text="<", command=self.prev_step)
		self.widgets["prev_button"].grid(row = 0, column = 0)
		self.widgets["open_button"] = Button(self.widgets["bottomButtons"], text="o", command=self.open_file)
		self.widgets["open_button"].grid(row = 0, column = 1)
		self.widgets["next_button"] = Button(self.widgets["bottomButtons"], text=">", command=self.next_step)
		self.widgets["next_button"].grid(row = 0, column = 2)

		self.root["background"] = "#f1f58f"
		for widget in self.widgets:
			#print("widget: %s - widget type: %s" % (widget, type(widget)))
			self.widgets[widget].configure(bg="#f1f58f", bd=0, relief=FLAT)	
		# because html_label only picks up color after the configure for some reason
		self.widgets["html_label"].set_html("")

		self.root.bind("<h>", lambda e:self.help_message())
		self.root.bind("<o>", lambda e:self.open_file())
		self.root.bind("<e>", lambda e:self.edit_file())
		self.root.bind("<Right>", lambda e:self.next_step())
		self.root.bind("<Left>", lambda e:self.prev_step())
		self.root.bind("<g>", lambda e:self.goto_step_number())
		self.root.bind("<Control-q>", lambda e:self.root.destroy())

		self.keybindings = dict()
		self.keybindings["h"] = "Show keybindings"
		self.keybindings["o"] = "Open local file"
		self.keybindings["e"] = "Edit file"
		self.keybindings["Right"] = "Go to next step"
		self.keybindings["Left"] = "Go to previous step"
		self.keybindings["g"] = "Go to step [number]"
		self.keybindings["Control-q"] = "Quit"

	def help_message(self):
		# Oneliner SOURCE: https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python
		message = "\n".join("{}\t{}".format(k, v) for k, v in self.keybindings.items())
		messagebox.showinfo("Key bindings", message)

	def open_file(self, file_location=None):
		if file_location is None:
			file_location = filedialog.askopenfilename(filetypes=[("markdown files", "*.md")])
		if type(file_location) is not str or file_location == "":
			return
		self.step = Steps(file_location)
		self.widgets["html_label"].set_html(self.step.html)
		self.update_counter()

	def update_counter(self):
		self.widgets["counter"].config(text = "%d / %d" % (self.step.number, self.step.step_count))

	def update_color(self):
		self.root["background"] = self.step.color
		for widget in self.widgets:
			#print("widget: %s - widget type: %s" % (widget, type(widget)))
			self.widgets[widget].configure(bg=self.step.color)	

	def update_widgets(self):
		self.update_counter()
		self.update_color()

	def goto_step_number(self):
		if self.step is None:
			return
		step_number = simpledialog.askinteger("Input", "Go to step", parent=self.root)
		html = self.step.goto_step_number(step_number)
		
		# must set html after update widgets so html has same color
		self.update_widgets()
		self.widgets["html_label"].set_html(html)

	def goto_step_increment(self, increment):
		if self.step is None:
			return
		html = self.step.goto_step_number(self.step.number + increment)
		
		# must set html after update widgets so html has same color
		self.update_widgets()
		self.widgets["html_label"].set_html(html)

	def prev_step(self):
		self.goto_step_increment(-1)

	def next_step(self):
		self.goto_step_increment(1)

	def edit_file(self):
		if self.step is None:
			return
		target_file = self.step.file_location
		editor(filename=target_file)
		self.open_file(target_file)

	def run(self):
		self.root.mainloop()


stickysteps = StickySteps()
stickysteps.run()