def data_type(arg):
    value = 'no value'
    if type(arg) == str:
        value = len(arg)

    elif type(arg) == None:
        value = 'no value'

    elif type(arg) == bool:
        value = arg

    elif type(arg) == int:
        if arg > 100:
            value = 'more than 100'

        elif arg == 100:
            value = 'equal to 100'

        elif arg < 100:
            value = 'less than 100'

    elif type(arg) == list:
        if len(arg) >= 3:
            value = arg[2]
        else:
            value = None

    return value
