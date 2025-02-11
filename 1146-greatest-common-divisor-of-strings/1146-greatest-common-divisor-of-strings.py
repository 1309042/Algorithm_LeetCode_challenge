class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 == str2 + str1:
            for i in range(len(str2), 0, -1):
                if len(str1) % i == 0 and len(str2) % i == 0:
                    if str1.replace(str1[:i], "") == "" and str2.replace(str1[:i], "") == "":
                        return str1[:i] 
        return ""
