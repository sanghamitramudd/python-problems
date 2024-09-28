def hollow_triangle(n,m):
    for i in range(1, n ):
        for j in range(1, m):
            if (i == n-1 or i + j == n or j - i == m - n ) :
                print('*', end='')
            else:
                print(' ', end='')
        print()
        
n=5
m=8
print(hollow_triangle(n,m))