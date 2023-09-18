from django.test import TestCase
from portfolio_app.models import Task


class TaskModelTestCase(TestCase):

    def setUp(self):
        self.task1 = Task.objects.create(
            title = 'task1',
            description = 'description to task 1',
        )
        self.task2 = Task.objects.create(
            title='task2',
            description='description to task 2',
        )

    def test_get_all_tasks(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 2)

    def test_get_task_by_id(self):
        retrieved_task = Task.objects.get(id=self.task1.id)
        self.assertEqual(retrieved_task.title, 'task1')
        self.assertEqual(retrieved_task.description, 'description to task 1')

        retrieved_task = Task.objects.get(id=self.task2.id)
        self.assertEqual(retrieved_task.title, 'task2')
        self.assertEqual(retrieved_task.description, 'description to task 2')

