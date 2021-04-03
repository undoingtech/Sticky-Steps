""" TODO: cosmetics
- get rid of the lines from html_label
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

"""TODO: bug fixes
- error when user cancels file open
- html_label lags behind on color update (charming bug I'm not sure I want to fix)
	- possible fix by changing StepSource::goto_step to return self.step
	- then change StickySteps::prev and StickySteps::next accordingly
	- then call StickySteps::update_widgets first
	- then update html label
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
		self.steps_list = html.split("<hr />")
		self.steps_count = len(self.steps_list)

		# - blue	#a9edf1 SOURCE: https://www.color-hex.com/color-palette/104537
		# - yellow	#f1f58f SOURCE: https://www.color-hex.com/color-palette/104537
		# - purple	#927ff4
		# - pink	#e095f9
		self.colors = ["#f1f58f", "#a9edf1", "#927ff4", "#e095f9"]
		self.step = dict()
		self.step["number"] = 1
		self.step["html"] = self.steps_list[0]
		self.step["color"] = self.colors[0]

	def goto_step(self, step_number):
		# if requested step number is invalid, return the current step
		if step_number in range(1, self.steps_count + 1):
			self.step["number"] = step_number
			self.step["html"] = self.steps_list[step_number - 1]
			color_index = step_number - 1 
			if step_number >= len(self.colors):
				color_index = (step_number - 1) % len(self.colors)
			self.step["color"] = self.colors[color_index]

		return self.step["html"]

	def next(self):
		return self.goto_step(self.step["number"] + 1)

	def prev(self):
		return self.goto_step(self.step["number"] - 1)


class StickySteps:

	root = Tk()
	root.title("Sticky Steps")
	widgets = dict()
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

	def open_file(self):
		sourcefile = filedialog.askopenfilename(filetypes=[("markdown files", "*.md")])
		self.ss = StepSource(sourcefile)
		self.widgets["html_label"].set_html(self.ss.step["html"])
		self.update_counter()

	def update_counter(self):
		self.widgets["counter"].config(text = "%d / %d" % (self.ss.step["number"], self.ss.steps_count))

	def update_color(self):
		self.root["background"] = self.ss.step["color"]
		for widget in self.widgets:
			#print("widget: %s - widget type: %s" % (widget, type(widget)))
			self.widgets[widget].configure(bg=self.ss.step["color"])	

	def update_widgets(self):
		self.update_counter()
		self.update_color()

	def prev_step(self):
		if self.ss is None:
			return
		self.widgets["html_label"].set_html(self.ss.prev())
		self.update_widgets()

	def next_step(self):
		if self.ss is None:
			return
		self.widgets["html_label"].set_html(self.ss.next())
		self.update_widgets()

	def run(self):
		self.root.mainloop()


stickysteps = StickySteps()
stickysteps.run()