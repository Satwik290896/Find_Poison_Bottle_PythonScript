# Find_Poison_Bottle_PythonScript
The devil decides to send you 1000 bottles of wine, but one of them is poisoned. He also sent you 10 testing strips that can detect the poison. A single drop of poison will turn the test permanently positive. You can put any number of drops on a test strip at once, and you can re-use it until it comes in contact with the poison. Unfortunately, you can run a test once per day, and it takes 1 week to find out the result of the test. Write a code that finds the poisoned bottle in a minimal number of days
# Code Description

''' Use Divide and Conquer Algorithm. 
    In Week-1, Divide the set of 1000 Wine bottles into 10 Disjoint Sets such that 
    Set-1 contains First 100 Wine Bottles (0-99), Set-2 contains Second 100 Wine Bottles etc... and 
    Wine Bottles numbered 90 to 999 goes to Set-10 . 
    Test Each Set on one Stripe (One Drop from Each Wine Bottle)
    
    In Week-2, Identify the Stipe that tested positive for the previous week and Identify that
    our poison bottle present in the Set that is tested on this Stripe. Then Divide this identified
    set into 10 Disjoint Sets and repeat earlier procedure
    
    Eventually, with this Divide and Conquer Algorithm, we can reach to the poison bottle in minimum 
    number of weeks'''
    
# Output    

'''Console Output Sample'''
'''Found the Sample with Poison - Sample 871'''
'''Number of Weeks Required to find the Sample: 3 Weeks'''
