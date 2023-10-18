def generate_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j <= i:
                print(j, end='')
            else:
                print('*', end='')
        for k in range(i + 1, n + 1):
            print(k, end='')
        print()

# Contoh pemanggilan fungsi
generate_pattern(5)
print()
generate_pattern(4)
