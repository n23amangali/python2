import time
number = int(input("Sample Input:\n"))
ms = int(input())
root = pow(number, 0.5) 
print("Sample Output:")
time.sleep(ms / 1000)
print("Square root of", number, "after", ms, "milliseconds", "is", root)