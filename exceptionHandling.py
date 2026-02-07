x = "10"
try:
    if(x>10):
        print("X is greater than 10")
    else:
        print("x is smaller than 10")
except Exception as e:
    print(f"This code is having an error - {e}")

finally:
    print("I will run irrespective of anything")

print("yes this is exception handling")