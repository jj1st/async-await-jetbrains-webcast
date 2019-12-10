from typing import List


# def fib(n: int) -> List[int]:
#     numbers = []
#     t1, t2 = 0, 1
#     while len(numbers) < n:
#         t1, t2 = t2, t1 + t2
#         numbers.append(t1)
#
#     return numbers


def fib():
    t1, t2 = 0, 1
    while True:
        t1, t2 = t2, t1 + t2
        yield t1


result = fib()

for n in result:
    if n > 10000:
        print(n)
        break
    else:
        print(n, end=', ')

print("\nDone")
