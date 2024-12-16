'''
Given two positive integers a and b, return the sum of the two integers without using the operators + and -.

'''

class adder:
        
    def add_without_plus_minus(self, a, b):
        while b!= 0:
            # XOR operation to calculate sum without carry
            sum_without_carry = a ^ b
            # AND operation followed by left shit to calculate carry
            carry = (a & b) << 1
            
            a = sum_without_carry
            b = carry
        
        return a
    
# Create an adder instance
adder = adder()
print(adder.add_without_plus_minus(2,3))
print(adder.add_without_plus_minus(0,3))

        
        
        
        