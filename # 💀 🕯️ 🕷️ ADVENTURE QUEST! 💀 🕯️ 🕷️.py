# 💀 🕯️ 🕷️ ADVENTURE QUEST! 💀 🕯️ 🕷️

#Special Thing: There are three characters that you can interact with: Mrs. Menteuse, Little Boy, and Housekeeper
#You can get a key from the Housekeeper when you give the Decanter to her and you can get the Decoder from the Little Boy when you give him the toy soldier (which you also have to name)

#Sample Use Item Comment:
#north
#up
#south
#take Bedknob
#north
#east
#south
#use Bedknob

import sys

character = {'inventory': [],
             'location': 'Frontage',
             'universal': 'on'}

mansion = {
    'Frontage': {
        'name': 'Frontage',

        'description': '\nYou find yourself standing on a disarmingly mundane street. Houses to the left and right of the one before you blend into a mass of dark brick colored, windowed monotony. Those houses, you know, contain wives and husbands and children - families. You feel almost sorry for the family in the house before you; they have reported a missing person - a husband and father. The two-storied building before you looks like every other house on the cobbled road, but not.... There is something foreboding about it, like a dark cloud hangs over the cheery building with bright flowers boxed in the front. Maybe this is due to the recent loss of the master of the house. With a sigh, you know there is only thing for you to do as the inspector sent by Scotland Yard: enter the house and begin your investigation.\n\n[type "help" to get list of commands]\n',

        'contents': {
          'Objects': {
            'name': "There is nothing for you to take here.",
            'room to use': 'You cannot use that item in this area.',
            'description':'N/A',
            'use checker':'false'
          }
        },

        'parler': {
          "name":"There is no one to talk to in this area."
        },

        'exits': {'north': 'Front Hall'}
    },

    'Front Hall': {
        'name': 'Front Hall',

        'description': '\nBefore you lays a narrow room, more like a hall, with a staircase to the left that leads up to some undefined second story. The floors are a dark lacquered wood laid over by richly colored oriental rugs. The walls are covered in a dark olive green wallpaper. There is a gap in the right wall that seems to lead to some furnished room. Beyond the staircase, you believe you can see an open door that if closed would blend into the woodwork.\n',

        'contents': {
          'Objects':{
            'name':"There is nothing for you to take here.",
            'room to use': 'You cannot use that item in this area.',
            'description': 'N/A',
            'use checker':'false'
          }
        },

        'parler': {
          "name":"There is no one to talk to in this area."
        },

        'exits': {'north': 'Kitchen',
                  'east': 'Parlor',
                  'south': 'Frontage',
                  'up' : 'Landing'}
    },

    'Kitchen': {
        'name': 'Kitchen',

        'description': '\nYou come into a kitchen. The first thing you notice is the strong smell of fish. Trying to find the source of the smell, your gaze dances across free standing, wooden cabinets, a black wood burning oven, hooks from which iron pots and pans hang, and what appears to be a stairwell in the corner. Finally, your eyes settle on the work table situated in the middle of the room. On it appears to be a recently gutted fish. A rough cough draws your attention to a weathered middle-aged woman in the corner whose uniform notifies you that she must be the housekeeper. Her face appears to be permanently set in a scowl as her eyes run over you. You shiver, not sure whether to talk to her or not.\n',

        'contents': {
          'Objects': {
              'name': 'Fish',
              'type': 'object',
              'description': '\nIt is a fish that appears to be of the genus Clupea harengus and seems to be have been gutted recently as it is very bloody.\n',
              'room to use': 'Kitchen',
              'action': '\nWhat are you going to do with a fish? It is obviously a red herring.\n',
              'use checker':'false'
            }
        },

        'parler': {
          "name":"Housekeeper"
        },

        'exits': {'south': 'Front Hall',
                  'up' : "Housekeeper's Quarters" }
    },

    'Parlor': {
        'name': 'Parlor',

        'description': '\nYou come into a parlor. The room is much warmer than the rest of the house, which could be accredited to the large fireplace on the wall adjacent. Along the fireplace mantel sits an ornate clock framed by two mallard duck statuettes. Various low-lying couches and plush velvet chairs dot the room. It is on one of the couches that you see who must be the lady of the house in her expensive layered dress. Her eyes are slightly red-rimmed, suggesting that she may have been crying at some point, but her dignified position gives her an air of strength. On the wall opposite you, two large glass doors lead out into a beautiful garden.\n',

        'contents': { 
          'Objects': {
            'name':'There is nothing for you to take here.',
            'room to use': 'You cannot use that item in this area',
            'description': 'N/A',
            'use checker':'false'
          }
        },

        'parler': {
          "name":"Mrs. Menteuse"
        },

        'exits': {'west': 'Front Hall',
                  'east' : 'Garden',
                  }
    },

    'Garden': {
        'name': 'Garden',

        'description': '\nThe garden is hedged in with tall, foreboding greenery. Ceramic pots hold brightly colored flowers, similar to those in the front of the house. Morning glory blooms from trellises leaning against the back of the house. Partially hidden by one of the flower pots is a bottle of clear liquid. In the corner of the garden, you see a small boy holding a circular device that has a magnifying glass in the middle. The young child seems to be leaning over a mound of dirt - an ant hill, you realize. He is angling the glass to burn the ants to death. The boy laughs maniacally as he kills another and you shudder slightly at the haunting sound.\n',

        'contents': {

          'Objects': {
            'name': 'Bottle',
            'type': 'Object',
            'description': '\nThe rectangular bottle holds clear liquid. The liquid gives off no scent but has a resemblance to strong, clear alcohol.\n',
            'room to use': 'Kitchen',
            'action': '\nYou give the rectangular bottle to the Housekeeper. She holds it up to the dim light that comes through the singular, grimey window. She sniffs with disdain and glares at you. "Why did you bring me a bottle of weed killer?" You flush with embarrassment, realizing your mistake, before shuffling off.\n',
            'use checker':'false'
          }
          
        },

        'parler': {
          "name":"Little Boy"
        },

        'exits': {'west': 'Parlor'}
    },

    'Landing': {
        'name': 'Landing',

        'description': '\nYou come onto a landing. The walls and floor match the rich, dark colors of the Front Hall. A plush, dark red carpet runs the length of the hall with a couple of small runner tables pushed up against the walls. You think you can see something peeking out behind one of these tables. To the south, there appears to be an open door leading to some small dark room, maybe the quarters of a servant or something. To the west, there is an open door that looks to lead to some sort of bedroom. Straight ahead, there seems to be an open door leading to, from what you can see, a room with many books - maybe a study. To the east there is another open door that leads to what appears to be a room with colorful toys and a childish ambience. Maybe it is a Nursery?\n',

        'contents': {

          'Objects': {
           'name': 'Soldier',
           'description': '\nThe toy soldier is a stiff standing figurine. Garbed in a red uniform with a black helmet resting on his head, his face is set in a stern expression, almost bordering on constipated. You wonder what his name is.\n',
           'room to use': 'Garden',
           'action': '\nYou give the Toy Soldier to the young boy. He smiles genuinely for the first time as he holds the toy. However, the smile is almost instantly replaced with a sneer. "Now! What is his name?"\n',
           'use checker':'false'
          
          }
        },

        'parler': {
          "name":"There is no one to talk to in this area."
        },

        'exits': {'down' : 'Front Hall',
                  'east': 'Nursery',
                  'north' : 'Study',
                  'west' : 'Master Bedroom',
                  'south': "Housekeeper's Quarters"}
    },

    'Water Closet': {
        'name': 'Water Closet',

        'description': '\nThe water closet is a small room. There appears to be a claw-footed bathtub in the corner with a bulky tap attached to it. The tap does not look quite right, however. You realize that it is missing the handle to turn it on. There is a free screw where the handle can be attached, but nothing to use. In the corner there is a toilet with a dangling chain with which to flush. On the opposite wall, you see a basin with a mirror bolted to the wall above. It looks like something is slightly smeared on the mirror, but you are not quite sure. If you could find a way to mist the mirror, you may be able to see the smearing more clearly.\n',

        'contents': {
          'Objects':{
            'name':'There is nothing for you to take here.',
            'room to use': 'You cannot use that item in this area.',
            'description':'N/A',
            'use checker':'false'
          }
        },

        'parler': {
          "name":"There is no one to talk to in this area."
        },

        'exits': {'north': 'Nursery'}
    },

    'Study': {
        'name': 'Study',

        'description': '\nA room full of books greets you in the study. The walls are lined with shelves and shelves of books, many leather bound and more than a little dusty. You get the feeling that the books are more for show than actual use, however you cannot help but admire them. In the center of the room lies a desk. On the desk there sits a decanter of some amber liquid - maybe a drink of some kind?\n',

        'contents': {
          'Objects': {
           'name': 'Decanter',
           'description': '\nThe decanter is a crystalline container that contains some rich amber liquid. Taking a whiff, you catch the strong scent of fine whiskey.\n',
           'room to use': 'Kitchen',
           'action': '\nYou give the decanter to the housekeeper. Her gnarled hands wrap around the decanter and her eyes take on a half-crazed, half-greedy look. She hands you a key without saying a word, her focus entirely on the whiskey in her hands.\n',
           'use checker':'false'
          }
        },

        'parler': {
          "name":"There is no one to talk to in this area."
        },

        'exits': {'south': 'Landing'}
    },

    'Master Bedroom': {
        'name': 'Master Bedroom',

        'description': '\nThe Master bedroom is one of the biggest rooms on the second floor. Rich carpets cover the floor and a giant four poster bed with drapery sits in the middle of the room. Dark green covers are tucked firmly, almost aggressively, under the mattress. You see what appears to be a box tucked underneath the bed. You wonder what the wooden box may contain.\n',

        'contents': {
          'Objects': {
           'name': 'Chest',
           'description': '\nThe chest is rectangular, not very large, but not overly small either. It is made of a light colored wood and there is an iron keyhole at the front.\n',
           'room to use': 'You cannot use that item in this area.',
           'action': '\nYou take the skeleton key and put it into the keyhole on the chest. Turning it slowly, you can hear the pins inside of the lock shifting around. There is a very audible click and you are able to open the box. Discarding the chest and key to the side, you look into it and see a piece of folded up paper.\n',
           'use checker':'false'
          }  
        },

        'parler': {
          "name":"There is no one to talk to in this area."
        },

        'exits': {'east': 'Landing'}
    }, 

    'Nursery': {
        'name': 'Nursery',

        'description': '\nThe nursery is an open room with toys scattered everywhere. There are toy soldiers lined up in marching formation; yo-yos, skipping ropes, and a rocking horse are left out and about. There is a small bed in the corner. To the south, you see an open door that leads to some sort of water closet.\n',

        'contents': {
          'Objects': {
            'name':'There is nothing for you to take here.',
            'room to use': 'You cannot use that item in this area.',
            'description':'N/A',
            'use checker':'false'
          }
        },

        'parler': {
          "name":"There is no one to talk to in this area."
        },

        'exits': {'west': 'Landing',
                  'south': 'Water Closet'}
    },

    "Housekeeper's Quarters": {
        'name': "Housekeeper's Quarters",

        'description': '\nThe stairway from the kitchen loops around the house into this room. It is sparsely furnished, so it is probably the quarters of a servant, maybe the housekeeper. There is an old worn cot made of wrought iron with a thin mattress and an even thinner woolen blanket. You are almost about to deem the room as useless to your investigation when you notice that one of the bedknobs screwed onto the posts of the bed seems loose. Could that be useful?\n',

        'contents': {
          'Objects': {
            'name': 'Bedknob',
            'description': '\nThe bedknob is made of iron. It is heavy, dark, and has a hole where you can screw it onto something.\n',
            'room to use': 'Water Closet',
            'action': '\nYou screw the bedknob onto the faucet next to the bathtub. It fits! You turn the bedknob, which acts as a handle, and water pours forth from the tap, filling the tub below. The room almost instantly fills with steam. Looking over at the mirror, you notice the word "Colonel" appear in a childish script. You wonder who had taken the time to write that? Obviously, you realize, it must have been the last person to use this bathroom.\n',
            'use checker':'false'
          }
          
        },

        'parler': {
          "name":"There is no one to talk to in this area."
        },

        'exits': {'north': 'Landing',
                  'down': 'Kitchen'}
    }
}

