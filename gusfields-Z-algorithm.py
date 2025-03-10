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
                self.z_array[i] = min(r - i + 1, self.z_array[i - l])
        
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
