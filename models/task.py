class TaskManager:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed 

    def to_dict(self): 
        return {
            "title": self.title,
            "id": self.id,
            "description": self.description,
            "completed": self.completed
        }