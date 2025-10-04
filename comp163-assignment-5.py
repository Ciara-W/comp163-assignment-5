print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number:"))
step_count = 0
print(" Sequence:", end=" ")
while current_number !=1:
    print(current_number, end=" ")
    if current_number % 2 == 0: #if number is divisible by 2 it gives an even number
        current_number = current_number // 2
    else:
        current_number = 3 * current_number + 1
    step_count += 1
print(current_number)
print("Steps:", step_count)

print("=== Challenge 2: Prime Number Checker ===")
n = int(input("Enter a number:"))
print(f" Testing divisors from 2 to {n-1}...")
is_prime = True
for i in range(2, n):
    if n % i == 0:#divides my code evenly
          print(f"{n} is not prime (divisible by {i})")
          is_prime = False
          break
if is_prime:
    print(f"{n} is prime!")

print("=== Challenge 3: Multiplication Table ===")

print("Multiplication Table:")
print("    1  2  3  4  5  6  7  8  9  10")
for row in range(1,11):
    print(f"{row:2}", end="")
    for column in range(1,11):
        product = row*column
        print(f"{product:4}", end="")
    print()