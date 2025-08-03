import re

class StringCalculator():
    
    def add(self, numbers):

        output = None
        #Handling Empty Case
        if not numbers:
            output = 0

        #defining Standard delimiter
        delimiters = [",", "\n"]

        #handling Custom Delimiter
        if numbers.startswith("//"):

            delimiter_section, numbers = numbers.split("\n", 1)
            custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_section)
            if custom_delimiters:
                delimiters = custom_delimiters
            else:
                delimiters = [delimiter_section[2:]]

        pattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(pattern, numbers)

        # numbers = numbers.replace("\n", ",").split(delimiter)

        #Iterating through Numbers List to find the sum of Numbers and Negatives
        if numbers:
            negatives = []
            output = 0
            for n in tokens:
                if n:
                    n = int(n)
                    if n < 0:
                        negatives.append(n)
                    # handling change in inputs
                    elif n < 1001:
                        output += n

            # negatives = [int(n) for n in numbers if n and int(n) < 0]
            if negatives:
                raise ValueError(f"Negative numbers not allowed: {','.join(map(str, negatives))}")
            
            # output = sum(int(n) for n in numbers if n and int(n) >0)

        return output