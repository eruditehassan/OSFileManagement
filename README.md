# OS File Management System
Operating System Level File Management System coded in Python

A brief documentation of the working of the project

## Dependencies and Libraries used
Following python libraries were used along with the purpose of use:
1. Math library was used briefly to handle a trivial calculation
2. Anytree library was obtained from pypi and a custom tree data structure was built after inheriting from the Anytree base NodeMixin class, and that tree data structure was used to keep track of the files and the memory storage locations and also for creating and visualizing a memory map.

## SYSTEM DESCRIPTION
The implemented system is a file management system. It uses a single data.dat file as a main directory which further consists of small files, which are created by user. For example, if Data.dat file is of 1000 bytes i.e. 1KB. The file is further divided into 10 tracks with size of 100 bytes each.

We implemented a tree data structure to keep records of files in a directory. Data.dat file will be parent node of the tree. This is done by using anytree library of python. When a file named file1.txt is created, it will be stored in first track which ranges from 1st byte to 100th byte (index position 0 to 99). If another file is created, it will be stored in succeeding track i.e. 2nd track. When more content is to be added into file1.txt, it will be look for next available track, for example the 3rd track.

## Directory Structure
Tree data structure is used to show the directory and the corresponding memory locations of the files in the form of track numbers.

## USER MANUAL
The user is provided with an interface to use the system.
- When user selects option 1, objects of FileObj class are created using create() function. These objects are files and are stored in files array. All these files are children of data.dat file which was set as parent node in the tree.
- When option 2 is selected, delete() function will be called which will set parent of specified file to none and remove it from the file structure.
- When option 3 is selected, the system will check if entered file exists in the file structure or not. If present, file will be opened for the user.
- When option 4 is selected, the same check will be also be applied here. If present and opened, the file will be closed.
- When user selects option 5, the system will check if specified file is present or not. If present, entered content will be written to the file. While writing to a file, a record of tracks is kept. This helps in reading operation when content of a file is spread over multiple tracks.
- When option 6 is selected, system will check if file is present or not and will be read if it is present.
- When option 7 is selected, a visual representation of the file structure will be displayed to the user. This will include children of the parent file and all the tracks which holds data of the child nodes.
- When option 8 is selected, it will exit from the system
- Any other option will give an invalid input error.
