def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    n=0
    while n<len(s):
        if s[n].isdigit():
            i=i+1
        n=n+1
    return i
print(main("python2023"))
<<<<<<< HEAD

=======
>>>>>>> 860089fd9b78dad1c61460d7b7f75df6338e70d9
