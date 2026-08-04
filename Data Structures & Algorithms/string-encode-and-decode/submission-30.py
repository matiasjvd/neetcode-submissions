class Solution:

    def encode(self, strs: list[str]) -> str:
        
        if not strs: return '-/-/'

        string = ''
        for s in strs[:-1]:
            
            string += s + '+/+/'

        string += strs[-1]

        return string

    def decode(self, s: str) -> list[str]:
        if s == '-/-/':
            return []
        lista = s.split('+/+/')
        return lista
