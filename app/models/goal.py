from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal")


    def to_dict(self):
            task_ids = [task.task_id for task in self.tasks]
            return {"id": self.goal_id,
                    "title": self.title
                    }
    
    @classmethod
    def from_dict(cls, goal_data):
        new_goal = Goal(title=goal_data["title"])
        
        return new_goal