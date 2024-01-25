def generate_fibonacci(n):
    fibSeq=[0,1]
    for i in range(2,n):
        nextTerm=fibSeq[-1]+fibSeq[-2]
        fibSeq.append(nextTerm)
    return fibSeq


n=int(input("Enter the number of terms for Fibonacci Series: "))
print(generate_fibonacci(n))