people = {
  'Housekeeper': {
    'name' : 'Housekeeper',
    'room' : 'Kitchen',
    'description': '\nA scowling, middle-aged woman stands in the corner, her attire signals that she is the Housekeeper. Time has done her no favors and her lined face, sullen eyes, and dumpy appearance make her rather off-putting.\n',
    'object':{
        'name' : 'Key',
        'type' : 'object',
        'description' : '\nThe key is a twisted bit of iron, sharp and jagged on one end. The other end is shaped into a rather unimaginative skull.\n',
        'action' : '\nYou use the key to open the old box. Inside, you find some folded sheets of parchment.\n'
      },
    'dialogue':'true'
  },

  'Mrs. Menteuse': {
    'name' : 'Mrs. Menteuse',
    'room' : 'Parlor',
    'description' : '\nMrs. Menteuse is a robust woman. She is not overly tall and nor heavily set, but there is strength in her gaze and perfect posture. She seems like the type of woman who always gets her way.\n',
    'dialogue': 'true'
  } ,
  
  'Little Boy': {
      'name': 'Little Boy',
      'room': 'Garden',
      'description': '\nThe young boy, who seems to share the same eyes as Mrs. Menteuse, is sitting over an ant hill holding some sort of magnifying device. He is rather pudgy and has an air of - similar to his mother, but more annoyingly - always getting his way.\n',
      'dialogue':'true',
      'object': {
        'name':'Decoder',
        'description': '\nThe decoder has two moveable rings around the edge with letters and symbols engraved onto them. In the middle, there is a magnifying glass.\n',
        'action': "You use the magnifying decoder to translate the words on the paper. The once impossible-to-read script becomes understandable. It appears to be a letter as it says: \n\n\nMy dearest Matilda, \nI fear that my wife has found out about us! She grows more unstable with every passing day. Her eyes follow me and it feels like being touched by the grave! Oh, Matilda! You must run! If my wife does know about us, no one is safe.\nYours, Charles Menteuse.\n\n"
      }
          
          },
}


