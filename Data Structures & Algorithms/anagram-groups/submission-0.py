class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for i in word:
                count[ord(i) - ord("a")] += 1
            key = tuple(count)
            group[key].append(word)
        return list(group.values())