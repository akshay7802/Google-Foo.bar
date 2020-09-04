
def solutions(data,n):
    if n==0:
        print("")
        return
    new_data=[]
    for num in data:
        if data.count(num)<=n:
            new_data.append(num)

    print(",").join(map(str,new_data))
