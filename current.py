class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map={}
        length=len(paths)
        for i in range(length):
            map[paths[i][0]]=paths[i][1]
        
        current_city=paths[0][0]
        
        while True:
            if current_city not in map:
                break
            current_city=map[current_city]
        return current_city
            
