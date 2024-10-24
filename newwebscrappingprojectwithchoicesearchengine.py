import tkinter as tk
import webbrowser
import requests
from bs4 import BeautifulSoup

def search_and_display(query, search_engine):
    search_engines = {
        "Google": "https://www.google.com/search?q=",
        "Bing": "https://www.bing.com/search?q=",
        "DuckDuckGo": "https://duckduckgo.com/?q=",
        # Add more search engines here
    }

    url = search_engines[search_engine] + query
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant information from the search results, including all links
    links = soup.find_all('a')
    results = []
    for link in links:
        href = link.get('href')
        if href and href.startswith('http'):
            results.append(href)

    # Update the listbox with the new results
    listbox.delete(0, tk.END)
    for result in results[:10]:  # Limit to 10 results
        listbox.insert(tk.END, result)

def open_url(event):
    selected_url = listbox.get(tk.ACTIVE)
    webbrowser.open_new_tab(selected_url)

# Create the main window
def on_resize(event):
    # Adjust window size based on content or other factors
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")

root = tk.Tk()
root.geometry("600x400")  # Set width and height in pixels
#root.bind("<Configure>", on_resize)
root.title("Search Engine Explorer")

# Create a label and entry for user input
label = tk.Label(root, text="Enter your search query:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Define the search engines dictionary
search_engines = {
    "Google": "https://www.google.com/search?q=",
    "Bing": "https://www.bing.com/search?q=",
    "DuckDuckGo": "https://duckduckgo.com/?q=",
    # Add more search engines here
}

# Create a dropdown menu for search engines
search_engine_var = tk.StringVar()
search_engine_var.set("Google")  # Default search engine
search_engine_menu = tk.OptionMenu(root, search_engine_var, *search_engines.keys())
search_engine_menu.pack()

# Create a button to trigger the search
button = tk.Button(root, text="Search", command=lambda: search_and_display(entry.get(), search_engine_var.get()))
button.pack()

# Create a listbox to display search results
def on_resize(event):
    listbox.config(width=root.winfo_width(), height=root.winfo_height())

root.bind("<Configure>", on_resize)
listbox = tk.Listbox(root)
listbox.pack()

# Bind the listbox click event to open the URL
listbox.bind("<Button-1>", open_url)

root.mainloop()