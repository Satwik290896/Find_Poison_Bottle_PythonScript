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
    
'''Console Output Sample'''
'''Found the Sample with Poison - Sample 871'''
'''Number of Weeks Required to find the Sample: 3 Weeks'''

import numpy as np




''' This API helps us to know the result of the Test Stripe with Test_Stripe_Number with the drops used  on it'''
def test_positive_or_negative(Num_Wine_totest, start_Wine_totest, last_Wine_totest, Wine_Bottles, Test_Stripe_Number,Test_Stripes):
    Poison_Found = 0
    for i in range(start_Wine_totest,last_Wine_totest+1):
        if Wine_Bottles[i]==1:
            Poison_Found = 1
            Test_Stripes[Test_Stripe_Number] = 1
            break
    
    return Poison_Found, Test_Stripes


''' This API is used once for Each Week 
    - to test the Stripes by using Drops from respective wine bottles '''
def find_poison(Num_Wine_totest,start_Wine_totest,last_Wine_totest,Wine_Bottles,Num_Test_Stripes,Test_Stripes,Week_Count):
    
    if Num_Wine_totest == 1:
        print('Found the Sample with Poison - Sample %d' % start_Wine_totest)
        return Week_Count,Test_Stripes
    
    #Number of Stripes that can be used in this Week
    Stripes_tobeused = Num_Test_Stripes - sum(Test_Stripes)
    '''Batch determines how many Wine bottles(Drops, one Drop from each Wine Bottle) 
      will be present on one test stripe in this week'''
    Batch = (int) (Num_Wine_totest/Stripes_tobeused)
    #Indices that can be used
    test_indices = np.where(Test_Stripes == 0)[0] 
    # Count = used for iteration
    Count = 0
    
    #Increment Week to identify the Current Week
    Week_Count = Week_Count+1
        
    ''' If Batch is less than 1, this means Number of Bottles to be tested 
        is less than the number of available Stripes '''
    if Batch < 1:
        Stripes_tobeused = Num_Wine_totest
        Batch = 1
        
    while Count < Stripes_tobeused:
        if Count ==  Stripes_tobeused-1:
            start = start_Wine_totest + (Count)*Batch
            end = last_Wine_totest
            num = end - start + 1
        else:
            start = start_Wine_totest + (Count)*Batch
            end = start_Wine_totest + (Count)*Batch + Batch - 1
            num = end - start + 1
            
        Poison_Found, Test_Stripes = test_positive_or_negative(num,start,end,Wine_Bottles,test_indices[Count],Test_Stripes)
        Count = Count+1
        
        if Poison_Found == 1:
            break
    
    Week_Count,Test_Stripes = find_poison(num,start,end,Wine_Bottles,Num_Test_Stripes,Test_Stripes,Week_Count)
    
    return Week_Count,Test_Stripes
    

def main():
    Num_Wine = 1000
    Num_Test_Stripes = 10
    #Wine Bottles numbered as 0-999. Each Valued is valued - 0 if no poison, 1 if there is poison
    Wine_Bottles = np.zeros(Num_Wine)
    #Testing Stripes are numbered from 0-9 and Each Valued - 0  if no Poison is detected on it; 1 if detected 
    # Testing Stipes will not be used further if no poison is detected
    Test_Stripes = np.zeros(Num_Test_Stripes)
    Week_Count = 0  #Used to Count the Weeks till the Experiment ends 
    #Set 591 Bottle as containing Poison.
    Wine_Bottles[871] = 1  #Poison
    
    Week_Count, Test_Stripes = find_poison(Num_Wine,0,Num_Wine-1,Wine_Bottles,Num_Test_Stripes,Test_Stripes,Week_Count)
    
    print('Number of Weeks Required to find the Sample: %d Weeks' % Week_Count)
    

if __name__ == '__main__':
    main()




