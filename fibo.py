def recursive_nth_fibo(n):
    if n in (0,1):
        return 1
    else:
        return (recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2))




def main():
    fib = recursive_nth_fibo(8)
    print(fib)

if __name__ == '__main__':
    main()
