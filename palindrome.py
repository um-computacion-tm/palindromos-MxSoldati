class Palindrome():
    def is_palindrome(string):
        str = string.replace(' ','').lower()
        if str == str[::-1]:
            return True
        return False
