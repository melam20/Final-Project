race_list = ['Phoenix', 'phoenix', 'Fenrir', 'fenrir']
class_list = ['Warrior', 'warrior', 'Phantom', 'phantom']
number_list = [1, 2, 3, 4, 5, 6]
air_list = ['air', 'Air']
affirmative_list = ['yes', 'Yes']

import random

def name_input():
    """asks the user for their name"""
    
    print('Hi, what is your name?')
    name_given = input('INPUT :\t')

def character_create_race():
    """asks user for basic details about their character for the game"""
    
    print('Okay, can you tell me what kind of character' +
        ' that you would like to create? Please choose from the following:' + 
        ' Phoenix or Fenrir')
    
    character_race = input('INPUT :\t')
    
    check_race_input(character_race)
    
def character_create_class():    
    print('What class would you like your character to be? Please' +
        ' choose from the following: Warrior or Phantom')
    
    character_class = input('INPUT :\t')
                            
    check_class_input(character_class)
    
def check_race_input(character_race):
    """checks if the input matches any of the two races
    
    Parameters
    ----------
    input: string
    	string that is in the list of races

    Returns
    -------
    a message to please choose a valid input from the list of races
    if input does not match any
    """ 

    #will re-run the character race selection if the input is not valid
    if character_race not in race_list:
        print('Please choose a valid input.')
        character_create_race()
        
def check_class_input(character_class):
    """checks if the input matches any of the two races
    
    Parameters
    ----------
    input: string
    	string that is in the list of classes

    Returns
    -------
    a message to please choose a valid input from the list of classes
    if input does not match any
    """ 
    
    #will re-run the character class selection if the input is not valid
    if character_class not in class_list:
        print('Please choose a valid input.')
        character_create_class()
    else:
        print('Awesome. Your character is all set! Adventure time it is!')


#phoenix routes
def phoenix_route_warrior_1():
    """starts the first part of the phoenix + warrior route

	Parameters
	----------
	input: str
		either a 1 or a 2 will lead the user down the route, with different
		options

    """
    
    print('You live in a small village at the base of a dormant volcano. Your ' +
        'people have just overcome a minor raid from a nearby town.' +
        ' Many of your people have been injured. As one of the ' +
        'best fighters of your small group, you decide to: ' +
        '1 - recruit allies from other friendly villages or 2 - pursue your attackers.'
        + ' Please choose 1 or 2.')
    
    choice = input('INPUT :\t')
    
    phoenix_route_check_1(choice)
    
def phoenix_route_check_1(choice):
	"""the first check in the phoenix + warrior route

	Parameters
	----------
	input : string
		uses the input from the first step of the phoenix + warrior route to make a choice

	Returns
	-------
	new message for different routes. one leads to the luck combat route and the other
	is a peaceful route
	"""

	user_roll_type = ''
    
    #leads to route 2 directly for the first choice while the second option will put you 
    #into the luck combat and checks for valid input
	if choice == '1':
		print('With the intentions of possible recruiting some other warriors or ' +
            'even securing some medical help for your injured, you continue toward ' +
            'the friendly village Norusant. To avoid much detection by any potential threats, ' +
            'you carefully prowl through shadows and underbrush to conceal yourself.')
		phoenix_route_warrior_2()
	elif choice == '2':
		print('Uh oh. On your way to the attacking village, you encounter a few' +
            ' enemies fleeing your village. Type "roll" to see if you will be able' +
            ' defeat them!')
        
		user_roll_type = input('INPUT :\t')
        
		combat_roll()
	else:   
		print('Please choose a valid input.')
		phoenix_route_warrior_1()

def combat_roll():
	"""rolls a randomized dice by selecting a random number from list of integers 1-6"""

	rolled_number = random.choice(number_list)
    
    #continues on to the second route if you pass this trial with a random number
    #equal to or higher than 3
    #if you randomly roll a lower number then you are given the option to restart
	if rolled_number >= 3:
		print('Congratulations! You were able to defeat the enemy.')
		phoenix_route_warrior_2() 
	else:
		print('Oh no, how unlucky! You have been defeated. Game over! Would you like to play again?' +
            'Please answer "yes" or "no".')
        
		play_again = input('INPUT :\t')
		reset_play(play_again)
        
		return