# This function prints a nicely formatted,
# comma-separated list of the names
# of every item in the character's inventory.
# If the inventory is empty, it will print
# "Your inventory is empty" (or similar descriptive text.)
def print_inventory():
  # 🦄 Your code here!
  inventory_item_list = character['inventory']
  if not inventory_item_list:
    print("\nYour inventory is empty.\n")
  else:
    print("\n" + ', '.join(inventory_item_list)+ "\n")




# This function prints a nicely formatted
# comma-separated list of the names
# of every item in the current room.
# If the room has no items to pick up, it will print
# "There is nothing for you to take in this room."
# (or similar descriptive text.)
def list_room_items():
  # 🦄 Your code here!
  character_locations_items = character['location']

  objects_listed_here = []

  if not mansion[character_locations_items]['contents']:
    print("Items Readily Available: There is nothing for you to take here.\n")
  elif mansion[character_locations_items]['contents']['Objects']['name'] in character['inventory'] and mansion[character_locations_items]['contents']['Objects']['use checker'] == 'false':
    print("Items Readily Available: There is nothing for you to take here.\n")
  elif mansion[character_locations_items]['contents']['Objects']['use checker'] == "true":
    print("Items Readily Available: There is nothing for you to take here.\n")
  else:
    object_name_is = mansion[character_locations_items]['contents']['Objects']['name']
    objects_listed_here.append(object_name_is)
    print("Items Readily Available: " + ', '.join(objects_listed_here)+"\n")





