from tkinter import Tk, END, IntVar
from tkinter.font import Font
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Notebook, Entry, Label, Frame, Button, Radiobutton, Treeview
from taskB.back import mainB
from taskC.back import mainC

columnsB = ['Title', 'Author', 'Year']
columnsC = ['Word', 'Count']

def getFilePathCSV() -> None:
    exe = askopenfilename(title='Select CSV file', filetypes=(('CSV', '*.csv*'), ('All files', '*.*')))
    if exe:
        entryPathCSV.delete(0, END)
        entryPathCSV.insert(0, exe)


def exeCSV() -> None:
    tableB.delete(*tableB.get_children())
    if entryPathCSV.get() == '':
        showwarning('Error', 'Must select the csv input file')
        return
    data = mainB(entryPathCSV.get(), variableFilter.get(), columnsB)
    for _, row in data.iterrows():
        tableB.insert('', END, values=row.tolist())


def sortTableB(table: Treeview, column, ascendent: bool) -> None:
    dataList = [(table.set(item, column), item) for item in table.get_children()]
    
    def parse(value: str):
        if column == 'Year':
            try:
                return int(value)
            except ValueError:
                return value
        return value.lower()
    
    dataList.sort(reverse=ascendent, key= lambda x: parse(x[0]))
    [table.move(item, '', index) for index, (_,item) in enumerate(dataList)]
    table.heading(column, command= lambda: sortTableB(table, column, not ascendent))


def getFilePathTXT() -> None:
    exe = askopenfilename(title='Select TXT file', filetypes=(('TXT', '*.txt*'), ('All files', '*.*')))
    if exe:
        entryPathTXT.delete(0, END)
        entryPathTXT.insert(0, exe)


def exeTXT() -> None:
    tableC.delete(*tableC.get_children())
    if entryPathTXT.get() == '':
        showwarning('Error', 'Must select the txt input file')
        return
    data = mainC(entryPathTXT.get(), columnsC)
    for _, row in data.iterrows():
        tableC.insert('', END, values=row.tolist())


def sortTableC(table: Treeview, column, ascendent: bool) -> None:
    dataList = [(table.set(item, column), item) for item in table.get_children()]
    
    def parse(value: str):
        try:
            return int(value)
        except:
            return value
    
    dataList.sort(reverse=ascendent, key= lambda x: parse(x[0]))
    [table.move(item, '', index) for index, (_,item) in enumerate(dataList)]
    table.heading(column, command= lambda: sortTableC(table, column, not ascendent))


root = Tk()
root.title('Proofpoint tasks')
root.geometry('700x480')
font = Font(family='Arial', size=10)

notebook = Notebook(root)
notebook.pack(expand=True, fill='both')

frameTaskB = Frame(notebook)
notebook.add(frameTaskB, text='Task B - Library')


labelPathCSV = Label(frameTaskB, text='Select path to .csv', font=font)
labelPathCSV.grid(row=0, column=0, padx=10, pady=10, sticky='w')
entryPathCSV = Entry(frameTaskB, width=50, font=font)
entryPathCSV.grid(row=0, column=1, pady=10, sticky='w')
entryButtonCSV = Button(frameTaskB, text='Search .csv', command=getFilePathCSV)
entryButtonCSV.grid(row=0, column=2, pady=10, sticky='w')

labelFilter = Label(frameTaskB, text='Select filter', font=font)
labelFilter.grid(row=1, column=0, padx=10, pady=10, sticky='w')
variableFilter = IntVar()
radioNone = Radiobutton(frameTaskB, text='Title', variable=variableFilter, value=0)
radioNone.grid(row=1, column=1, padx=50, pady=10, sticky='w')
radioAuthor = Radiobutton(frameTaskB, text='Author', variable=variableFilter, value=1)
radioAuthor.grid(row=1, column=1, padx=110, pady=20, sticky='w')
radioYear = Radiobutton(frameTaskB, text='Year', variable=variableFilter, value=2)
radioYear.grid(row=1, column=1, padx=180, pady=10, sticky='w')

tableB = Treeview(frameTaskB, columns=columnsB, show='headings')
tableB.grid(row=3, column=0, padx=10,  pady=10, columnspan=3)
for column in columnsB:
    tableB.heading(column, text=column, command= lambda c = column: sortTableB(tableB, c, False))
    tableB.column(column, width=160, anchor='center')

exeButtonCSV = Button(frameTaskB, text='Execute', command=exeCSV)
exeButtonCSV.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)


frameTaskC = Frame(notebook)
notebook.add(frameTaskC, text='Task C - Frequency')

labelPathTXT = Label(frameTaskC, text='Select path to .txt', font=font)
labelPathTXT.grid(row=0, column=0, padx=10, pady=10, sticky='w')
entryPathTXT = Entry(frameTaskC, width=50, font=font)
entryPathTXT.grid(row=0, column=1, padx=10, pady=10, sticky='w')
entryButtonTXT = Button(frameTaskC, text='Search .txt', command=getFilePathTXT)
entryButtonTXT.grid(row=0, column=2, padx=10, pady=10, sticky='w')

tableC = Treeview(frameTaskC, columns=columnsC, show='headings')
tableC.grid(row=3, column=0, padx=10,  pady=10, columnspan=3)
for column in columnsC:
    tableC.heading(column, text=column, command= lambda c = column: sortTableC(tableC, c, False))
    tableC.column(column, width=160, anchor='center')

exeButtonTXT = Button(frameTaskC, text='Execute', command=exeTXT)
exeButtonTXT.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)


root.mainloop()