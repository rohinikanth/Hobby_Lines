Print this pattern
*      *
 *    * 
  *  *  
   **   
   **   
  *  *  
 *    * 
*      *

  def print_x_pattern(rows):
    for i in range(rows):
         for j in range(rows):
            if i == j or i + j == rows - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Input from user
rows = int(input("Enter number of rows: "))
print_x_pattern(rows)

