import unittest
from database import add_task, complete_task, show_tasks

class TestCompleteTask(unittest.TestCase):
    def test_complete_task(self):
        task_description = "Test task for completion"
        add_task(task_description)
        tasks = show_tasks()
        task_id = tasks[-1][0]
        
        complete_task(task_id)
        tasks = show_tasks()
        
        for task in tasks:
            if task[0] == task_id:
                self.assertTrue(task[2])  # Tamamlandı mı kontrol et

if __name__ == '__main__':
    unittest.main()
