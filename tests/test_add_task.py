import unittest
from database import add_task, show_tasks

class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        task_description = "Test task"
        add_task(task_description)
        tasks = show_tasks()
        self.assertIn(task_description, [task[1] for task in tasks])

if __name__ == '__main__':
    unittest.main()