# This function prints a nicely formatted
# comma-separated list of the exits
# in the current room.
# It should include the direction of the exit
# and the name of the room it leads to.
def list_room_exits():
  # 🦄 Your code here!
  character_locations_exit = character['location']
  
  exists_dictionary = mansion[character_locations_exit]['exits']

  exits_lists = []

  for key, value in exists_dictionary.items():
    ideas = key + ' - ' + value
    exits_lists.append(ideas)
    
  print("Exits: " + ', '.join(exits_lists) +"\n")




# This function takes one parameter: item_name.
# This function lets you take a single item
# if the user has specified the name of the item
# to take (for instance: "take spoon"). If
# the item the user specified is not in the room,
# it should print something like
# "There is no such item in this room."
# You could also take ALL of the items in the room
# if the user said "take all".
# If the user said "take all" but there are no
# items to take, it should print something like
# "There is nothing to take!"
def take_item(item_name):
  # 🦄 Your code here!
  character_take_item = character['location']

  if mansion[character_take_item]['contents']['Objects']['name'] == "There is nothing for you to take here.":

    print("\nThere are no items to take in this area.\n")

  elif item_name in mansion[character_take_item]['contents']['Objects']['name'] and mansion[character_take_item]['contents']['Objects']['use checker'] == 'false':

    print("\nYou have taken the " + item_name + ".\n")
    character['inventory'].append(item_name)
    mansion[character['location']]['contents']['Objects']['use checker'] = 'true'

  elif item_name == "all" and mansion[character_take_item]['contents']['Objects']['use checker'] == 'false':

    if mansion[character_take_item]['contents']['Objects']['name'] in character['inventory'] or mansion[character_take_item]['contents']["Objects"]["use checker"] == 'true':
      print("\nYou have already collected all of the items in this area.\n")
    else:
      print("\nYou have just collected all the items in this area.\n")
      character['inventory'].append(mansion[character_take_item]['contents']['Objects']['name'])
      mansion[character['location']]['contents']['Objects']['use checker'] = 'true'

  else:
    print("\nThere is or are no such item(s) in this area.\n")
  




