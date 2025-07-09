def isPalindrome(s: str) -> bool:
    """
    Leetcode problem #125

    Args:
        s (str): _description_

    Returns:
        bool: _description_
    """
    characters_to_remove = {
            ",":"", 
            ".":"",
            "!":"",
            " ":"",
            ":":"",
            "?":"",
            "'":"",
            '"':"",
            "(":"",
            ")":"",
            "[":"",
            "]":"",
            "-":"",
            "_":"",
            "@":"",
            "#":"",
            "%":"",
            "/":"",
            "<":"",
            "{":"",
            "}":"",
            ">":"",
            ";":"",
            "+":"",
            "=":"",
            "&":"",
            "^":"",
            "$":"",
            "\\":"",
            "|":"",
            "`":"",
            "~":""
    }
    
    s = s.lower()
    string = ""
    
    for chr in s:
        if chr not in characters_to_remove:
            string += chr

    left = 0
    right = len(string)
    length = len(string)
    
    for idx in range(length):
        left = idx
        right -= 1
        print(right)
        if string[left] != string[right]:
            return False
        if left == right:
            break
        
    return True

#str_input = "A man, a plan, a canal: Panama"
#str_input = "race a car"
str_input = " "
print(isPalindrome(str_input))