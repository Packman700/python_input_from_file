FILE_PATH = 'example_input_file'

class __InputClass:
    def __init__(self, file_name):
        self.file_name = file_name
        self.my_input_instance = self.file_input()

    def next_line(self):
        return next(self.my_input_instance)

    def file_input(self):
        with open(self.file_name , 'r') as inp:
            for line in inp.read().splitlines():
                    yield str(line)

__input_object = __InputClass(FILE_PATH)

def input():
    return __input_object.next_line()
