pomo = 25 
rest = 5
mult_pomo = [25,50,75,100,125,150,175]
ideal = int(input("how many minutes do you want to work for?"))
total = (ideal/pomo*rest)+ideal
goal = ideal/pomo+rest
#clock = x/pomo+rest
mult_goal = [4,8,12,16,20]

#intro
print("goal:", ideal, "minutes and", ideal/60, "hours")
print( "total required time:", total, "minutes and", total/60, "hours.", goal, "is the minumum amount of rounds required.")

#conditionals(x == counter)
for x in total:
  if x == mult_pomo:
    print("time for a 5 minute break")
  #if clock == mult_goal:
    print("your breaks are now 30 minutes starting now")
