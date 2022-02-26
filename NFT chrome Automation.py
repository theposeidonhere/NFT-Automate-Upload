import subprocess
from tkinter import *
from tkinter.messagebox import WARNING, showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
from tkinter import filedialog
import tkinter.scrolledtext as tkst
from tkinter import colorchooser
import tkinter.font as font
from tkinter import filedialog
###
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
###
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
import platform 
from colorama import init
from colorama import Fore,Back,Style 
init()
import tempfile

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)



opsys = platform.system()
main_directory = os.getcwd()
file = None

print("main_directory: "+main_directory+"\
	\nscript_location: "+os.path.join(sys.path[0])+"\
	\nif the above do not match the browser will not open \
	")
message= "watch my Youtube Video and Contact me if you need any clarifications.\n\n"
message2= "💀Modded By DrSkull💀\n"


for char in message:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.00001)
for char in message2:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.1)



class LineNumbers(Text):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
 
        self.text_widget = text_widget
        self.text_widget.bind('<KeyRelease>', self.on_key_release)
        self.text_widget.bind('<FocusIn>', self.on_key_release)
        self.text_widget.bind('<MouseWheel>', self.on_key_release)

        self.insert(1.0, '1')
        self.configure(state='disabled')
 
    def on_key_release(self, event=None):
        p, q = self.text_widget.index("@0,0").split('.')
        p = int(p)
        final_index = str(self.text_widget.index(END))
        num_of_lines = final_index.split('.')[0]
        line_numbers_string = "\n".join(str(p + no) for no in range(int(num_of_lines)))
        width = len(str(num_of_lines))
 
        self.configure(state='normal', width=width)
		
        self.delete(1.0, END)
        self.insert(1.0, line_numbers_string)
        self.configure(state='disabled')
				


root = Tk()
root.configure(background='#474244')
root.title("💀NFT Chrome Automation💀")

root.geometry("644x788")
root.iconbitmap(default=ICON_PATH)

def upload_folder_input():
	global upload_path
	upload_path = filedialog.askdirectory()
	Name_change_folder_button(upload_path)

def Name_change_folder_button(upload_folder_input):
	folder["text"] = upload_folder_input

def open_chrome_profile():
	if main_directory == os.path.join(sys.path[0]):
		browser_port=int(p.get())
		if opsys == "Windows":
			subprocess.Popen(['start', 'chrome', 
			'--remote-debugging-port={port_num}'.format(port_num=browser_port), 
			'--user-data-dir=' + main_directory + '/chrome_profile'], shell=True)
		elif opsys == "Darwin":
			cmd = "open -a /Applications/Google\ Chrome.app --args \
			--remote-debugging-port={port_num} \
				--user-data-dir={cwd}/chrome_profile".format(cwd = main_directory, port_num=browser_port)
			subprocess.Popen(cmd, shell=True)
		else:
			subprocess.Popen(['google-chrome', 
			'--remote-debugging-port={port_num}'.format(port_num=browser_port), 
			'--user-data-dir=' + main_directory + '/chrome_profile'], shell=True)

		print("Opening debug browser on port {port_num}".format(port_num=browser_port))
	else:
		print("Main_directory and Program directory do not match, \
			Please Only Run the Auto_Chrome_* script directly from the folder it is in\
				\n easy fix to this might be to put everything the program folder in a sub-folder")
	
#####MENU BAR#####
def newFile():
	global file
	root.title("Untitled - Auto_Chrome")
	file = None
	TextArea.delete(1.0, END)

def openFile():
	global file
	file = askopenfilename()
	if file == "":
		file = None
	else:
		root.title(os.path.basename(file) + " - Auto_Chrome")
		TextArea.delete(1.0, END)
		f = open(file, "r")
		TextArea.insert(1.0, f.read())
		f.close()

def saveFile():
	global file
	if file == None:
		file = asksaveasfilename(initialfile = 'Untitled.py')
		if file =="":
			file = None

		else:
			#Save as a new file
			f = open(file, "w")
			f.write(TextArea.get(1.0, END))
			f.close()

			root.title(os.path.basename(file) + " - Auto_Chrome")
			print("File Saved")
	else:
		# Save the file
		f = open(file, "w")
		f.write(TextArea.get(1.0, END))
		f.close()

def quitApp():
	root.destroy()
def donate():
	showinfo("Donate", "https://paypal.me/spreadcare1996")

def about():
	showinfo("NFT Chrome Automation", "modded by @DrSkull")

MenuBar = Menu(root)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="New", command=newFile)
FileMenu.add_command(label="Open", command = openFile)
FileMenu.add_command(label = "Save", command = saveFile)
FileMenu.add_separator()
FileMenu.add_command(label = "Exit", command = quitApp)
MenuBar.add_cascade(label = "File", menu=FileMenu)
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label = "Donate", command=donate)

HelpMenu.add_command(label = "About Notepad", command=about)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
root.config(menu=MenuBar)
root.config (bg = '#34b7eb')
#####MENU BAR END#####


