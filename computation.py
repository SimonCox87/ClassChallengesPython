class Computation:
    def __init__(self, integer):
        self.integer = integer

    
    def factorial(self):
        fact = 1
        for i in range(1, self.integer +1):
            fact *= i
        return f'The factorial of {self.integer} is {fact}'

    
    def sum(self):
        sum = 0
        for i in range(1, self.integer + 1):
            sum += i
        return f'The sum of {self.integer} is {sum}'

    
    def testPrim(self):
        flag = False
        for i in range(2, (self.integer // 2) + 1):
            if self.integer % i == 0:
                flag = True
                break
        if flag:
            return f'{self.integer} is not a prime number'
        else:
            return f'{self.integer} is a prime number'
    
    
    def testPrimes(self, integerA, integerB): #do not invoke with the print function
        flag = False
        if integerA > integerB:
            integerA, integerB = integerB, integerA
        for i in range(integerA, integerB + 1):
            for j in range(2, (i // 2) + 1):
                if i % j == 0:
                    flag = True
                    break
            if flag:
                print(f'{i} is not a prime number')
                flag = False
            else:
                print(f'{i} is a prime number')
            flag = False

        
    def tableMult(self):
        multTab = ""
        for i in range(1, 13):
            multTab += str(i * self.integer) + ", "
        return f'This is the {self.integer} times table: {multTab.rstrip(", ")}'

    
    def allTablesMult(self):
        multTab = ""
        for i in range(1, 10):
            for j in range(1, 13):
                if j % 12 != 0:
                    multTab += str(i * j) + ", "
                else:
                    multTab += str(i * j) + "\n"
        return multTab.rstrip("\n")

    
    def listDiv(self):
        Ldiv = []
        for i in range(1, (self.integer // 2) + 1):
            if self.integer % i == 0:
                Ldiv.append(i)
        return f'This is a list of divisors of {self.integer}: {Ldiv}'
        
    
    def listDivPrime(self):
        primeLdiv = []
        flag = False
        for i in range(2, (self.integer // 2) + 1):
            if self.integer % i == 0:
                for j in range(2, (i // 2) + 1):
                    if i % j == 0:
                        flag = True
                        break
            if not flag:
                primeLdiv.append(i)
        return f'This is a list of prime divisors of {self.integer}: {primeLdiv}'


int = Computation(8)
int.testPrimes(2, 8)
print("\n")
print(int.factorial(), "\n")
print(int.sum(), "\n")
print(int.tableMult(), "\n")
print(int.allTablesMult(), "\n")
print(int.listDiv(), "\n")
print(int.listDivPrime())