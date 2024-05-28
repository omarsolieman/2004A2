class OrfFinder:
    def __init__(self, genome):
        self.genome = genome
        self.suffix_array = self._build_suffix_array(genome)
    
    def _build_suffix_array(self, genome):
        suffixes = [(genome[i:], i) for i in range(len(genome))]
        suffixes.sort()
        return [suffix[1] for suffix in suffixes]
    
    def _find_occurrences(self, pattern):
        occurrences = []
        left, right = 0, len(self.suffix_array) - 1
        while left <= right:
            mid = (left + right) // 2
            suffix = self.genome[self.suffix_array[mid]:]
            if suffix.startswith(pattern):
                occurrences.append(self.suffix_array[mid])
                left = mid + 1
            elif pattern < suffix:
                right = mid - 1
            else:
                left = mid + 1
        return occurrences
    
    def find(self, start, end):
        start_occurrences = self._find_occurrences(start)
        end_occurrences = self._find_occurrences(end)
        substrings = []
        for i in start_occurrences:
            for j in end_occurrences:
                substring = self.genome[i:j+len(end)]
                if i <= j and substring.startswith(start) and substring.endswith(end) and substring not in substrings:
                    substrings.append(substring)
        substrings.sort(key=lambda x: (len(x), x))
        return substrings

genome1 = OrfFinder("AAABBBCCC")
print(genome1.find("AAA", "BB"))  # Output: ['AAABB', 'AAABBB']
print(genome1.find("BB", "A"))    # Output: []
print(genome1.find("AA", "BC"))   # Output: ['AABBBC', 'AAABBBC']
print(genome1.find("A", "B"))     # Output: ['AAAB', 'AAABB', 'AAABBB', 'AAB', 'AABB', 'AABBB', 'AB', 'ABB', 'ABBB']
print(genome1.find("AA", "A"))    # Output: ['AAA']
print(genome1.find("AAAB", "BBB"))  # Output: []

genome2 = OrfFinder("ATGCATGCATGC")
print(genome2.find("ATG", "TGC"))  # Output: ['ATGCATGC', 'ATGCATGCATGC']
print(genome2.find("CAT", "ATG"))  # Output: ['CATGCATG']
print(genome2.find("A", "A"))      # Output: ['ATGCA', 'ATGCATGCA']
print(genome2.find("AT", "AT"))    # Output: []
print(genome2.find("TGC", "ATG"))  # Output: ['TGCATG']

genome3 = OrfFinder("AAAAAA")
print(genome3.find("AAA", "AAA"))  # Output: ['AAAAAA']
print(genome3.find("A", "A"))      # Output: ['AA', 'AAA', 'AAAA', 'AAAAA', 'AAAAAA']
print(genome3.find("AAAA", "AA"))  # Output: ['AAAAAA']

genome4 = OrfFinder("ATCGATCG")
print(genome4.find("AT", "CG"))    # Output: ['ATCG', 'ATCGATCG']
print(genome4.find("ATC", "TCG"))  # Output: ['ATCGATCG']
print(genome4.find("C", "C"))      # Output: ['CG', 'CGATC']
print(genome4.find("AT", "AT"))    # Output: []
print(genome4.find("ATCG", "TCG"))  # Output: ['ATCGATCG']