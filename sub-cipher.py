alpha = 'abcdefghijklmnopqrstuvwxyz'
lst = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]

result = ''
for i in range(len(lst)):
    print(lst[i], " : ", alpha[lst[i]])
    result += str(alpha[lst[i]-1])
        

print(result)