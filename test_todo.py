"""Unit tests for the core project. Run with:  python -m unittest test_todo -v"""
import io
import unittest
from contextlib import redirect_stdout

from todo import add_task, view_tasks


class TestAddTask(unittest.TestCase):
    def test_adds_task_to_list(self):
        tasks = []
        self.assertTrue(add_task(tasks, "Finish Python assignment"))
        self.assertEqual(tasks, ["Finish Python assignment"])

    def test_strips_whitespace(self):
        tasks = []
        add_task(tasks, "   Buy Milk   ")
        self.assertEqual(tasks, ["Buy Milk"])

    def test_rejects_empty_task(self):
        tasks = []
        self.assertFalse(add_task(tasks, "    "))
        self.assertEqual(tasks, [])

    def test_keeps_order(self):
        tasks = []
        for t in ["A", "B", "C"]:
            add_task(tasks, t)
        self.assertEqual(tasks, ["A", "B", "C"])


class TestViewTasks(unittest.TestCase):
    def capture(self, tasks):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            view_tasks(tasks)
        return buffer.getvalue()

    def test_empty_list_message(self):
        self.assertIn("No tasks yet", self.capture([]))

    def test_numbered_output(self):
        out = self.capture(["Buy Milk", "Walk Dog"])
        self.assertIn("1. Buy Milk", out)
        self.assertIn("2. Walk Dog", out)
        self.assertIn("Total tasks: 2", out)


if __name__ == "__main__":
    unittest.main()
