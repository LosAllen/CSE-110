#Added a option do restart the sequence once.
#

adjective = input('Choose an adjective:')
animal = input('Choose an animal:')
exclamation = input('Choose an exclamation:')
verb1 = input('Choose a first verb:')
verb2 = input('Choose a second verb:')
verb3 = input('Choose a third verb:')

if adjective or animal or exclamation or verb1 or verb2 or verb3 == "restart" or "Restart": 
    adjective = input('Choose an adjective:')
    animal = input('Choose an animal:')
    exclamation = input('Choose an exclamation:')
    verb1 = input('Choose a first verb:')
    verb2 = input('Choose a second verb:')
    verb3 = input('Choose a third verb:')
    print('The other day, I was really in trouble. It all started when I saw a very')
    print(adjective, animal, verb1, 'down the hallway. "', exclamation, '"! I yelled. But all')
    print('I could think to do was to', verb2, ' over and over. Miraculously,')
    print('that caused it to stop, but not before it tried to ')
    print(verb3, ' right in front of my family.')
    
else:
    print('The other day, I was really in trouble. It all started when I saw a very')
    print(adjective, animal, verb1, 'down the hallway. "', exclamation, '"! I yelled. But all')
    print('I could think to do was to', verb2, ' over and over. Miraculously,')
    print('that caused it to stop, but not before it tried to ')
    print(verb3, ' right in front of my family.')
    