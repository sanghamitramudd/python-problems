def o_star_pattern(n,m):
    for i in range (n):
        for j in range(m):
            if ((j == 0 or j == m-1) and (i != 0 and i != n-1)) or ((i == 0 or i == n-1) and (j > 0 and j < m-1)):
                print("*", end="")
            else :
                print(" ", end="")
        print()
        
n = 4
m = 6

print(o_star_pattern(n,m))