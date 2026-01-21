FILE_PATH = "todos.txt"

def greet():
    message = "hello world!!"
    new_message = message.title()
    return new_message

# greet()
# greeting = greet()
# print(greeting)

def get_avg():
    list = [5,6,7,8,9]
    values  = [float(i) for i in list]
    avg_loc = sum(values) / len(values)
    return avg_loc

def get_todos(filepath=FILE_PATH):
    """
    Read a text file and return a list of todos
    :param filepath:
    :return: todos
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath = FILE_PATH):
    """
    Write a text file to a file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print(greet())