import unittest
from database import add_task, show_tasks

class TestShowTasks(unittest.TestCase):
    def test_show_tasks(self):
        task_description = "Test task for display"
        add_task(task_description)
        
        tasks = show_tasks()
        self.assertIn(task_description, [task[1] for task in tasks])

if __name__ == '__main__':
    unittest.main()
