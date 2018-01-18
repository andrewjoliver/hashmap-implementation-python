'''
Created on Jan 17, 2018

@author: andrewoliver
'''


class HashMap():

    def __init__(self, size):
        if (size < 0):
            raise ValueError("The input for size must be an integer greater than 0.")
        self.size = size
        self.hashmap = [None] * self.size  # initial placeholder for length

    def generate_hash(self, key):
        if (key is None):
            raise ValueError("Cannot generate a hash value for null key.")
        hash_code = 11
        for unicode_character in str(key):
            hash_code = (hash_code * 17 + ord(unicode_character)) % self.size
        return hash_code

    def insert(self, key, value):
        if (key is None):
            raise ValueError("Key or Value entered cannot have a null value")
        
        key_hash_code = self.generate_hash(key)
        kvpair = [key, value]

        if self.hashmap[key_hash_code] is None:
            self.hashmap[key_hash_code] = list([kvpair])
            #print("Key-Value Pair has been added successfully.")
            return True
        else:
            for each_pair in self.hashmap[key_hash_code]:
                if each_pair[0] == key:
                    each_pair[1] = value
                    #print("Key-Value Pair exists already. Value has been updated.")
                    return True
            self.hashmap[key_hash_code].append(kvpair)
            #print("New Key-Value Pair has been added.)"
            return True

    def remove(self, key):
        if (key is None):
            raise ValueError("Cannot remove Key-Value Pair with null key entered.")
        
        key_hash_code = self.generate_hash(key)

        if self.hashmap[key_hash_code] is None:
            #print("Key-Value Pair does not exist and cannot be removed.")
            return False

        for j in range(0, len(self.hashmap[key_hash_code])):
            test = self.hashmap[key_hash_code]
            if test[j][0] == key:
                self.hashmap[key_hash_code].pop(j)
                #print("Key-Value Pair has been removed.")
                return True
        #print("Key-Value Pair has not been removed.")
        return False

    def get(self, key):
        if (key is None):
            raise ValueError("Cannot get a Key-Value Pair with a null value.")
        
        key_hash_code = self.generate_hash(key)
        if self.hashmap[key_hash_code] is not None:
            for kvpair in self.hashmap[key_hash_code]:
                if kvpair[0] == key:
                    return kvpair[1]
        return None
