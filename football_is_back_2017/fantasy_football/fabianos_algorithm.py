'''
Created on Aug 10, 2017
I'm just learning python, go easy on me!!!
This is my implementation of Fabiano's Algorithm, which consists
of displaying the top 5 players at each position. Someone, then drafts
a player and that player is removed from the list and the top-5 lists are
adjusted accordingly
@author: josephleovao
'''
# Player list objects to hold players
rb_player_list = []
wr_player_list = []
qb_player_list = []
te_player_list = []

class playa(object):
    def __init__(self,position,team,name,projection):
        self.position = position
        self.team = team
        self.name = name
        self.projection = projection
    def __repr__(self):
        return self.position + " " + self.name + "(" + self.team + "): " + str(self.projection)

def get_position(player):
    for i in range(len(rb_player_list)):
        if player == rb_player_list[i].name:
            return "RB"
    for i in range(len(wr_player_list)):
        if player == wr_player_list[i].name:
            return "WR"
    for i in range(len(qb_player_list)):
        if player == qb_player_list[i].name:
            return "QB"
    for i in range(len(te_player_list)):
        if player == te_player_list[i].name:
            return "TE"
    return ""

def delete_playa(player_to_delete, curr_position):
    # test delete value
    if curr_position == "TE":
        for i,o in enumerate(te_player_list):
            if o.name == player_to_delete:
                del te_player_list[i]
                break
    elif curr_position == "WR":
        for i,o in enumerate(wr_player_list):
            if o.name == player_to_delete:
                del wr_player_list[i]
                break
    elif curr_position == "RB":
        for i,o in enumerate(rb_player_list):
            if o.name == player_to_delete:
                del rb_player_list[i]
                break
    if curr_position == "QB":
        for i,o in enumerate(qb_player_list):
            if o.name == player_to_delete:
                del qb_player_list[i]
                break
# Read in rb_stats

with open("rb_stats.txt","r") as my_file:
    for line in my_file.readlines():
        word = line.split("\t")
        player = playa(word[0],word[1],word[2],word[3])
        rb_player_list.append(player)
    if not my_file.closed:
        my_file.close()

# Read in wr_stats

with open("wr_stats.txt","r") as my_file:
    for line in my_file.readlines():
        word = line.split("\t")
        player = playa(word[0],word[1],word[2],word[3])
        wr_player_list.append(player)
    if not my_file.closed:
        my_file.close()
        
# Read in qb_stats

with open("qb_stats.txt","r") as my_file:
    for line in my_file.readlines():
        word = line.split("\t")
        player = playa(word[0],word[1],word[2],word[3])
        qb_player_list.append(player)
    if not my_file.closed:
        my_file.close()

# Read in te_stats

with open("te_stats.txt","r") as my_file:
    for line in my_file.readlines():
        word = line.split("\t")
        player = playa(word[0],word[1],word[2],word[3])
        te_player_list.append(player)
    if not my_file.closed:
        my_file.close()
       
done = 'n'
option = 'n'

print "Welcome back Charlie, fantasy football is finally back and it's time to"
print "finally show everyone what we're made of. Last season's playoff loss hurt and it's"
print "time for some sweet revenge. So what do you say?"
print 
initialize = 'n'
while initialize != 'y' and initialize != "hell yeah":
    initialize = raw_input("You ready to get this party started (y / n / hell yeah)?")
    if initialize != 'y' and initialize != "hell yeah":
        print "Let's try this again."
if initialize == "hell yeah":
    print "\nHell yeah Charlie! That's the spirit!"
else:
    print "\nAll aboard the hype train!"
print "Welcome to the 2017 Charlie draft program. Let's dance!\n"

while(done != 'y'):
    print "* * * * * * * * * * * * * * * * * * *"
    option = raw_input("Is it your turn to select (y/n)? ")
    if option == 'y':
        print "Okay Charlie, based on players drafted so far, I, Fabiano,"
        print "suggest that you pick among these players:"
        print
    else:
        print "Hey Charlie, Fabiano here. Based on the draft so far, here's a list of the top 3 players"
        print "at each position(except K and DEF cuz who da hell cares about that?):"
    
    print "Top 5 RBs" 
    index = 1
    for person in rb_player_list:
        print "%s. %s" % (str(index),person) 
        if index == 5:
            break
        index += 1
    print "\nTop 5 WRs"  
    index = 1
    for person in wr_player_list:
        print "%s. %s" % (str(index),person) 
        if index == 5:
            break
        index += 1
       
    print "\nTop 5 QBs" 
    index = 1
    for person in qb_player_list:
        print "%s. %s" % (str(index),person) 
        if index == 5:
            break
        index += 1
    
    print "\nTop 5 TEs" 
    index = 1
    for person in te_player_list:
        print "%s. %s" % (str(index),person) 
        if index == 5:
            break
        index += 1
    
    if option == 'y':
        draft_selection = raw_input("Okay Charlie, who do you select for this round? ")
        selection_position = get_position(draft_selection)
        print "The 2017 Gnarly Charlies have selected %s %s" % (selection_position, draft_selection)
        delete_playa(draft_selection,selection_position)
        print
    else:
        their_selection = raw_input("Who does your opponent select? ")
        their_position = get_position(their_selection) 
        print "They have drafted %s %s" % (their_position,their_selection)
        delete_playa(their_selection,their_position)
        print
    done = raw_input("Exit draft (y/n)? ")
    if(done == 'y'):
        print "\nCongratulations on your selections and good luck this season!"
        print "I promise to not suggest Tony Romo to you anymore. Good luck Charlie!"
        break