# This function takes one parameter: item_name.
# It USES the item in your current room, if
# possible.
# You can only use the item if:
# 1) You have the item in your inventory.
# 2) You are in the correct room (that is, if
# the 'room to use' value matches the room you are
# currently in. You can only use the spoon in the kitchen,
# for example!
# If the item is in your inventory but you aren't in
# the correct room to use it, you should print something like
# "You can't use that item in this room."
# If you don't have that item in your inventory, you should
# print something like "You do not have that item in your inventory."
def use_item(item_name):
  # 🦄 Your code here!
  use_location = {}
  action = {}

  for k in mansion:
    use_location[mansion[k]['contents']['Objects']['name']] = mansion[k]['contents']['Objects']['room to use']

    if 'action' in mansion[k]['contents']['Objects']: 
      action[mansion[k]['contents']['Objects']['name']] = mansion[k]['contents']['Objects']['action']

  if item_name == "Decoder" and item_name in character['inventory']:
    if "Paper" in character['inventory']:
      print(people["Little Boy"]["object"]["action"])
      ending()
    else:
      print("\nYou do not have anything to use this decoder on.\n")

  elif item_name == "Key" and item_name in character['inventory']:
    if "Chest" in character['inventory']:
      print(mansion["Master Bedroom"]["contents"]["Objects"]["action"])
      character['inventory'].remove("Chest")
      character['inventory'].remove("Key")
      character['inventory'].append("Paper")
    else:
      print("\nYou do not have anything to use this key on.\n")

  elif item_name == "Paper" and item_name in character['inventory']:
    print("\nYou cannot use this item in any area.\n")
  elif item_name in character['inventory'] and character['location'] == use_location[item_name] and use_location[item_name] != "You cannot use that item in this area.":
    print(action[item_name] +"\n")
    character['inventory'].remove(item_name)

    if item_name == "Decanter":
      character['inventory'].append(people["Housekeeper"]["object"]["name"])
      people['Housekeeper']['dialogue'] = 'third'
    
    if item_name == "Soldier":
      print('\n"I will give you three guesses," the little boy says. "If you get them all wrong, you will just have to try again later!"\n')
      x = 0
      y = 0
      while x < 3:  
        print("Guess:")
        guess1 = input()
        if guess1 == "Colonel":
          print('\n"Good guess," the little boy remarks snidely. "I would normally just ignore you now, but Mother always goes on about the importance of being faithful. Maybe because Father was never faithful. Anyways, here you go." The little boy hands you the magnifying device. You want to comment on what the child just said, but find yourself focusing on the magnifying device instead. Upon closer inspection, you see that it appears to have moveable rings around the edge and looks like some sort of decoder.\n')
          character['inventory'].append(people['Little Boy']['object']['name'])
          x = 3
        else:
          if y < 2:
            print('\n"Wrong! Guess again!" the boy sneers.\n')
            y += 1
          else:
            print('\n"You got all three guesses wrong! Come back when you know the name of my toy soldier, and while you are at it, keep him safe! I cannot hold both the ant killer and my precious toy soldier at the same time!" the boy says as he hands the toy soldier back to you. He refocuses on the ants in front of him, returning to incinerating them one by one.\n')

            character['inventory'].append(mansion["Landing"]['contents']['Objects']['name'])
        x += 1    

  elif item_name in character['inventory'] and character['location'] != use_location[item_name]:
    print("\nYou cannot use that item in this area.\n")

  elif item_name not in character['inventory']:
    print("\nYou do not have that item in your inventory.\n")


