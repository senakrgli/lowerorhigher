import data
import random
bigData=data.data


clb1=random.choice(bigData)
bigData.remove(clb1)
clb2=random.choice(bigData)
score=0
game_over = False
while not game_over:
    print(clb1['name']+"-"+clb1['description'])
    print("vs")
    print(clb2['name']+"-"+clb2['description'])
    celebrity=input("Is first one more popular higher or lower?: (higher='y', lower='n') \n")
    if celebrity=='y':
        case1= clb1['follower_count']>clb2['follower_count']
        if case1==True:
            score+=1
            print("True choice.")
            clb1=clb2
            clb2 = random.choice(bigData)
            bigData.remove(clb2)
        else:
            game_over=True
            print(f"Game Over. Your score {score}")
    else:
        case2=clb1['follower_count'] < clb2['follower_count']
        if case2==True:
            score+=1
            print("True choice.")
            clb1=clb2
            clb2 = random.choice(bigData)
            bigData.remove(clb2)
        else:
            print(f"Game Over. Your score {score}")
            game_over=True


