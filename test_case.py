import unittest
from  to_do_list import ToDoList, Task

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo = ToDoList()
        self.todo.add_task("Make homework", "You need to do your python homework", "20.02.2025", "Medium")
        self.todo.add_task("Call mom", "Call mom and wish happy birthday", "18.02.2025", "High")

    def test_add_task(self):
        self.todo.add_task("Buy some products", "Buy milk, cheese and beef", "17.02.2025", "Low")
        self.assertTrue(self.todo.task_exists("Buy some products"))

    def test_add_duplicated(self):
        with self.assertRaises(ValueError):
            self.todo.add_task("Call mom", "Call mom and wish happy birthday", "18.02.2025", "High")

    def test_deleting_tusk(self):
        self.todo.delete_task('Make homework')
        self.assertFalse(self.todo.task_exists('Make homework'))

    def test_delete_nonexistent_task(self):
        with self.assertRaises(NameError):
            self.todo.delete_task("Nonexistent Task")

    def test_delete_all_list(self):
        self.todo.delete_all_tasks()
        self.assertTrue(len(self.todo.task_list) == 0)

    def test_change_status(self):
        self.todo.change_status("Call mom", True)
        self.assertTrue(self.todo.show_completed_tasks()[0].status)

    def test_show_completed_tasks_empty(self):
        with self.assertRaises(ValueError):
            self.todo.show_completed_tasks()

    def test_sort_by_priority(self):
        sorted_tasks = self.todo.sort_by_priority()
        self.assertEqual(sorted_tasks[0].priority, "High")
        self.assertEqual(sorted_tasks[1].priority, "Medium")

    def test_edit_the_task(self):
        self.todo.edit_the_task('Make homework',"Write test cases using Python unittest")
        for task in self.todo.task_list:
            if task.task_title == 'Make homework':
                self.assertEqual(task.task_text,"Write test cases using Python unittest")

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            Task("Invalid Task", "Text", "2025-01-01", "InvalidPriority")

if __name__ == "__main__":
    unittest.main()
