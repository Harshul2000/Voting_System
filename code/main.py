nominee1 = input("Enter the name of first nominee:")
nominee2 = input("Enter the name of second nominee:")

nm1_votes=0
nm2_votes=0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter=len(voter_id)

while True:
    if voter_id == []:
        print("Voting Has been concluded")
        if nm1_votes>nm2_votes:
            percent = (nm1_votes/no_of_voter)*100
            print(nominee1, "has won the election with",percent,"% of votes")
            break
        elif nm2_votes>nm1_votes:
            percent = (nm2_votes/no_of_voter)*100
            print(nominee2, "has won the election with",percent,"% of votes")
            break
        else:
            print("Both have equal number of votes")
            break
        

    voter = int(input("Enter your voter ID: "))
    if voter in voter_id:
        voter_id.remove(voter)
        print("To give vote to",nominee1, "press 1")
        print("To give vote to",nominee2, "press 2 ")
        vote = int(input("Cast your vote"))     
        if vote ==1:
            nm1_votes +=1
            print(nominee1,"Thanks for your support")
        elif vote ==2:
            nm2_votes +=1
            print(nominee2,"Thanks for your support")
        elif vote >2:
            print("Please check again")
        

