from re import sub


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallest = ""
        if (len(str1) > len(str2)):
            smallest = str2
            biggest = str1
        else:
            smallest = str1
            biggest = str2

        start = 0
        end = len(smallest)
        while(True):
            subsection = smallest[start:end+1]
            # print(subsection)
            state = True
            for i in range(0, end, end-start + 1):
                # print(biggest[i:i+end-start])
                if (biggest[i:i+end-start] != subsection):
                    state = False

            if (state == True):
                for i in range(0, end, end-start + 1):
                    print(smallest[i:i+end-start])
                    if (smallest[i:i+end-start] != subsection):
                        state = False
                if (state == True):
                    return subsection
                    
            start += 1
            if (start == end): return ""


def print_response(result: str, expected:str):
    assert result == expected, f"Got \"{result}\", expected \"{expected}\""

if __name__ == "__main__":
    s = Solution()
    print_response(s.gcdOfStrings("ABCABC", "ABC"),"ABC")
    print_response(s.gcdOfStrings("ABABAB", "ABAB"),"AB")
    print_response(s.gcdOfStrings("LEET", "CODE"),"")

 