import tkinter as tk
from scapy.all import sniff
import threading

root = tk.Tk()
root.title("Personal Firewall Monitor")

text_area = tk.Text(root, width=80, height=20)
text_area.pack()

def packet_callback(packet):
    text_area.insert(tk.END, f"{packet.summary()}\n")
    text_area.see(tk.END)

threading.Thread(target=lambda: sniff(prn=packet_callback, store=0), daemon=True).start()
root.mainloop()
