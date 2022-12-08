#Python Project (CA-3)
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
count = 0
for i in range(start, end + 1):
    if isPrime(i):
        print("{} is a prime number".format(i))
        count = count + 1
    else:
        print("{} is a composite number".format(i))
print("There are {} prime numbers and {} composite numbers in the range".format(count, end - start + 1 - count))