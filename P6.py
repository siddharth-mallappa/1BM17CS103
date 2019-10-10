def validate(inp):

        lst = []
        dict = {']' : '[', '}' : '{', ')': '('}
        for x in inp:
            if x in '({[':
                lst.append(x)
            elif x in ')}]':
                if dict[x] != lst.pop():
                    return 'Invalid'
        if len(lst) == 0:
            return 'Valid'
        return 'Invalid'

        



string1="{}{}{"
print(validate(string1))                

                 

               
