class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if t[tp] == s[sp]:
                sp += 1
                tp += 1
            else:
                sp += 1
            
        if sp == len(s) and tp < len(t):
            return len(t) - tp
        else:
            return 0