def ending():
  print('\nIn your mind, the clues begin to add up.\n\n This letter...\n\n The words of the little boy when he said "Father was never faithful"...\n\n The housekeeper when she called the family "twisted"...\n\n It all pointed to something. But what?\n\n The letter! The letter gave a motive for the disappearance of Charles Menteuse. Obviously he had been having an affair and Mrs. Menteuse found out about it. He said that Mrs. Menteuse was irrational, so maybe she was the culprit all along.\n\n With this conclusion in mind, you decide to go and confront Mrs. Menteuse. However, a shuffling behind you draws your attention. Turning, you come face to face with Mrs. Menteuse! Her face is impassive and you feel a shiver go down your spine at the cold look in her eyes. \n\n"Ah... I see you found the letter," she remarks coldly. "I really should not have trusted the key with that useless housekeeper, or the decoder with my waste of space of a child." Her demeanor suddenly changes and her face splits into a wide manic grin. You take a small step back in fear. \n\n"Oh, do not worry, dear." Mrs. Menteuse continues to smile, "There is nothing to fear. You just know too much now. Luckily, I have the perfect solution." You want to speak, but fear grasps at your throat, physically holding the words in. \n\n"You, Inspector, I think, will find the rest of your stay with us most enjoyable." Suddenly, you feel a sharp pain at the back of your head and everything goes black. \n\n')

  sys.exit("Fin.")



# This function should print a nicely
# formatted list of all of the available commands,
# with corresponding descriptions of how they work.
def print_help():
  # 🦄 Your code here!
  print("\nnorth: move to the room to the north\nsouth: move to the room to the south\neast: move to the room to the east\nwest: move to the room to the west\nup: move up a set of stairs to the next level\ndown: move down a flight of stairs to the floor below\ndescription / d: gives a description of the room your in\ntake [item name/all] / t [item name/all]: add the item(s) to your inventory\nuse [item name] / u [item name]: uses the item to accomplish some task\nexamine [item name] / e [item name]: allows you to examine an item in your inventory\ninspect [name of person] / in [name of person]: allows you to inspect a person in a room \nconsult [name of person] / c [name of person]: allows you to give a user input to the specified person\ninventory / i: returns a list of what is in your inventory\nhelp / h: prints a list of all of the commands\nquit / q: exit the game\n\nNote: Capitalization matters!\n\n")




#Create a function to EXAMINE your item
def examine_item(item_name):
  
  examining = {}
  for naimer in mansion:
    examining[mansion[naimer]['contents']['Objects']['name']] = mansion[naimer]['contents']['Objects']['description']
  
  if item_name in character['inventory'] and item_name == "Key":
    print(people['Housekeeper']['object']['description'])
  elif item_name in character['inventory'] and item_name == "Decoder":
    print(people['Little Boy']['object']['description'])
  elif item_name == "Paper":
    print("\nUnfolding the piece of paper, you realize that there seem to be a bunch of illegible squiggles on it. If only you had some sort of decoder....")
  elif item_name in character['inventory']:
    print(examining[item_name] +"\n")



