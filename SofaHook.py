import customtkinter as ctk
import requests
import json

# Initialize the customtkinter window
app = ctk.CTk()
app.geometry("800x450")
app.title("Discord Webhook Manager")

# Set a uniform padding value
padding = {"padx": 20, "pady": 10}

# Define the delete webhook function
def delete_webhook():
    webhook_url = webhook_entry.get()
    if webhook_url:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            status_label.configure(text="Webhook deleted successfully", text_color="green")
        else:
            status_label.configure(text="Failed to delete webhook", text_color="red")
    else:
        status_label.configure(text="Please enter a webhook URL", text_color="red")

# Define the send message function
def send_message():
    webhook_url = webhook_entry.get()
    message = message_entry.get()
    if webhook_url and message:
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            status_label.configure(text="Message sent successfully", text_color="green")
        else:
            status_label.configure(text="Failed to send message", text_color="red")
    else:
        status_label.configure(text="Please enter both a webhook URL and a message", text_color="red")

# Define the get webhook info function
def get_webhook_info():
    webhook_url = info_webhook_entry.get()
    if webhook_url:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            info = json.loads(response.text)
            info_text.configure(state="normal")
            info_text.delete(1.0, ctk.END)
            info_text.insert(ctk.END, json.dumps(info, indent=4))
            info_text.configure(state="disabled")
            info_status_label.configure(text="Webhook info retrieved successfully", text_color="green")
        else:
            info_status_label.configure(text="Failed to retrieve webhook info", text_color="red")
    else:
        info_status_label.configure(text="Please enter a webhook URL", text_color="red")

# Function to show the manage frame
def show_manage_frame():
    manage_frame.pack(fill='both', expand=True)
    info_frame.pack_forget()

# Function to show the info frame
def show_info_frame():
    info_frame.pack(fill='both', expand=True)
    manage_frame.pack_forget()

# Function to clear inputs in manage frame
def clear_manage_inputs():
    webhook_entry.delete(0, ctk.END)
    message_entry.delete(0, ctk.END)
    status_label.configure(text="")

# Function to clear inputs in info frame
def clear_info_inputs():
    info_webhook_entry.delete(0, ctk.END)
    info_text.configure(state="normal")
    info_text.delete(1.0, ctk.END)
    info_text.configure(state="disabled")
    info_status_label.configure(text="")

# Create frames for "Manage Webhook" and "Webhook Info"
manage_frame = ctk.CTkFrame(app)
info_frame = ctk.CTkFrame(app)

# Create the buttons to switch between frames
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10, fill='x')

manage_button = ctk.CTkButton(button_frame, text="Manage Webhook", command=show_manage_frame)
manage_button.pack(side="left", padx=10, pady=10)

info_button = ctk.CTkButton(button_frame, text="Webhook Info", command=show_info_frame)
info_button.pack(side="left", padx=10, pady=10)

# "Manage Webhook" frame contents
webhook_frame = ctk.CTkFrame(manage_frame)
webhook_frame.pack(pady=20, padx=20, fill="x")

webhook_label = ctk.CTkLabel(webhook_frame, text="Webhook:")
webhook_label.pack(side="left", **padding)

webhook_entry = ctk.CTkEntry(webhook_frame, width=300, placeholder_text="Enter Discord Webhook URL")
webhook_entry.pack(side="left", **padding)

message_frame = ctk.CTkFrame(manage_frame)
message_frame.pack(pady=10, padx=20, fill="x")

message_label = ctk.CTkLabel(message_frame, text="Message:")
message_label.pack(side="left", **padding)

message_entry = ctk.CTkEntry(message_frame, width=300, placeholder_text="Enter message to send")
message_entry.pack(side="left", **padding)

button_frame = ctk.CTkFrame(manage_frame)
button_frame.pack(pady=20, padx=20, fill="x")

delete_button = ctk.CTkButton(button_frame, text="Delete Webhook", command=delete_webhook)
delete_button.pack(side="left", padx=10, pady=10, expand=True)

send_button = ctk.CTkButton(button_frame, text="Send Message", command=send_message)
send_button.pack(side="left", padx=10, pady=10, expand=True)

clear_manage_button = ctk.CTkButton(manage_frame, text="Clear", command=clear_manage_inputs)
clear_manage_button.pack(pady=10)

status_label = ctk.CTkLabel(manage_frame, text="")
status_label.pack(pady=20)

# "Webhook Info" frame contents
info_webhook_frame = ctk.CTkFrame(info_frame)
info_webhook_frame.pack(pady=20, padx=20, fill="x")

info_webhook_label = ctk.CTkLabel(info_webhook_frame, text="Discord Webhook URL:")
info_webhook_label.pack(side="left", **padding)

info_webhook_entry = ctk.CTkEntry(info_webhook_frame, width=300, placeholder_text="Enter Discord Webhook URL")
info_webhook_entry.pack(side="left", **padding)

get_info_button = ctk.CTkButton(info_webhook_frame, text="Get Info", command=get_webhook_info, width=100)
get_info_button.pack(side="left", padx=10, pady=10)

info_text = ctk.CTkTextbox(info_frame, width=500, height=200, state="disabled")
info_text.pack(pady=10, padx=20)

clear_info_button = ctk.CTkButton(info_frame, text="Clear", command=clear_info_inputs)
clear_info_button.pack(pady=10)

info_status_label = ctk.CTkLabel(info_frame, text="")
info_status_label.pack(pady=20)

# Show the initial frame
show_manage_frame()

# Run the app
app.mainloop()
