class ZAlgorithm:
    def __init__(self, txt: str, pat: str) -> None:
        self.txt = txt
        self.pat = pat
        self.string = pat + "$" + txt
        self.z_array = [0] * len(self.string)

    def compute_z_array(self):
        l, r = 0, 0
        for i in range(1, len(self.string)):
            # Either at the end of a z-box or within a z-box
            if i <= r:
                # Use previously computed Z-values
                '''
                
                self.z_array[i] = min(r - i + 1, self.z_array[i - l]), is used for indexes that 
                are already contained within a z-box. If self.z_array[i - l],  the length of the 
                substring within the current z-box is chosen as the min, it must mean that the 
                distance from the index to the end of the current z-box (r - i + 1) is greater than
                the substring, and therefore the substring is completely contained within the current
                z-box and we can just set the index z-value to be the z-value that we already computed.
                
                If the length to the end of the z-box is chosen as the min, it must mean that the previously 
                computed substring extends outside the current z-box, in which case we don't know if the text
                following the end of the current z-box will match, so we start doing explicit comparison again.
                
                So in summary: 
                
                r - i + 1 is min: The substring goes past the end of the current z-box, compare chars until
                    mismatch
                    
                self.z_array[i - l] is min: The substring is completely contained within the current
                    z-box and no new comparisons are needed
                
                '''
                self.z_array[i] = min(r - i + 1, self.z_array[i - l])
            
            '''
            
            This while loop ensures that we only compare with the string from the current index
            plus its current substring length to the end of the string, as soon as there is a 
            mismatch it will exit.
            
            Therefore if a substring is completely contained in a z-box the while loop will exit after
            1 comparison because we know the next character must be a mismatch
            
            If the substring reached the end of the current z-box, it will continue to match
            from that point until the next mismatch and update the z-value accordingly
            
            '''
            # Explicitly compare characters when needed
            while i + self.z_array[i] < len(self.string) and \
                    self.string[self.z_array[i]] == self.string[i + self.z_array[i]]:
                self.z_array[i] += 1
            # Update l and r if a new Z-box is found
            if i + self.z_array[i] - 1 > r:
                l = i
                r = i + self.z_array[i] - 1

    def get_matches(self):
        self.compute_z_array()
        matches = []
        for i in range(len(self.pat) + 1, len(self.string)):
            if self.z_array[i] == len(self.pat):
                matches.append(i - len(self.pat) - 1)
        return matches


if __name__ == "__main__":
    z = ZAlgorithm("aabcaxaabaabcy", "aab")
    print(f"The pattern was found in the string at indices: {z.get_matches()}")