#function to print description of person
def inspect_person(item_name):
  if item_name == "Mrs. Menteuse" and character['location'] == people["Mrs. Menteuse"]['room']:
    print(people['Mrs. Menteuse']['description'])
  elif item_name == "Housekeeper" and character['location'] == people["Housekeeper"]['room']:
    print(people['Housekeeper']['description'])
  elif item_name == "Little Boy" and character['location'] == people['Little Boy']['room']:
    print(people['Little Boy']['description'])
  else:
    print("\nThere is no one by that name in this area.\n")




#list the people to talk to in each room
def list_room_people():
  if character['location'] == people["Mrs. Menteuse"]['room']:
    print("People: Mrs. Menteuse\n")
  elif character['location'] == people["Housekeeper"]['room']:
    print("People: Housekeeper\n")
  elif character['location'] == people["Little Boy"]['room']:
    print("People: Little Boy\n")
  else:
    print("People: There are no people to talk to in this area.\n")



def game_play_talking(item_name):
  if character['location'] == people["Mrs. Menteuse"]['room'] and item_name == "Mrs. Menteuse" or character['location'] == people['Housekeeper']['room'] and item_name == "Housekeeper" or character['location'] == people["Little Boy"]["room"] and item_name == "Little Boy":
    if item_name == "Mrs. Menteuse" and people['Mrs. Menteuse']['dialogue'] == 'true' and character['location'] == people['Mrs. Menteuse']['room']:
      print('\n"Ah! You must be the inspector from Scotland Yard, yes?" Mrs. Menteuse greets.\n')
      response = input()
      if response == "Yes" or response == "yes" or response == "y":
        print('\n"I am so grateful that you are here," Mrs. Menteuse states, "Everyone has just been so kind since my husband has disappeared. I am just so... grateful!"\n')
      elif response == "No" or response == "no" or response == 'n':
        print('\n"Who are you then?" she asks, eyes narrowing. "No, your uniform clearly tells me that you are an inspector."\n')
      else:
        print('\n"Hmm... What was that?" she asks questioninly.\n')
        
      print('\n"Well, anyways," Mrs. Menteuse continues, "I am sure that you would like to proceed with your investigation. Feel free to inspect the house. I will just leave you to it then." Mrs. Menteuse sits down and pulls out some needlework, leaving you to your investigation.\n')

      people["Mrs. Menteuse"]["dialogue"] = 'false'

    elif item_name == "Mrs. Menteuse" and people['Mrs. Menteuse']['dialogue'] == 'false':
      print('\nMrs. Menteuse glances us at you from her needlework, "I am just so grateful for Scotland Yard sending someone so soon! It has been so difficult, but one must always look for the bright things in life!" She refocuses on the needlework, leaving you to your investigation.\n')

    
    if item_name == "Housekeeper" and people["Housekeeper"]['dialogue'] == 'true' and character['location'] == people['Housekeeper']['room']:
      print('\n"Oi! You! Yeah, you!" the housekeeper snaps at you. "You from the Yard?"\n')
      responses = input()
      if responses == "Yes" or responses == "yes" or responses == "y":
        print('\n"Good. I have something for ya," the housekeeper sneers.\n')
      elif responses == "No" or responses == "no" or responses == "n":
        print('\n"Nah, I bet you are. Your uniform says it all," she declared, "But, either way, I have something for ya."\n')
      else:
        print('\n"Huh? What did you say?" the housekeeper questions sharply. "Nevermind, I have something for ya."\n')
      
      print('\n"Something that would help you, I bet, in this little investigation of yours. And you are going to need all the help in the world when dealing with this twisted family. However, nothing comes for free in this world. I am old and I like to ease my creaky bones with some good old fashioned liquid strength. Find me some of that and it will be worth your while," the housekeeper explains, her face contorting into a rather disturbing grin. "Now off you go." Her face settles back into its natural scowl and she directs her glare at anything and everything in the kitchen.\n')

      people["Housekeeper"]['dialogue'] = 'false'

    elif item_name == "Housekeeper" and people["Housekeeper"]['dialogue'] == 'false':
      print('\n"What are you doing dawdling round here?" the housekeeper asks sharply. "Get me that liquid luck and then we will talk." She turns to look off into the distance, not paying you any mind.\n') 
    
    elif item_name == "Housekeeper" and people["Housekeeper"]['dialogue'] == 'third':
      print('\nThe housekeeper barely spares you a glance. "Go!" she shoos you away, "I have no more need for you." With that she turns back to the decanter in her hands, admiring it in the dim light of the room.\n')
    

    if item_name == "Little Boy" and people["Little Boy"]['dialogue'] == 'true' and character['location'] == people['Little Boy']['room']:
      print('\n"You are the inspector Mother called round, right?" the little boys asks.\n')
      reprose = input()
      
      if reprose == "Yes" or reprose == "yes" or reprose == "y":
        print('\n"I knew it! Mother always says that I am the smartest person in the whole world!" the child grins smugly.\n')
      elif reprose == "No" or reprose == "no" or reprose == "n":
        print('\n"No! You are lying! I can tell by your uniform!" the child wildly waves his arms, pointing at you. "Mother always says that I am way smarter than my father. Father never would have been able to guess that you are an inspector. Father was dumb, Mother always said so."\n')
      else:
        print('\n"What did you say?" the little boy waves his hand, "Nevermind, I am sure that it was not all that important."\n')
      
      print('\nYour attention wanders from the brat in front of you to the object he holds in his chubby hands. It is the magnifying-glass-thing he was using to burn those poor ants to death. \n\nThe little boy notices what your eyes are focusing on and comments, "I see you are interested in my ant killer. Mother gave it to me for safe keeping, but I thought it would be much more useful to burn these little devils, they deserve it after all." You cannot help but unkindly think that it would be rather nice if someone would take a giant magnifying glass and burn the annoying little brat in front of you. \n\n"Well!" the boys exclaims, drawing you from your murderous ponderings, "It is mine. However, Mother always goes on about the importance of using people, so I will use you. I seem to have misplaced my toy soldier. Bring him to me! Actually, to make it even harder - because as Mother always says, you have to work hard for everything - you must also correctly name my toy soldier!" \n\nYou pause for a moment, a little stunned by the long speech the boy gave. He sneers at you, "What are you waiting for? I want my toy!" You take a step back, realizing that until you bring the toy to the boy, he will be of no more help to you.\n')

      people["Little Boy"]['dialogue'] = 'false'

    elif item_name == "Little Boy" and people["Little Boy"]["dialogue"] == 'false':
        print('\n"Bring me my toy!" the little boy yells at you before going back to burning those poor ants to death.\n')
  else:
    print("\nThere is no one by that name in this area to talk to.\n") 
   




