class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        res = []

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in map:
                map[sorted_word] = [word]
            else:
                map[sorted_word].append(word)

        for values in map.values():
            res.append(values)

        return res