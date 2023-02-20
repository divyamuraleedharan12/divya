def clean(string):
    """ This function returns word with non-letters removed and 
    converts letters to lower case"""
    
    # remove non-ascii signs like the quotes in this text
    string = string.encode('ascii', 'ignore').decode()
    # convert to lower case
    string = string.lower()
    
    # now remove list of punctuation marks
    nonletters = [".", ",", ":", ";", "!", "?", "-", "(", ")", 
                  "/", "0", "1", "2", "3", "4", "5", 
                  "6", "7", "8", "9", ">", "<", "#", '"', "^", 
                  "=", "_", "[", "]", "%", "$", "@", "+", "|",
                  "*", "~", "&"]
    nonletters.append(chr(92))   # use ascii code for backslash
    nonletters.append(chr(35))   # and for double cross

    for nl in nonletters:
        string = string.replace(nl, '')
    
    return string


