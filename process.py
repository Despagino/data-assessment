log_file = open("um-server-01.txt")


# def sales_reports(log_file): #creating a function that passes in a parameter
#     for line in log_file: # looping over all the elements in the file
#         line = line.rstrip() # seperating all elements
#         day = line[0:3] # catching all elements from 0 - 3
#         if day == "Mon": # if the elements include "Tue"
#             print(line) # print line if day == Tue


# sales_reports(log_file)  # you run the function here

def melon_orders():
    for line in log_file:
        line = line.rstrip()
        res = line.split(",")
        print(res[])

melon_orders()