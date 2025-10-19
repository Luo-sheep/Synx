def get_fibonacci(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib

# 调用并输出前 10 项
print("get_fibonacci(10):", get_fibonacci(10))