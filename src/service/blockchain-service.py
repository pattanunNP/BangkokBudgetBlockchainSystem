import hashlib
import os

class Block:


    def __init__(self, previous_hash, transactions, timestamp):

        """
        Initailize the block object 
        """
        
        self.transations = transactions

        self.previous_hash = previous_hash

        self.timestamp = timestamp

     

    def get_hash(self):

        header_bin = (str(self.previous_hash) +
                      str(self.transations) +
                      str(self.timestamp)).encode()

        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

