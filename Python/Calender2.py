import datetime

Month = int(input("Enter month (1-12): "))
Year = int(input("Enter year: "))

days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

firstDay=datetime.date(Year,Month,1)
startDay=firstDay.weekday()

if Month == 12:
    Next_month = datetime.date(Year+1,1,1)
else:
    Next_month = datetime.date(Year,Month+1,1)

x = Next_month - firstDay
y = x.days

print("  ".join([f"{day:^4}" for day in days]))

print(" " * 6 * startDay, end="")

for day in range(1, y + 1):
    print(f"{day:^3} ", end="  ")
    if (startDay + day) % 7 == 0:
        print()

print()

"""
Sample1:
Enter month (1-12): 6
Enter year: 2025
Mon   Tue   Wed   Thu   Fri   Sat   Sun 
                                     1    
 2     3     4     5     6     7     8    
 9    10    11    12    13    14    15    
16    17    18    19    20    21    22    
23    24    25    26    27    28    29    
30  

Sample2:
Enter year: 2025
Mon   Tue   Wed   Thu   Fri   Sat   Sun 
                   1     2     3     4    
 5     6     7     8     9    10    11    
12    13    14    15    16    17    18    
19    20    21    22    23    24    25    
26    27    28    29    30    31 

Sample3:
Enter month (1-12): 4
Enter year: 2025
Mon   Tue   Wed   Thu   Fri   Sat   Sun 
       1     2     3     4     5     6    
 7     8     9    10    11    12    13    
14    15    16    17    18    19    20    
21    22    23    24    25    26    27    
28    29    30   
"""