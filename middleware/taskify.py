import sys
import io
import silly_print
import time


_timer = False


def config(timer: bool):
    global _timer
    _timer = timer


tasks = []


class Task:
    def __init__(self, func):
        self.name = func.__name__
        self.body = func


def task(func):
    tasks.append(Task(func))
    return func


def run():
    initial_stdout = sys.stdout
    ostream = io.StringIO()
    sys.stdout = ostream
    names = []
    output = []
    time_counts = []
    for tsk in tasks:
        start = time.time()
        tsk.body()
        finish = time.time()
        time_counts.append(finish - start)
        names.append(tsk.name)
        output.append(ostream.getvalue())
        ostream.seek(0)
        ostream.truncate()
    sys.stdout = initial_stdout
    for task_name, task_output, task_time in zip(names, output, time_counts):
        silly_print.silly_print(f"{task_name: ^40}", fore=silly_print.Colors.Fore.BLUE)
        print("-" * 40)
        print(task_output, end='' if not len(task_output) or task_output[-1] == '\n' else '\n')
        print("-" * 40, end='\n')
        if _timer:
            silly_print.silly_print(f'{task_name} took {task_time} seconds to run',
                                    fore=silly_print.Colors.Fore.YELLOW)
        print()
