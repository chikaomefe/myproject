# Task 7.3
def largestsquare():
    largestsquarenum = 0
    
    num = int(input("Enter a number: "))
    
    for counter in range(num):
        if  largestsquarenum <= num:
            counter + counter + 1
        else:
            break
        largestsquarenum = counter * counter
            

    print(largestsquarenum)
            
        
    

largestsquare()