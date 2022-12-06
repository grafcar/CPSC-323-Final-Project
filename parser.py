class CompilerData:
    def __init__(self):
        self.file_loc = None
        self.data = []
        self.reserved_words = ["var", "begin", "end"]
        self.non_terminals = []
        self.terminals = []
        self.rules = []
        self.rules_old = []
        self.start_symbol = 0

class FileOpener:
    def __init__(self, compiler_data):
        self.compiler_data = compiler_data
        self.comment_found = 0
        self.new_format = ""

    def verify_comment(self):
        if self.comment_found == 0:
            return 1
        return 0

    def format(self, data):
        data_list = data.split()
        for dl in data_list:
            if dl == "**":
                self.comment_found = self.verify_comment()
            elif self.comment_found == 0:
                self.compiler_data.data.append(dl)

    def build(self):
        for x in self.compiler_data.data:
            if x == ";":
                self.new_format += (str(x) + "\n")
            elif x in self.compiler_data.reserved_words:
                self.new_format += (str(x) + "\n")
            elif x.find(";") != -1:
                self.new_format += (str(x[:-1]) + " ;\n")
            else:
                self.new_format += (str(x) + " ")
        print(self.new_format)

    def start(self):
        data = open(self.compiler_data.file_loc, "r")
        for of in data:
            self.format(data=of)
        data.close()
        self.build()

class Compiler:
    def __init__(self, file_loc):
        self.compiler_data = CompilerData()
        self.compiler_data.file_loc = file_loc
        self.file_opener = FileOpener(compiler_data=self.compiler_data)

    def start(self):
        self.file_opener.start()


def main():
    c = Compiler(file_loc="finalp1.txt")
    c.start()


if __name__ == "__main__":
    main()