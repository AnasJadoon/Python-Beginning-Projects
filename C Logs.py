import os
import time
import threading
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import winreg
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import scrolledtext, Tk, END

log_file_path = 'C_drive_log.txt'


class LogHandler:
    def __init__(self, log_file):
        self.log_file = log_file
        self.previous_log = set()
        self.load_existing_logs()

    def load_existing_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as log_file:
                for line in log_file:
                    self.previous_log.add(line)

    def update_log(self, event_type, path):
        try:
            log_entry = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {event_type}: {path}\n"
            if log_entry not in self.previous_log:
                self.previous_log.add(log_entry)
                with open(self.log_file, 'a') as log_file:
                    log_file.write(log_entry)
        except Exception as e:
            print(f"Failed to write log: {e}")

    def get_logs(self):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, 'r') as log_file:
                    return log_file.read()
            except Exception as e:
                print(f"Failed to read log file: {e}")
        return ""


log_handler = LogHandler(log_file_path)


class FileChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        log_handler.update_log("File created", event.src_path)

    def on_modified(self, event):
        log_handler.update_log("File modified", event.src_path)

    def on_deleted(self, event):
        log_handler.update_log("File deleted", event.src_path)


def monitor_software_installations():
    installed_software = set()

    uninstall_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, uninstall_key) as key:
            for i in range(winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)
                try:
                    display_name = winreg.QueryValueEx(subkey, 'DisplayName')[0]
                    if display_name not in installed_software:
                        installed_software.add(display_name)
                        log_handler.update_log("Software installed", display_name)
                except OSError:
                    continue
    except Exception as e:
        print(f"Failed to monitor software installations: {e}")


def get_drive_space():
    try:
        usage = psutil.disk_usage('C:\\')
        total = usage.total / (1024 ** 3)
        used = usage.used / (1024 ** 3)
        free = usage.free / (1024 ** 3)
        return total, used, free
    except Exception as e:
        print(f"Failed to get drive space: {e}")
        return 0, 0, 0


def create_image():
    # Generate an image and draw a pattern
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), 'white')
    dc = ImageDraw.Draw(image)

    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill='black')

    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill='black')

    return image


def open_log_window():
    def close_log_window():
        root.quit()
        root.destroy()

    root = Tk()
    root.title("Log Viewer")
    root.geometry('600x400')

    log_text = scrolledtext.ScrolledText(root, width=70, height=30)
    log_text.pack()
    log_text.insert(END, log_handler.get_logs())

    close_button = tk.Button(root, text="Close", command=close_log_window)
    close_button.pack()

    root.protocol("WM_DELETE_WINDOW", close_log_window)
    root.mainloop()


def main():
    def on_quit(icon, item):
        icon.stop()
        os._exit(0)

    def on_view_logs(icon, item):
        threading.Thread(target=open_log_window).start()

    menu = (item('View Logs', on_view_logs), item('Quit', on_quit))
    icon = pystray.Icon("MonitorService", create_image(), "Monitoring Service", menu)

    observer = Observer()
    event_handler = FileChangeHandler()
    observer.schedule(event_handler, 'C:\\', recursive=True)
    observer.start()

    def monitoring():
        while True:
            try:
                monitor_software_installations()
                total, used, free = get_drive_space()
                drive_space_log = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Drive space: Total: {total:.2f} GB, Used: {used:.2f} GB, Free: {free:.2f} GB\n"
                if drive_space_log not in log_handler.previous_log:
                    log_handler.update_log("Drive space", drive_space_log)
                time.sleep(5)
            except Exception as e:
                print(f"Monitoring loop exception: {e}")

    monitoring_thread = threading.Thread(target=monitoring)
    monitoring_thread.daemon = True
    monitoring_thread.start()

    icon.run()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Service main loop exception: {e}")
