from anytree import Node, RenderTree, NodeMixin
from math import floor


class DataNode(NodeMixin):  
    def __init__(self, name, parent=None, children=None):
        super(DataNode, self).__init__()
        self.name = name
        self.parent = parent
        if children:
            self.children = children

files = {}
nodes = {}

# Root file class

class root_file():
    def __init__(self,name = "data.dat", size = 1000, track_size = 100):
        self.name = name
        self.size = size
        self.track_size = track_size
        self.available_tracks = list(range(1,floor(size / track_size) + 1))
        self.used_tracks = []


    def create_file(self):
        self.f = open(self.name, 'wb')
        self.f.seek(self.size-1)
        self.f.write(b"\0")
        self.f.close()

    def write_to_file(self, text):
        self.f = open(self.name, 'r+b')
        if self.available_tracks != []:
            self.f.seek((self.available_tracks[0] - 1 )*self.track_size)
            self.f.write(text.encode('utf-8'))
            temp = self.available_tracks.pop(0)
            self.used_tracks.append(temp)

    def read_from_file(self,track_list,bytes_on_tracks):
            output = ""
            f = open("data.dat", "rb")
            for t in track_list:
                f.seek((t-1)*self.track_size)
                output += f.read(bytes_on_tracks[t]).decode('utf-8')
            f.close()
            return output.strip()


root = root_file()
nodes["root"] = DataNode(root.name)

class FileObj():
    def __init__(self,name,mode,root_file = root):
        self.name = name
        self.mode = mode
        self.size = 0
        self.track = 0
        self.size_on_track = 0
        self.root_file = root_file
        self.file_tracks = []
        self.bytes_on_tracks = {}

    def write_to_file(self,text):
        self.content = text
        self.root_file.write_to_file(self.content)
        track_num = self.root_file.used_tracks[-1]
        self.file_tracks.append(track_num)
        self.bytes_on_tracks[track_num] = len(text)
        nodes[track_num] = DataNode(track_num, parent=nodes[self.name])

    def read_from_file(self):
        output = self.root_file.read_from_file(self.file_tracks,self.bytes_on_tracks)
        return output

# Main required Functions
def open_file(fname):
    files[fname] = FileObj(fname,mode)
    return files[fname]

def create(fname, p = nodes["root"]):
    open_file(fname)
    nodes[fname] = DataNode(files[fname].name, parent=p)

def delete(fname):
    nodes[fname].parent = None

def close(fname):
    delete(fname)

def show_memory_map():
    for pre, fill, node in RenderTree(nodes["root"]):
        print("%s%s" % (pre, node.name))


while True:
    print("What operation do you want to perform:\n1. Create File \n2. Delete File \n3. Open File \n4. Close File \n5. Write to file \n6. Read from file \n7. Show memory map \n8. Exit")
    decision = int(input())
    if (decision == 1):
        file_name = input("Enter the name of the file: ")
        create(file_name)
        print("File created!")
    elif (decision == 2):
        file_name = input("Enter the name of the file: ")
        if file_name in files.keys():
            delete(file_name)
            print("File deleted")
        else:
            print("File does not exist")
    elif (decision == 3):
        file_name = input("Enter the name of the file: ")
        if file_name in files.keys():
            f = open(file_name)
            print("File opened")
        else:
            print("File does not exist")

    elif (decision == 4):
        file_name = input("Enter the name of the file: ")
        if file_name in files.keys():
            close(file_name)
            print("File closed")
        else:
            print("File does not exist")

    elif (decision == 5):
        file_name = input("Enter the name of the file: ")
        if file_name in files.keys():
            text = input("Enter the text to be written on file: ")
            files[file_name].write_to_file(text)
            print("Given content written to file successfully!")
        else:
            print("File does not exist")

    elif (decision == 6):
        file_name = input("Enter the name of the file: ")
        if file_name in files.keys():
            print("Reading from file: ")
            print(files[file_name].read_from_file())
        else:
            print("File does not exist")

    elif (decision == 7):
        show_memory_map()
    
    elif (decision == 8):
        break
    else:
        print("Invalid input")
