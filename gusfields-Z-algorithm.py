

class ZAlgorithm:
    
    def __init__(self, txt: str, pat: str) -> None:
        self.txt = txt
        self.pat = pat
        self.string = pat + "$" + txt
        # Array stores a tuple for each character as [Z-length, left box, right box]
        self.z_array = [[0, 0, 0, [0, 0]] for _ in range(len(self.string))]
        
        self.l = -1
        self.r = -1

    def get_matches(self) -> list:
        matches = []
        for i in range(1, len(self.string)):
            
            self.get_z_box(i)
            
            if self.z_array[i][0] == len(self.pat):
                matches.append(i - len(self.pat) - 1)
        
        if len(matches) == 0:
            print(f"There were no matches found.")
            
        return matches
    
    def get_z_box(self, k: int):
        
        # Case 1
        if k > self.r:
            
            # Compute Zk by explicitly comparing characters str[k . . . q − 1] with str[1 . . . q − k] 
            # until a mismatch is found at some q ≥ k.
            q = self.compare(k)
            Zk = q - k
            
            # If Zk == 0 then there is no need to update l and r and they retain the same values as before.
            if Zk > 0:
                self.r = q - 1
                self.l = k
            
            self.z_array[k] = [Zk, self.l, self.r, [k, q - 1]]
        
        # In these cases k is inside the right-most Z-box
        
        # Case 2a: If Zk−l < r − k + 1 (and k ≤ r)
        elif k - self.l > 0 and \
            self.z_array[k - self.l][0] < self.r - k + 1 and k <= self.r:
            
            # Set Zk to Zk−l
            Zk = self.z_array[k - self.l][0]
            
            # r and l remain unchanged
            self.z_array[k] = [Zk, self.l, self.r, [k, Zk + k - 1]]
        
        # Case 2b: If Zk−l ≥ r − k + 1 (and k ≤ r)
        # (Zk must also be ≥ r − k + 1)
        elif k - self.l > 0 and self.r + 1 != len(self.string) and \
            self.z_array[k - self.l][0] >= self.r - k + 1 and k <= self.r:
            
            # Start explicitly comparing str[r + 1] with str[r − k + 2] and so on until mismatch occurs
            q = self.compare(self.r + 1)
            Zk = q - k
            
            # set Zk to q − k, set r to q - 1, and set l to k
            self.z_array[k] = [Zk, self.l, q - 1, [k, q]]
            self.r = q - 1
        
        else:
            print("Something has gone wrong.")
    
    # Returns the location in the string array where the matching fails
    def compare(self, k: int) -> int:
        
        q = k
        # Comparing to str[1...q - k]
        for n in range(len(self.string) - k):
            # Compare to find str[k...q-1]
            if self.string[n] == self.string[k + n]: 
                q += 1
            else:
                break
        return q
    
if __name__ == "__main__":
    
    z = ZAlgorithm("aabcaxaabaabcy", "aab")
    print(f"The pattern was found in the string at i = {z.get_matches()}")