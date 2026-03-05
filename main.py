weight=float(input( "enter the weight = "))
height=float(input("enter the height = "))

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<25:
    print("normal weight")
else:
    print("overweight")
    

