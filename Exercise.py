def find_factorial(num):
    if num <= 0:
        pass
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact


print("Prime numbers between 1 to 100")
for i in range(2, 100):
    b = True
    for j in range(2, i // 2+1):
        if i % j == 0:
            b = False
            break
    if b:
        print(i)

# Implement a Python program that asks the user to enter a password. If the password matches a predefined secret
# password, display a success message. Otherwise, display an error message using an if/else ternary expression.
password = "asdf2021"
user_password = "asdf2021"
if password == user_password:
    print("Login succeeded")
else:
    print("Wrong password")


def print_pattern(n):
    k = 1
    while k <= n:
        q = 1
        while q <= k:
            print(q, end=' ')
            q += 1
        k += 1
        print()


def find_common_elements(list1, list2):
    new_ls = []
    for element in list1:
        if element in list2:
            new_ls.append(element)
    return new_ls


def find_prime_factors(num):
    prime_factors = []
    fact = 2
    while fact <= num:
        if num % fact == 0:
            num = num // fact
            if fact not in prime_factors:
                prime_factors.append(fact)
        else:
            fact += 1

    return prime_factors


print("Factorial: ", find_factorial(5))
print(print_pattern(8))
ls1 = [1, 2, 3, 8, 7]
ls2 = [1, 5, 6, 4, 3, 9, 8, 7]
print(find_common_elements(ls1, ls2))
print(find_prime_factors(84))