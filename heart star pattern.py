def heart_star_pattern(n):
    
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('*' * (2*i + 1))                         

    for i in range(2*n-1,0,-1):
        print(' ' * (2 * n - i -1), end='')
        print('*' * (2 * i - 1))
            
n=5
print(heart_star_pattern(n))