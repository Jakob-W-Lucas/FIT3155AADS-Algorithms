

class ZAlgorithm:
    
    def __init__(self, txt: str, pat: str):
        self.txt = txt
        self.pat = pat
        self.string = "aabaabcaxaabaabcy"
        # Array stores a tuple for each character as [Z-length, left box, right box]
        self.z_array = [[0, 0, 0, [0, 0]] for _ in range(len(self.string))]
        
        self.l = -1
        self.r = -1
         
    def solve(self):
        
        for i in range(1, len(self.string)):
            self.get_z_box(i)
            n = i + 1
            print(f"Z{n} = {self.z_array[i][0]}, || \
                Z{n}-box = [{self.z_array[i][3][0]}..{self.z_array[i][3][1]}]\
                    (l{n}, r{n}) = ({self.z_array[i][1]}, {self.z_array[i][2]})")
        pass
    
    def get_z_box(self, k: int):
        
        if k > self.r:
            
            #print("Case 1")
            q = self.compare(k)
            
            if q - k > 0:
                self.l = k
                self.r = q - 1
            
            self.z_array[k] = [q - k, self.l, self.r, [k, q - 1]]
            
        elif k - self.l > 0 and \
            self.z_array[k - self.l + 1][0] < self.r - k + 1 and k <= self.r:
                
            #print("Case 2a")
            q = self.z_array[k - self.l][0]
            self.z_array[k] = [q, self.l, self.r, [k, k + q]]
            
        elif k - self.l > 0 and self.r + 1 != len(self.string) and \
            self.z_array[k - self.l + 1][0] >= self.r - k + 1 and k <= self.r:
                
            #print("Case 2b")
            q = self.compare(self.r + 1)
            self.z_array[k] = [q - k, self.l, q - 1, [k, k + q]]
            self.r = q - 1
    
    def compare(self, k: int) -> int:
        
        for q in range(len(self.string)):
            if self.string[q] != self.string[k + q]: 
               return k + q
    
if __name__ == "__main__":
    print("hello")
    
    z = ZAlgorithm("aabcaabxaay", "aab")
    z.solve()