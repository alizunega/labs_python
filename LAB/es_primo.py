def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
           # print("No es primo", n, "es divisor")
            return False
    #print("Es primo")
    return True


for i in range(1, 100):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

