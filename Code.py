class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        r = n%k
        if r != 0:
            for i in range(k-r):
                s += fill
        t = []
        y = 0
        n = len(s)
        for x in range(k,n+1,k):
            print(x,y)
            y = x-k
            t.append(s[y:x])
        return t

            
