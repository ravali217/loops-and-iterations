# 1.Create .
# 2.Use for loop to print numbers 1–100.
# 3.Use while loop for countdown timer.
# 4.Implement break and continue.
# 5.Iterate over string characters.
# 6.Generate multiplication table.
# 7.Use range with steps.
# 8.Combine loop with conditions.
# 9.Add real-world examples.

for i in range(1,101):
    print(i)

i=10
while(i>0):
    print(i)
    i=i-1

print("===")
for i in range(1,10):
    
    if i==5:
        break
    print(i)

for i in range(1,10):
    
    if i==6:
        continue
    print(i)
name="ravali"
for i in name:
    print(i,end=" ")
print("\n")

for i  in range(1,11):
    a=5*i
    print(a)

for i in range(0,21,2):
    print(i)
for i in range(1,21):
    if i%2==0:
        print(i," is even")
    else:
        print(i, "is odd")
    