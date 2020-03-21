from locust import Locust, TaskSet, task


class ExamplesTasks(TaskSet):
    @task
    def do_smth_evil(self):
        pass

    @task
    def do_smth_interesting(self):
        pass


class ExampleLocust(Locust):
    task_set = ExamplesTasks
