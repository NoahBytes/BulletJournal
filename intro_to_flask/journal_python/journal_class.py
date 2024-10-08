import os
from datetime import datetime

class Journal:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content
        self.filename = self.create_filename(title)
        self.created_at = datetime.now()

    def create_filename(self, title):
        return f"{title.replace(' ', '_')}.md"

    def save(self, directory="journals"):
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        #Save the content to a markdown file in the directory
        with open(os.path.join(directory, self.filename), 'w') as file:
            file.write(self.content)
        
    def load(self, directory="journals"):
        try:
            with open(os.path.join(directory, self.filename), 'r') as file:
                self.content = file.read()
        except FileNotFoundError:
            self.content = None
            raise Exception("Journal file not found")

    def delete(self, directory="journals"):
        try:
            os.remove(os.path.join(directory, self.filename))
        except FileNotFoundError:
            raise Exception("Journal file not found")