import sys
from creator import Creator

def run():
    """ run the script """
    args = sys.argv
    if len(args) < 2:
        print( "Not enough arguments" )
    else:
        action = args[1]
        entity_type = args[2]
        if action == "create":
            creator = Creator()
            creator.create_entities(entity_type)

run()