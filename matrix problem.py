# getting info about rows and columns
m = int(input("enter row  "))
n =  int(input("enter column "))


# initialise matrix 
matrix = [[0]* n for  p in range (m)]


# asking prices for each point 
for i in range (m):
    for j in range(n):
        matrix[i][j] = int(input(f"enter the cost from point {i} to point {j}:  "))


# get input for start and end point

current = int(input("Enter your current location (0,1,2): "))
destination = int(input("Enter your destination (0,1,2):  "))

# calculate cost
cost = matrix[current][destination]
print(f"the cost of travelling from  point{current} to point {destination} is {cost}")


