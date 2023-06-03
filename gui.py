import tkinter as tk
from Search import search
import time
def display():
    pass

def main():
    def start_search():
        # gets the query from search
        query = entry.get()
        # gets the first time
        t1 = time.time()
        # processes the query by calling search
        links = search(query)
        # after search is done we get the second time 
        t2 = time.time()
        # configures newList to be the time difference between t2 and t1 and then prints it out
        newList[0].configure(text=str(t2-t1) + " Seconds")
        newList[0].grid(row=1, column=5, padx=5, pady=5,)
        # processing of the links that were obtained from search
        docs = links[0]
        finalizedLinks = links[1]
        count = 0
        # puts it all into label_list
        for item in finalizedLinks:
            label_list[count].configure(text=docs[str(item[0])])
            count += 1
        count = 0
        # prints everything in label list out
        for i in label_list:
            i.grid(row= 6 + count, column=5, padx=5, pady=5, sticky="w")
            count += 1
    
    def clear_tk():
        # clearing the link list and prints it out as nothing to clear it up.
        for i in range(0, 10):
            label_list[i].configure(text="")
        count = 0
        for i in label_list:
            i.grid(row=5 + count, column=5, padx=5, pady=5)
            count += 1

        
    # creating a tkinter object
    window = tk.Tk()
    # creating the window
    window.geometry("400x400")
    # Create a search button
    search_button = tk.Button(window, text='Search', command=start_search)
    search_button.grid(row=1, column = 5, sticky=tk.W)
    # Create an Entry widget for the search bar
    entry = tk.Entry(window, font=('Arial', 16), width= 20)
    entry.grid(row=0, column = 5, sticky=tk.W)

    # Creating output Labels
    label_list = [] # where the linkss stored
    newList = [] # where the time is stored
    newList.append(tk.Label(window, text="", font=('Arial', 12)))
    for i in range(11):
        label_list.append(tk.Label(window, text="", font=('Arial', 12)))
    # after it's done make sure it's cleared before printing again
    clear_tk()
    # Start the main event loop
    window.mainloop()

if __name__ == "__main__":
    main()
    