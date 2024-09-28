def x_star_pattern(n):
    #total number of rows and columns
    count = n * 2 - 1
    
    for i in range(1, count + 1):
        for j in range(1, count + 1):
            if j == i or j == count - i + 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
        
n = 5
print(x_star_pattern(n))