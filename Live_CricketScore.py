import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Listbox, Label, Button, Scrollbar

def get_live_matches():
    url = "http://static.cricinfo.com/rss/livescores.xml"
    try:
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')  # Use 'html.parser' instead of 'lxml'
        matches = [item.find('description').text for item in soup.find_all('item')]
        return matches
    except requests.exceptions.RequestException as e:
        print(f"Error fetching live matches: {e}")
        return []

def show_selected_match():
    selected_index = matches_listbox.curselection()
    if selected_index:
        selected_match = matches[selected_index[0]]
        score_label.config(text=selected_match)

# GUI setup
root = Tk()
root.title("Live Cricket Score")

matches = get_live_matches()

matches_listbox = Listbox(root, selectmode="SINGLE", height=len(matches))
for match in matches:
    matches_listbox.insert("end", match)

matches_listbox.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(root, command=matches_listbox.yview)
scrollbar.pack(side="right", fill="y")

matches_listbox.config(yscrollcommand=scrollbar.set)

show_match_button = Button(root, text="Show Match", command=show_selected_match)
show_match_button.pack()

score_label = Label(root, text="", wraplength=300, justify="left")
score_label.pack()

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
