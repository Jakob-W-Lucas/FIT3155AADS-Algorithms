

class ZAlgorithm:
    
    def __init__(self, txt: str, pat: str):
        self.txt = txt
        self.pat = pat
        self.string = pat + '$' + txt
        self.start = len(pat) + 2
        # Array stores a tuple for each character as [Z-length, right box, left box]
        self.z_array = [[0, 0, 0] for _ in range(len(txt))]
        
    def solve(self):
        
        for i in range(self.start, len(self.string)):
            self.get_z_box(i)
            print(self.z_array[i - self.start])
        pass
    
    def get_z_box(self, index: int) -> tuple[int, int, int]:
        
        count = 0
        n = index - self.start + 1
        self.z_array[n][1] = n
        for i in range(len(self.string)):
            if self.string[n + i] != self.string[index]:
                break
            count += 1
            self.z_array[n + i][2] = n + i
        
        self.z_array[n][0] = count
    
if __name__ == "__main__":
    print("hello")
    
    z = ZAlgorithm("aabcaabxaay", "aab")
    z.solve()