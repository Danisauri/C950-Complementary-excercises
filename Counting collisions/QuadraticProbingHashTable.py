# class to represent an empty bucket
import sys


class EmptyBucket:
    pass


# Hashtable class definition using linear probing
class QuadraticProbingHashTable:

    # Constructor with optional initial capacity. All buckets are
    # assigned with an EmptyBucket() instance called self.EMPTY_SINCE_START.
    def __init__(self, initial_capacity=10, c1=0, c2=1):

        # Special constants to be used as the two types of empty buckets.
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        # Initialize all the table buckets to be EMPTY_SINCE_START.
        self.table = [self.EMPTY_SINCE_START] * initial_capacity

        self.c1 = c1
        self.c2 = c2

    # Inserts a new item into the hashtable.
    def insert(self, item):
        i = 0
        buckets_probed = 0
        collisions = 0

        # Hash function determines initial bucket
        number_of_buckets = len(self.table)
        bucket = ((hash(item)) % number_of_buckets)

        while buckets_probed < number_of_buckets:
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = item
                return True, collisions
            # increment i and recompute bucket index
            i += 1
            bucket = ((hash(item) + (self.c1 * i) + (self.c2 * i * i)) % number_of_buckets)

            # increment number of buckets probed
            buckets_probed += 1
            collisions += 1
        return False, collisions

    # Removes an item with a matching key from the hashtable.
    def remove(self, key):
        i = 0
        buckets_probed = 0
        number_of_buckets = len(self.table)
        bucket = hash(key) % number_of_buckets

        while (self.table[bucket] is not self.EMPTY_SINCE_START) and (buckets_probed < number_of_buckets):
            if (self.table[bucket] is not EmptyBucket) and (self.table[bucket] == key):
                self.table[bucket] = self.EMPTY_AFTER_REMOVAL
                return True
            # increment i and recompute bucket index
            # c1 and c2 are programmer-defined constants for quadratic probing
            i += 1
            bucket = (hash(key) + (self.c1 * i) + (self.c2 * i * i)) % number_of_buckets

            # increment number of buckets probed
            buckets_probed += 1
        return False

    # Searches for an item with a matching key in the hashtable. Returns the
    # item if found, or None if not found.
    def search(self, key):
        # TO-DO: implement the search() method using quadratic probing
        # when collisions occur. Return the item with a matching key if one
        # is found while probing.
        i = 0
        buckets_probed = 0

        # hash function determines initial bucket
        number_of_buckets = len(self.table)
        bucket = hash(key) % number_of_buckets

        while (self.table[bucket] is not self.EMPTY_SINCE_START) and (buckets_probed < number_of_buckets):
            if (self.table[bucket] is not EmptyBucket) and (self.table[bucket] == key):
                return self.table[bucket]

            # increment i and recompute bucket
            # c1 and c2 are programmer-defined constants for quadratic probing

            i += 1
            bucket = (hash(key) + (self.c1 * i) + (self.c2 * i * i)) % number_of_buckets

            # increment number of buckets probed
            buckets_probed += 1
        return None  # key not found

    # Overloaded string conversion method to create a string
    # representation of the entire hashtable. Special values
    # "E/S" and "E/R" are used to represent "EMPTY_SINCE_START"
    # and "EMPTY_AFTER_REMOVAL".
    def __str__(self):
        s = "   --------\n"
        index = 0
        for bucket in self.table:
            value = str(bucket)
            if bucket is self.EMPTY_SINCE_START:
                value = 'E/S'
            elif bucket is self.EMPTY_AFTER_REMOVAL:
                value = 'E/R'
            s += '{:2}:|{:^6}|\n'.format(index, value)
            index += 1
        s += "   --------"
        return s
