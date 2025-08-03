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

        #Iterating through Numbers List to find the sum of Numbers
        if numbers:
            output = sum(int(n) for n in numbers.replace("\n", ",").split(delimiter)) 

        return output