def phoenix_route_warrior_2():
    """continues with the second part of phoenix + warrior route after part 1"""
    
    print('You continue your journey. As you finally finish meandering through an ashen forest,' +
        ' you come face-to-face with the Lava River, Irfiamma. Which option do you' +
        ' decide to take? 1 - Fly across or 2 - Use the obsidian brige')
    
    choice = input('INPUT :\t')
    
    phoenix_route_check_2(choice)
    
def phoenix_route_air_riddle():
    """the riddle for phoenix route check 2"""
    
    answer_given = input('INPUT :\t')
    
    if answer_given in air_list:
        print('That is correct! You are able to defeat the enemy and continue on to Norusant safely.')
        phoenix_route_3()
    else:
        print('Oh no! You did not get it right. Game over! Would you like to play again?' +
             ' Please answer "yes" or "no".')
        
        play_again = input('INPUT :\t')
        reset_play(play_again)
        
        return

def phoenix_route_check_2(choice):
	"""
	
	Parameters
	----------
	input : string, from the second step in the route to select a user route
		uses the input to move to the riddle route or branch into another route selection
	
	Returns
	-------
	a riddle or another branch route

	"""    

	#riddle with string input or branching route with number inputs
	#success leads to moving the route forward
	if choice == '1':
		print('You spread your wings and begin to fly across the river, only to have an incoming enemy!' +
            ' The other phoenix seems to have spotted you because you are in the air. Solve this riddle to ' +
            'see if you can outwit the enemy and defeat them or not!')
		print('I am lighter than a feather, but even the strongest person on Earth cannot hold me for more ' +
            'than a few minutes. What am I?')
		phoenix_route_air_riddle()
    
	elif choice == '2':
		print('While walking across the bridge, a stream of lava jumps alive and'
            ' takes the form of a dragon right in front of you!' +
            ' How will you handle this? 1 - Use fire magic to dispel the lava or' +
            ' 2 - dodge and fly away from the lava dragon.')
        
		choice = input('INPUT :\t')
        
		if choice == '1':
 			print('You channel the power of flames and are able to tame the lava ' +
                'so that you can cross the bridge safely.')
		else:
			print('You are able to dodge the lava successfully, and you fly ' +
                'across the river to the other side safely.')
            
		phoenix_route_4()
        
def phoenix_route_3():
    """ending path for the first option in route 2"""
    
    #uses user input to restart game or not
    print('You have finally made it to Norusant. What kind of gift did you bring to show your appreciation?')
    
    gift_brought = input('INPUT :\t')
    
    print('The phoenixes are pleased with your gift of ' + gift_brought + 
          ' and decide to aid you in your cause. You win!')

    print('Would you like to play again?')
    play_again = input('INPUT :\t')
    reset_play(play_again)
        
    return
    
def phoenix_route_4():
    """ending path for the second option in route 2"""
    
    #uses user input to restart the game or not
    print('You have finally made it to the village of your enemies, only to find that they are under' +
         ' attack by a coalition of your own allies. What will you do? Please type "fight" or "go home".')
    
    battle_choice = input('INPUT :\t')
    
    if battle_choice == 'fight':
        print('You have chosen to fight. The war may turn in your favor, but only time will tell...')
    elif battle_choice == 'go home':
        print('You choose not to engage in more fighting, to avoid putting your people at risk. Perhaps ' +
             'you may turn to negotiations for future matters. Only time will tell...')
    
    print('Would you like to play again?')
    play_again = input('INPUT :\t')
    reset_play(play_again)
        
    return

def reset_play(play_again):
    """checks if the user wants to play again or not"""
    
    if play_again in affirmative_list:
        run_adventure()
    else:
        return      
    
def run_adventure():
    """overall function to have the adventure happen"""
    
    #obtains user's name
    name_input()

    #obtains user's character's race
    character_create_race()

    #obtains user's character's class
    character_create_class()

    #starts the phoenix + warrior selection route
    phoenix_route_warrior_1()

