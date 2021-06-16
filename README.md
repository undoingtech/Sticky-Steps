# STICKY STEPS

Sticky Steps is a small productivity app. The goal is to focus on one small step at a time. Sticky Steps takes a markdown file as input and uses `horizontal rules` to divide the file into steps.

**Contents**

- [Dependencies](#dependencies)
- [How to run](#how-to-run)
- [About this project (for CS50)](#about-this-project)
	- [Demo video and screenshots](#demo-video-and-screenshots)
	- [Project file descriptions](#project-file-descriptions)
	- [Design decisions](#design-decisions)

## Dependencies
Sticky Steps is built on python3 and the following python modules:

- markdown
- [tkhtmlview](https://github.com/bauripalash/tkhtmlview/) (itself dependent on Pillow)
- editor

## How to run

1. Make sure you have [python3](https://www.python.org/downloads/) installed.
2. Install the dependencies above
	
`pip install [dependency]`

3. Download the source code for Sticky Steps
	
`wget -O StickySteps.zip https://github.com/undoingtech/Sticky-Steps/archive/refs/heads/main.zip`

4. Unzip the source code
	
`unzip StickySteps.zip`

5. Open the source code folder
	
`cd StickySteps-main` 

6. Run `python3 steps.py`

---

# About this project

Sticky Steps was made as the final project for Harvard's CS50x class. As per the requirements of the class, I have:

- included a link to a [demo video](#demo-video-and-screenshots) 
- described the functionality of [each file](#project-file-descriptions) in this project
- documented the [design decisions](#design-decisions) and the thought process behind them

## Demo video and screenshots

[![Demo video](https://i3.ytimg.com/vi/AEcpiR9QA44/maxresdefault.jpg)](https://youtu.be/AEcpiR9QA44)

![intro welcome step](https://github.com/undoingtech/Sticky-Steps/blob/main/screenshots/intro-welcome.png "Intro - Welcome")

![intro keybindings step](https://github.com/undoingtech/Sticky-Steps/blob/main/screenshots/intro-keybindings.png "Intro - Keybindings")

![keybindings help menu](https://github.com/undoingtech/Sticky-Steps/blob/main/screenshots/keybindings-help-menu.png "Keybindings help menu")

![go to step menu](https://github.com/undoingtech/Sticky-Steps/blob/main/screenshots/go-to-step-menu.png "Go-to-step menu")

## Project file descriptions

This section contains a description of the file contents for:

- [steps.py](#steps.py)
- [test.md](#test.md)
- [sticky-steps-features.png](#sticky-steps-features.png)

### steps.py

This file creates the Sticky Steps application. It is the only file with code.

This file contains two classes: `Steps` and `StickySteps`.

The `Steps` class handles text data from a markdown file. It is responsible for 

- keeping the markdown file location
- dividing the markdown file into steps
- converting the markdown to html
- counting the steps
- assigning colors and numbers to the steps

The `StickySteps` class creates the GUI and impliments most of the application's functionality. This class contains functions for 

- opening a markdown file 
- editing the current file 
- changing steps
- displaying a help message
- updating the gui
- starting the gui

### test.md

This file contains an introduction to Sticky Steps for new users. It deliberately uses many markdown elements. This helps new users and developers understand how markdown files will look in Sticky Steps.

### sticky-steps-features.png

This file contains the initial Sticky Steps design. It includes a list of MVP features, a list of extra features, and GUI drawing.

## Design decisions

In this section, I discuss the major design decisions and my thought process behind them. I also dicuss which decisions I regret and why.

- [Idea origin](#idea-origin)
- [Language and library choices](#language-and-library-choices)
- [Markdown vs gemtext](#markdown-vs-gemtext)
- [GUI layout design](#gui-layout-design)
- [Unfinished features](#unfinished-features)

### Idea origin

I was laying on the couch, wondering what my project would be. 
I was "shuffling" some sticky notes, just fidgeting with them. 
I thought about how tasks go on sticky notes. 
I thought it would be nice if one task was on one note, so that I can focus on it 
(while on the computer at least). 
But I had a whole stack of sticky notes chained together, so I thought
about chaining tasks together. 
The chain would be suitable for short ordered tasks and instructions. 

The idea for Sticky Steps is to have a "stack" of notes that have one task each. 

Every other project idea was either too big for me to do or too small to matter.

I now regret making Sticky Steps because I know I won't use it. I wanted to make something really useful for myself. Sticky Steps was supposed to help me focus on one task at a time while I am on the computer. However, Sticky Steps just doesn't work for me.

### Language and GUI toolkit choices

I considered the language and GUI toolkit at the same time. I wanted to use C or python since I already had some experience using those languages. Fortunately for me, there were several cross platform GUI toolkits for C and python.

I wanted this project to be cross platform, so I looked up
cross platform GUI libraries. I read a few articles to help inform my decision: 

- [gui library for beginner C++ programmer](https://stackoverflow.com/questions/5248105/gui-library-for-beginner-c-programmer)
- [What's the most enjoyable cross-platform GUI toolkit?](https://www.quora.com/Whats-the-most-enjoyable-cross-platform-GUI-toolkit?share=1)
- [PyQt vs Tkinter – The better GUI library](https://coderslegacy.com/pyqt-vs-tkinter/)

I picked python because it is easier and quicker for me to use compared to C. Also, I anticipated that Sticky Steps would mostly handle small amounts of text data. Therefore, I would not need to prioritize handling data efficiently in regards to RAM usage. If my idea had required working with large amounts of data, I would have used C instead to help optimize RAM usage and execution time.

I picked the tkinter GUI toolkit because I wanted to create a minimal application. 
I did not need a whole bunch of widgets or other functionality. 
Also, tkinter comes with python, so I did not need to add an extra dependency to use it. 
The *PyQt vs Tkinter* article also showed that elements in tkinter are more "fuzzy" than those in PyQt. 
This was good for my project since I wanted more focus on the text and less focus on the buttons.

### Markdown vs gemtext

When I started designing this project, I had to decide the format of the text input. The two candidates I considered were Markdown and gemtext.

Markdown is very popular and has tons of libraries. There were already python libraries for parsing and rendering Markdown in a tkinter app.

Gemtext is a very new and not well known text format. By design, it is much simpler than Markdown. As explained in [A quick introduction to "gemtext" markup](https://gemini.circumlunar.space/docs/gemtext.gmi), gemtext only has a few elements:

- text
- links
- headings
- lists
- blockquotes
- preformatted text

I decided to use Markdown because the python libraries for handling Markdown files already existed. If I had used gemtext, I would have had to create a parser and renderer myself.

I now wish I had used gemtext and regret using Markdown. The Markdown library, [tkhtmlview](https://github.com/bauripalash/tkhtmlview/), creates very large text. It also renders some Markdown elements in weird ways. For example, inline `code` is rendered on its own line. For another example, blockquotes and regular text appear the same.

If I had created my own gemtext parser and renderer, I could have made sure all elements were rendered exactly how I wanted.

### GUI layout design

You can look at the initial design in [sticky-steps-features.png](https://github.com/undoingtech/Sticky-Steps/blob/main/sticky-steps-features.png).

I wanted the app window to look like a sticky note. I wanted the text to be prominent and the buttons to be small and out of the way.

I considered removing the title bar to make the window look more like a sticky note. 
However, removing the title bar would have also removed functionality from the OS. 
I decided it would be better to keep the OS functionality and adjust my cosmetic plan instead. 

I only kept buttons for MVP functionality. 
I used many keybindings to cover extra functionality, thereby limiting the number of buttons needed. 

### Unfinished features

If you look at the top of [steps.py](https://github.com/undoingtech/Sticky-Steps/blob/main/steps.py), you will see many features that I have not implimented. 
I worked on Sticky Steps until it had MVP functionality, plus a few features. 
I do not think adding any of the other planned features will make me like Sticky Steps more. 
It was a nice little experiment, but I have lost interest. 
I do not plan to use or maintain Sticky Steps.

---

[Back to top of README](#sticky-steps)

[Back to top of About section](#about-this-project)