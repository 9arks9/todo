from datetime import datetime

class Task:
    def __init__(self, title, description, done=False, creation_date=None, progress_txt=None):
        self.title = title
        self.description = description
        self.done = done
        self.creation_date = creation_date if creation_date else datetime.now().strftime("[%Y-%m-%d][%H:%M]")
        self.progress_txt = progress_txt if progress_txt else ('-[✔]-' if done else '-[ ]-')
        self.done_txt_tr = '-[✔]-'

    def done_setter(self):
        self.progress_txt = self.done_txt_tr
        self.done = True
        self.creation_date = datetime.now().strftime("[%Y-%m-%d][%H:%M]")

    def display(self):
        return f'{self.progress_txt}{self.creation_date}- {self.title}: {self.description} '

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "creation_date": self.creation_date,
            "progress_txt": self.progress_txt
        }
