import sys


def yesno(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        reply0 = raw_input(prompt)
        if reply0.lower()[0]=="y":
            return True
        if reply0.lower()[0]=="n":
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint



