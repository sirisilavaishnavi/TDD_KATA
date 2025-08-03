class StringCalculator():
    
    def add(self, numbers):

        output = None
        #Handling Empty Case
        if not numbers:
            output = 0

        #defining Standard delimiter
        delimiter = ","

        #handling Custom Delimiter
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)
            if len(delimiter) > 1:
                delimiter = delimiter.replace("[","").replace("]","")


        numbers = numbers.replace("\n", ",").split(delimiter)

        #Iterating through Numbers List to find the sum of Numbers and Negatives
        if numbers:
            negatives = []
            output = 0
            for n in numbers:
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