# _____MAIN_CODE_____
def main_program_loop(): 
	browser_port=int(p.get())
	###new chrome options
	if opsys == "Windows":
		ser = Service(main_directory + "/chromedrivers/chromedriver.exe")
	elif opsys == "Darwin":
		ser = Service(main_directory + "/chromedrivers/chromedriver")
	else:
		ser = Service(main_directory + "/chromedrivers/linuxchromedriver")

	op = webdriver.ChromeOptions()
	op.add_experimental_option("debuggerAddress", "localhost:{port_num}".format(port_num=browser_port))
	driver = webdriver.Chrome(service=ser, options=op)
	wait = WebDriverWait(driver, int(w.get()))

	print("Connected to browser on port {port_num}".format(port_num=browser_port))

	#establish main page
	main_page = driver.current_window_handle

	def xpath_and_click(code, fail_message = "Xpath not found"):
		while True:
			try:
				x = wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))
				x.click()
				break
			except:
				print(fail_message + ": " + code + "\nretrying...")
				time.sleep(1)
		

	def css_and_click(code, fail_message = "Css not found"):
		while True:
			try:
				x = wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code)))
				x.click()
				break
			except:
				print(fail_message + ": " + code + "\nretrying...")
				time.sleep(1)


	def xpath_and_key(code, key, fail_message = "Xpath not found"):
		while True:
			try:
				x = wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))
				x.send_keys(key)
				break
			except:
				print(fail_message + ": " + code + "\nretrying...")
				time.sleep(1)


	def css_and_key(code, key, fail_message = "Css not found"):
		while True:
			try:
				x = wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code)))
				x.send_keys(key)
				break
			except:
				print(fail_message + ": " + code + "\nretrying...")
				time.sleep(1)


	def linktext_click(code, fail_message = "Linked text not found"):
		while True:
			try:
				x = wait.until(ExpectedConditions.presence_of_element_located((By.LINK_TEXT, code)))
				x.click()
				break
			except:
				print(fail_message + ": " + code + "\nretrying...")
				time.sleep(1)


	def go_to(address, fail_message = "Address not found"):
		while True:
			try:
				driver.get(address)
				break
			except:
				print(fail_message + ": " + address + "\nretrying...")
				time.sleep(1)

	def wait_for_xpath(code, fail_message = "Element not found"):
		while True:
			try:
				wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))
				break
			except:
				print(fail_message + ": " + code + "\nretrying...")
				time.sleep(1)

	loop_amount = int(e.get())
	try:
		file_folder = upload_path
	except Exception as wtf:
		print("ALERT - no file path selected, if your preset needs a folder path, it will crash.")
		pass
	exec(TextArea.get(1.0, END))



####UI ELEMENTS######
my_font = "Roboto"
bg = "#000000"

info = Label(text = "Please Ensure your browser is open before you start the mainloop, else the program might freeze/crash.\
	\n Press Ctrl-C in debug window to stop main loop \
	\nInput variables include (file_folder, loop_amount)",fg="white" ,bg = "#000000")
info.pack()
info.config(font=("Arial", 9))

open_browser = Button(text = "click here to Open chrome Browser(Step1)", command = open_chrome_profile, bg = "#bd2626", font=(my_font, 10))
open_browser.pack(anchor=N, pady=5, padx=5)

#File folder input
folder = Button(root, text="Add Upload Folder(Step 2)", font=(my_font, 10), bg = "orange", command=upload_folder_input)
folder.pack(anchor=N, pady=1, padx=1)

start_button = Button(text = "Upload the preset and click Start Main Loop(Step 3)", command = main_program_loop, bg = "green", font=(my_font, 10))
start_button.pack(anchor=N, pady=5, padx=5)

#number of loop entry
e = Entry(root)
e.insert(1, 1)
e.label = Label(text= "Loop amount:")
e.configure(background='#7f32a8')
e.label.pack(anchor=W, pady=0, padx=1)
e.config(font=(my_font, 8))
e.label.config(font=(my_font, 8))
e.pack(anchor=W, pady=1, padx=1)

#wait time in sec
w = Entry(root)
w.insert(1, 10)
w.label = Label(text= "Wait amount(s):")
w.configure(background='#7f32a8')
w.label.pack(anchor=W, pady=0, padx=1)
w.config(font=(my_font, 8))
w.label.config(font=(my_font, 8))
w.pack(anchor=W, pady=1, padx=1)

#port
p = Entry(root)
p.insert(1, 8989)
p.label = Label(text= "Port:")
p.configure(background='#7f32a8')
p.label.pack(anchor=W, pady=0, padx=1)
p.config(font=(my_font, 8))
p.label.config(font=(my_font, 8))
p.pack(anchor=W, pady=1, padx=1)


#Add TextArea
TextArea = Text(root, relief=GROOVE)


ln = LineNumbers(root, TextArea, width=2)
ln.pack(side=LEFT, fill=BOTH)
TextArea.pack(expand=True, fill=BOTH)
TextArea.focus()
TextArea.config(tabs=('0.5c', '1c', '1.5c', '2c'))
TextArea.config(wrap=NONE)


scrollx = Scrollbar(TextArea, orient=HORIZONTAL)
scrollx.pack(side=BOTTOM, fill=X, pady=1, padx=1)
scrollx.config(command=TextArea.xview)
TextArea.config(xscrollcommand=scrollx.set)
scrollx.config(cursor='sb_h_double_arrow')
root.mainloop()
