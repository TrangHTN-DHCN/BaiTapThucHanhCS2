lst = map(int, input().split())
k = int(input())

def isSumDigitEqualTok(x: int, k: int) -> bool:
    m = 0
    while x > 0:
        #print(x, end = ' ')
        m += x%10
        x //= 10
    return (m == k)

for x in lst:
    if isSumDigitEqualTok(x,k):
        print(x, end = ' ')