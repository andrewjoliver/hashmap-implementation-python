'''
Created on Jan 17, 2018

@author: andrewoliver
'''
import unittest
from hashmap import HashMap


class TestHashMap(unittest.TestCase):

    def test_init(self):
        h = HashMap(64)
        self.assertEqual(h.size, 64, "Initial size of array is not 64.")
        try:
            HashMap(-64)
        except ValueError:
            print("Size of HashMap is less than 0 error caught.")

    def test_generate_hash(self):
        self.assertEqual(HashMap.generate_hash(HashMap(64), "cat"), 3)
        self.assertNotEqual(HashMap.generate_hash(HashMap(64), "cta"), 3)
        self.assertNotEqual(HashMap.generate_hash(HashMap(64), "tac"), 3)
        self.assertEqual(HashMap.generate_hash(HashMap(64), ""), 11)
        self.assertEqual(HashMap.generate_hash(HashMap(64), "!#$"), 19)
        self.assertEqual(HashMap.generate_hash(HashMap(64), "a a a"), 62)
        
        try:
            HashMap.generate_hash(HashMap(64), None)
        except ValueError:
            print("Null hash value has not been generated.")

    def test_insertion(self):
        h = HashMap(64)
        h.insert("one", 1)
        h.insert("two", 2)
        
        self.assertEquals(h.hashmap[29], [['one', 1]], "(one, 1) was not inserted correctly")  # hash value for one is 29
        self.assertEquals(h.hashmap[37], [['two', 2]], "(two, 2) was not inserted correctly")  # hash value for two is 37
        
        h.insert("three", 3)
        h.insert("four", 4)
        
        count = 0
        for x in range(0, 64):
            if h.hashmap[x] is not None:
                count += 1
        
        self.assertEquals(
            count,
            4,
            "Exactly 4 elements have not been added to the list")
        
        try:
            h.insert(None, 5)
        except ValueError:
            print("Insertion of null value has been caught.")

    def test_removal(self):
        h = HashMap(64)

        h.insert("one", 1)
        h.insert("two", 2)
        h.insert("three", 3)

        h.remove("one")
        h.remove("two")
        h.remove("three")

        for x in range(0, 64):
            self.assertFalse(h.hashmap[x] == "one", "HashMap entry with key one has not been deleted.")
            self.assertFalse(h.hashmap[x] == "two", "HashMap entry with key two has not been deleted.")
            self.assertFalse(h.hashmap[x] == "three", "HashMap entry with key three has not been deleted.")
            
        self.assertFalse(h.remove("four"), "Removal of key that was not added is true.")
        
        try:
            h.remove(None)
        except ValueError:
            print("Removal of null value exception has been caught.")
        
    def test_get(self):
        h = HashMap(64)
        h.insert("one", 1)
        
        self.assertEquals(h.get("one"), 1, "Value of 1 was not returned for key of one")
        self.assertNotEqual(h.get("two"), 2, "Value of 2 was not returned for key of two")
        
        #N.B. cat and H have same hash value
        h.insert("cat", 1)
        h.insert("H", 2)
        
        self.assertEqual(h.generate_hash("cat"), h.generate_hash("H"), "Values are not the same.")
        self.assertEquals(h.get("H"), 2, "Value of @ is not 2")
        
        try:
            h.get(None)
        except ValueError:
            print("Retrieval of null value error has been caught.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
