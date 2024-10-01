import unittest
from database import add_task, delete_task, show_tasks

class TestDeleteTask(unittest.TestCase):
    def test_delete_task(self):
        task_description = "Test task for deletion"
        add_task(task_description)
        tasks = show_tasks()
        task_id = tasks[-1][0] 
        
        delete_task(task_id)
        tasks = show_tasks()
        
        self.assertNotIn(task_description, [task[1] for task in tasks])

if __name__ == '__main__':
    unittest.main()
