# hashmap-implementation-python

This project implements the basic functionality of a hash map (initialization, hash function, insertion, deletion, and retrieval) using lists. It runs in amortized constant time for insertion, deletion, and retrieval (assuming the hash function is not changed, the values to be hashed are not incredibly numerous, and the size of the HashMap is appropriate). This project also contains PyUnit tests, which tests each of these functions to ensure they work as desired.

GETTING STARTED: Follow the instructions below to install all necessary software.

PREREQUISITES: Computer with necessary specifications to run Python and other necessary files. Python 3.6 or greater (Install here: https://www.python.org/downloads/). See installation help videos here: Mac: https://www.youtube.com/watch?v=uA8SA81nivg and Windows: https://www.youtube.com/watch?v=dX2-V2BocqQ. Optional: Python IDE other than Python IDLE (https://www.jetbrains.com/pycharm/download/#section=mac). See installation help video here for Python IDE(PyCharm): https://www.youtube.com/watch?v=-9YhPrtWz6Q

INSTALLING: Download hashmap.py and test_hashmap.py from https://github.com/andrewjoliver/hashmap-implementation-python. Open hashmap.py and test_hashmap.py using desired Python IDE (or the default Python IDLE)

RUNNING THE TESTS. In desired IDE, run test_hashmap.py using run command. Additionally, you can run these tests from the terminal. First, navigate to the directory of test_hashmap.py. Second, type into the terminal “python test_hashmap.py” and execute the command (hit enter)

DEPLOYMENT: Not ready to be deployed on a live system at this point

FURTHER DEVELOPMENT: Further development of this project may include: Development of .contains() function for determining if a key/value exists in the map, development of a .clear() function and an .is_empty() function, development of a .size() function to return number of non null Key-Value pairs, increased development of hash function (to further prevent collisions)
  
AUTHORS: Andrew Oliver - (Initial Build) - andrewjoliver

LICENSE: This project is licensed under the MIT License - see the LICENSE file for details.

ACKNOWLEDGEMENTS: The resources listed below were used in development of the implementation and tests. https://www.geeksforgeeks.org/hashmap-class-methods-java-examples-set-1-put-get-isempty-size/
https://www.youtube.com/watch?v=MfhjkfocRR0
https://docs.python.org/2/tutorial/datastructures.html
https://www.youtube.com/watch?v=9HFbhPscPU0&t=72s
https://www.cs.hmc.edu/~geoff/classes/hmc.cs070.200101/homework10/hashfuncs.html
https://www.youtube.com/watch?v=6tNS--WetLI
https://stackoverflow.com/questions/4393268/how-to-raise-a-valueerror
http://www.pythonforbeginners.com/error-handling/python-try-and-except
