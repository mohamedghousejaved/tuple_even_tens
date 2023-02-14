tupl=()
n=int(input("enter the N value of integers"))
for i in range(n):
    inp=int(input("enter the elements of tuple"))
    tupl=tupl+(inp,)
print(tupl)


for j in range(0, len(tupl)):

    quotient = tupl[j] //10
    remainder=quotient%10
    if remainder % 2 == 0:

        print(tupl[j])