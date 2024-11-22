import tkinter as tk

class DataAnalysisApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Analysis Application")

        # Create a button
        self.btn = tk.Button(self.root, text="Analyze Data", command=self.analyze_data)
        self.btn.pack(padx=20, pady=20)

        # List to store event data
        self.event_data = []

        # Bind the '<Button-1>' event to the 'on_change' method
        self.root.bind("<Button-1>", self.on_change)

        # Start the event loop
        self.root.mainloop()

    def on_change(self, event):
        # Append the event data to the list
        self.event_data.append((event.x, event.y))

        # Call the callback function (if provided)
        if self.callback:
            self.callback(self.event_data)

    def analyze_data(self):
        # Example of using a higher-order function (lambda) to handle the event data
        self.callback = lambda data: print(f"Analyzing data: {data}")
        
        # Call the 'on_change' method to trigger the event and process the data
        self.on_change(tk.Event(type='<Button-1>', x=100, y=200))

if __name__ == "__main__":
    app = DataAnalysisApp()
