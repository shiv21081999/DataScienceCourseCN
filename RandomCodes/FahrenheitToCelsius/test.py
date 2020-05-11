start = int(input())
end = int(input())
step = int(input())
for i in range(start, end+1, step):
    c = int((i-32)*(5/9))
    print(str(i)+'\t'+str(c))