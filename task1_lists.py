#enter numbers
x = int(input())
y = int( input())

#function for receiving lists
def lists_creator(x, y):
    p = [i for i in range(1, x*y + 1)]#create a sequence of numbers
    return (([p[i: i + y] for i in range(0, len(p), y) ])) #cut sequence to lists

print (lists_creator(x,y))#output
