

class ZAlgorithm:
    
    def __init__(self, txt: str, pat: str):
        self.txt = txt
        self.pat = pat
        self.string = pat + '$' + txt
        
        print(self.string)
    
if __name__ == "__main__":
    print("hello")
    
    z = ZAlgorithm("aabcaabxaay", "aab")