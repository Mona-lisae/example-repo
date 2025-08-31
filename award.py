swimming = float(input("Total time taken to complete swimming"  ))
cycling = float(input("Total time taken to complete swimming"  ))
running = float(input("Total time taken to complete swimming"  ))
Total_time_to_complete_the_triathlon = swimming + cycling + running 
print(Total_time_to_complete_the_triathlon)

if Total_time_to_complete_the_triathlon > 111:
    print("Sorry, No Award")
elif Total_time_to_complete_the_triathlon >105 and Total_time_to_complete_the_triathlon <=110:
    print("Well Done! You have received a PROVINCIAL SCROLL")
elif Total_time_to_complete_the_triathlon ==105 or Total_time_to_complete_the_triathlon >100:
    print("Well Done! You have received PROVINCIAL HALF COLOURS")
elif Total_time_to_complete_the_triathlon <=100:
    print("Congradulations! You have received PROVINCIAL COLOURS") 
    