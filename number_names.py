ones = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine', 10:'ten'}
teens = {11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
upper_tens = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

def number_name(num):
    name = ''
    mynum = num
    if mynum//1000000>0:
        name += number_name(mynum//1000000) + ' million'
        mynum%=1000
        if mynum > 0:
            name += ' '
    if mynum//1000>0:
        name += number_name(mynum//1000) + ' thousand'
        mynum%=1000
        if mynum > 0:
            name += ' '
    if mynum//100>0:
        name += number_name(mynum//100) + ' hundred'
        mynum%=100
        if mynum > 0:
            name += ' and '
    if mynum > 19:
        name += upper_tens[mynum//10]
        mynum%=10
        if mynum > 0:
            name += ' '
        if mynum > 0:
            name += ones[mynum]
    elif mynum > 10:
        name += teens[mynum]
    elif mynum > 0:
        name += ones[mynum]
    return name
