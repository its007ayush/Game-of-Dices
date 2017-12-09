def sample_space(dice1, dice2):
    ss = []
    for i in dice1:
        for j in dice2:
            ss.append([i,j])
    return ss

##################################################################################

def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    
    ss = sample_space(dice1, dice2)
    
    for i in ss:
      if i[0] > i[1]:
        dice1_wins +=1
        
      elif i[0] < i[1]:
        dice2_wins +=1
    
    return (dice1_wins, dice2_wins)

####################################################################################

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    best_dice = 0
    
    jump=0
    for i in range(0, len(dices)):
      for j in range(0, len(dices)):
        if i!=j:
          count = count_wins(dices[i],dices[j])
          print(i,end=" ")
          print(j,end=" ")
          print(count)
          
          if count[0] > count[1]:
            if j==len(dices)-1:
              return best_dice
              
            if best_dice <= i:
              best_dice = i
              print("A")
            else:
              print("B")
              return -1
              
          elif count[0]<count[1]:
            print("C")
            if best_dice <= j:
              best_dice =j
              i=j-1
              break
            else:
              return -1
            
    return best_dice
   

#####################################################################################

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
        
    bd = find_the_best_dice(dices)
    if bd != -1:
      strategy["first_dice"]= bd
    
    else:
       strategy["choose_first"] = False
       
       for i in range(0, len(dices)):
          for j in range(0, len(dices)):
            if i!=j:
              count = count_wins(dices[i],dices[j])
              if count[0] > count[1]:
                strategy[j] = i 
                
              else:
                strategy[i] = j
    return strategy          
              
    
#####################################################################################

print(compute_strategy( [[1,1,6,6,8,8], [2,2,4,4,9,9], [3,3,5,5,7,7]]))

