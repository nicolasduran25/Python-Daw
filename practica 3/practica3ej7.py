Day = int(input("introduzca el dia:"))
Month = int(input("introduzca el mes:"))
Year = int(input("introduzca el año:"))
if Day > 31  and Month == 1 or Year > 2019:
        print ("Error")
elif Day > 31  and Month == 3 or Year > 2019:
        print ("Error")
elif Day > 31  and Month == 5 or Year > 2019:
        print ("Error")
elif Day > 31  and Month == 7 or Year > 2019:
        print ("Error")
elif Day > 31  and Month == 8 or Year > 2019:
        print ("Error")
elif Day > 31  and Month == 10 or Year > 2019:
        print ("Error")
elif Day > 31  and Month == 12 or Year > 2019:
        print ("Error")        
elif Day < 1 or Month < 1:
        print ("Error")
elif Day > 30 and Month == 4 or Year > 2019:
        print ("error")
elif Day > 30 and Month == 6 or Year > 2019: 
        print ("error")        
elif Day > 30 and Month == 9 or Year > 2019:
        print ("error")
elif Day > 30 and Month == 11 or Year > 2019:
        print ("error")        
elif Day > 28 and Month == 2 or Year > 2019:
        print ("Error")
else:
        print (Day, "/",  Month, "/", Year)
        
