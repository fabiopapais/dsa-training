"""
First intuition
- native str() and eval() -> too simple

First usable intuition
- Use a separator
- If the separator already exists, escape it
- If the escape char existis, escape it again

Another useful solution
Encode each word with the word + delimiter + lenght 

"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        
        encoded = str(len(strs[0]))
        
        for s in strs[1:]:
            encoded += "," + str(len(s))
        
        encoded += "#"

        for s in strs:
            encoded += s
    
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        hashtag_index = 0
        for i in range(len(s)):
            if s[i] == "#":
                hashtag_index = i
                break
        sizes = s[:hashtag_index].split(',')
        words = s[hashtag_index + 1:]

        decoded = []
        current_i = 0
        for size in sizes:
            if size == '0':
                decoded.append("")
            else:
                decoded.append(words[current_i:current_i + int(size)])
                current_i += int(size)

        return decoded
