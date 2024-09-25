import unittest
from database import add_task, show_tasks

class TestTaskManager(unittest.TestCase):

    def test_add_task(self):
        add_task("Test Task")
        tasks = show_tasks()
        self.assertTrue(any(task[1] == "Test Task" for task in tasks))

if __name__ == '__main__':
    unittest.main()
