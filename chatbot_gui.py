
import tkinter as tk

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Ask me anything about college.",
    "admission": "Admissions usually open in June. Check the official website for updates.",
    "courses": "Our college offers programs like B.Tech, BBA, MBA and more.",
    "fees": "Fee details are available on the official college website.",
    "hostel": "Yes, hostel facilities are available for students.",
    "placement": "Our college provides placement support and career guidance.",
    "bye": "Goodbye! Have a great day!"
}

def get_response(user_text):
    user_text = user_text.lower()
    for key in responses:
        if key in user_text:
            return responses[key]
    return "Sorry, I don't understand that yet."

def send_message():
    user_text = entry.get()
    chat.insert(tk.END, "You: " + user_text + "\n")
    reply = get_response(user_text)
    chat.insert(tk.END, "Bot: " + reply + "\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI Student Chatbot")

chat = tk.Text(root, height=20, width=50)
chat.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()
