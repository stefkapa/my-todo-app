FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ read a file and return the list
    of to-do items.
    """
    with open(filepath, "r") as file_local:
        """" write the to=do items in the text files2."""
        todos_local =file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

#print(__name__)

if __name__ == "__main__":
    print("hello")
    print(get_todos())