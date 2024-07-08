import random
from higher_lower_data import data
from art import logo


continue_game = True
final_score = 0 # counts user score

def compare():
 from replit import clear
 continue_game = True
 global final_score
 a = {}
 b = {}
 while continue_game:
    from art import logo_higher_lower
    print(logo_higher_lower)
    compare_a = random.choice(data) # generating a new compare
   
    #saves the values of compare_a as string in variable a
    for keys in compare_a :
      a = compare_a['name'] + ',' +compare_a['description'] + ',' + compare_a['country']  
    print(f"Compare_A : {a}")
    from art import vs
    print(vs)
    #saves the values of compare_b as string in variable b
    compare_b = random.choice(data)
    for keys in compare_b :
      b = compare_b['name'] + ',' +compare_b['description'] + ',' + compare_b['country']
    print(f"Compare_B : {b}")
    follower_a = int(compare_a['follower_count'])
    follower_b = int(compare_b['follower_count'])
    
    # print(follower_a)
    # print(follower_b)

    # comparing the follower_count and user guessed answer
    answer = input("Who has more followers A or B ?  :  ")
    if follower_a != follower_b :
      if (follower_a > follower_b and answer == "a") or (follower_b > follower_a and answer == "b"):
        final_score += 1
        clear()
        print(f"Correct!!, your final score is : {final_score}")

      else:

        clear()
        print(f"you lose and your final score is : {final_score}")
        continue_game  = False

    else: 
      return
      

compare()
