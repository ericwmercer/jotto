'''
Created on Oct 24, 2010

@author: ola
'''
import Tkinter
import tkMessageBox
import jottoModel

root = Tkinter.Tk()
root.title("Duke Jotto")
entryList = []
spinList = []
currentIndex = 0

def disable():
    for entry,box in zip(entryList,spinList):
        entry.delete(0,Tkinter.END)
        box.selection_clear()
        box.config(values=(0,1,2,3,4,5,6),state=Tkinter.DISABLED)
        
def showVictory():
    tkMessageBox.showinfo("Duke Jotto", "I have won the game.\nI guessed your word!")
    disable()

def displayGuess():
    global entryList,currentIndex
    word = jottoModel.getGuess()
    entryList[currentIndex].insert(0,word)
    spinList[currentIndex].config(state=Tkinter.NORMAL)
    currentIndex += 1

def newGame():
    jottoModel.startGame()
    global currentIndex
    currentIndex = 0
    for entry,box in zip(entryList,spinList):
        entry.delete(0,Tkinter.END)
        box.selection_clear()
        box.config(values=(0,1,2,3,4,5,6),state=Tkinter.DISABLED)
    displayGuess()

def makeMenus():
    global root
    menubar = Tkinter.Menu(root)
    filemenu = Tkinter.Menu(menubar)
    menubar.add_cascade(label='JottoFile',menu=filemenu)
    filemenu.add_command(label='New Game',command=newGame)
    filemenu.add_command(label='Quit',command=root.quit) 
    root.config(menu=menubar)

def processCount(count):
    count = int(count)
    if count == 6:
        showVictory()
    else:
        numLeft = jottoModel.processCommon(count)
        print "number of words left is ",numLeft
        displayGuess()
    
    
def makeBox(r,c):
    global root
    global entryList
    tfont = ("Helvetica", 14, 'bold')
    entry = Tkinter.Entry(root,font=tfont,width=12)
    if r == 0:
        entry.insert(0,'     ')
    else:
        entry.insert(0,'     ')
    entry.grid(row=r,column=c)
    entryList.append(entry)
    box = Tkinter.Spinbox(root,font=tfont,width=2,
                          values=(0,1,2,3,4,5,6),state=Tkinter.DISABLED)
    box.grid(row=r,column=c+1)
    spinList.append(box)
    button = Tkinter.Button(root,text="GO",
                            font=tfont,command=lambda: processCount(box.get()))
    button.grid(row=r,column=c+2)
    
jottoModel.loadWords("kwords5.txt")
makeMenus()  
for row in range(0,20):
    makeBox(row,0)

Tkinter.mainloop()


