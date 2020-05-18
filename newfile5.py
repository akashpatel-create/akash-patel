run_ply1=int(input("enter runs by player 1 in 60 balls:"))
run_ply2=int(input("enter runs by player  2 in 60 balls:"))
run_ply3=int(input("enter runs by player 3 in 60 balls:"))
strikerate1=run_ply1*100/60
strikerate2=run_ply2*100/60
strikerate3=run_ply3*100/60
print("strikerate by player1=",strikerate1)
print("strikerate by player2=",strikerate2)
print("strikerate by player3=",strikerate3)
print("runs scored by player1 :",run_ply1*2)
print("runs scored by player2:",run_ply2*2)
print("runs scored by player3:",run_ply3*2)
print("max sixes by player1=",run_ply1//6)
print("max sixes by player2=",run_ply2//6)
print("max sixes by player3=",run_ply3//6)