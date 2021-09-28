import time
counts = 1000
timecount = counts
countdown = 1
times = 2
times2 = 10

while True:

    print (timecount)
    time.sleep(0.0001)
    timecount -= countdown
    
    countdier = 1000
        
    if timecount == 0:
        countdown *= times
        if countdown == 1:
            countdown += 1     
        timecount = 1000
    
    if timecount < 0:
        countdown *= times
        timecount = counts
        if countdown > countdier:
            countdier *= times2
            counts *= times2
           

    


        

        
            


    
    

