# import Libraries
import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Set the path for the directory to track changes
from_dir =  "<Set path for tracking file system events>"

#Write a FileEventHandler Class with following methods to track file system eventsb (See Hint 1)
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey there!, {event.src_path} has been created")
    
    def on_deleted(self, event):
        print(f"Oops! Someone deleted, {event.src_path} !")

    def on_modified(self, event):
        print(f"Hey there!, {event.src_path} has been modified")
    
    def on_moved(self, event):
        print(f"Someone moved {event.src_path} to {event.dest_path}")

# Initialize Event Handler Class
event_handler = FileEventHandler()
# Initialize Observer
observer = Observer()
# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)
# Start the Observer
observer.start()
#Code to stop observer on key press:(Check hint 2)
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()