import sys
import yesno

def youenter(item_title, prompt):
    while True:
        if(yesno.yesno("You have Entered %s. Is this correct? (Y/N)" % item_title)):
            break
        else:
            item_title = raw_input (prompt)



