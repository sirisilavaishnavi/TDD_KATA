class StringCalculator():
    
    def add(self, numbers):

        output = None
        if not numbers:
            output = 0
        
        if numbers:
            output = sum(int(n) for n in numbers.replace("\n", ",").split(',')) 

        return output