# This code runs when the game first begins, before
# the first input prompt.
# The variable room contains the character's current location.
room = mansion[character['location']]
print(room['description'])
list_room_exits()
list_room_items()
list_room_people()

# this code continues to run until the game ends
# (that is, when you reach a 'break' statement)
while True:
    room = mansion[character['location']]
    # prompt should include the room's name
    command = input(room['name'] + ' > ')
    # split can have a MAX ELEMENTS parameter
    # https://www.w3schools.com/python/ref_string_split.asp
    command_parts = command.split(" ", 1)
    verb = command_parts[0]
    obj = command_parts[-1]

    if verb in ['east', 'west', 'north', 'south', 'up', 'down']:
        if verb in room['exits']:
            character['location'] = room['exits'][verb]
            room = mansion[character['location']]
            print(room['description'])
            list_room_exits()
            list_room_items()
            list_room_people()
        else:
            print('\nYou cannot go that way.\n')
    if verb == 'inventory' or verb == 'i':
        print_inventory()
    if verb == 'quit' or verb == 'q':
        print('\nYou have left the game.')
        break # we exit the loop and the game ends!
    if verb == 'take' or verb == 't':
        take_item(obj)
    if verb == 'd' or verb == 'description':
      print(room['description'])
      list_room_items()
      list_room_exits()
      list_room_people()
    if verb == 'help' or verb == 'h':
      print_help()
    if verb == 'use' or verb == 'u':
      use_item(obj)
    if verb == 'examine' or verb == 'e':
      examine_item(obj)
    if verb == "inspect" or verb == "in":
      inspect_person(obj)
    if verb == "consult" or verb == "c":
      game_play_talking(obj) 