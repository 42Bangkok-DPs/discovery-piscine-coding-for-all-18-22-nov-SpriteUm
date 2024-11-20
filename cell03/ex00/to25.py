#!/usr/bin/env python3
input_num = int(input("Enter a number less than 25\n"))
if input_num > 25:
    print("Error")
else:
    for i in range(input_num,26):
        print(f"Inside the loop, my variable is {i}")