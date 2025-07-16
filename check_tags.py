def check_tags(text):
    """Check for appropriate closing of opening tags: ([{<>}])
       Return 'OK' if all closings match openings
       Return 'CORRUPTED' if more than 1 error
       Return the right closing tag if only one error
    Args:
        text (_type_): the text to check
    """
    tags = {"{": "}", "<": ">", "[": "]", "(": ")"}
    openings = []
    fix_suggestion = ""
    for index, char in enumerate(text):
        if char in tags: # char is an opener
            openings.append(char)
        if char in tags.values(): # char is a closer
            if tags[openings[-1]] == char: # correct closing
                openings.pop()
            else: 
                if not fix_suggestion:
                    fix_suggestion = tags[openings[-1]]
                else:
                    return "CORRUPTED"
    if len(openings) == 1:
        if not fix_suggestion:
            return tags[openings[-1]]
        else:
            return "CORRUPTED"
    if len(openings) == 0:
        return "OK"
    return "CORRUPTED"


print("lkjmlkjmkjfzaf:", check_tags("lkjmlkjmkjfzaf"))
print("lkjmlkjmkj[fzaf:", check_tags("lkjmlkjmkj[fzaf"))
print("lkjmlkjmkj[fza]f:", check_tags("lkjmlkjmkj[fza]f"))
print("lkjml{}kjmkj[fza]f:", check_tags("lkjml{}kjmkj[fza]f"))
print("lkjml<k(j)mkj[fza]f:", check_tags("lkjml<k(j)mkj[fza]f"))
print("lkjml<k(j)[mkj[fza]f:", check_tags("lkjml<k(j)[mkj[fza]f"))