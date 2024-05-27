from prefect import flow, task

@flow
def hello_world():
    task_message = create_message
    print(task_message)
    something_else()

@task
def create_message():
    msg = "Hello World"
    return msg

@flow
def something_else():
    task_message = create_message
    print(task_message)
    print(" and something else.")

if __name__ == "main":
    hello_world()