import or_list

def format_value(v):
    if v is None:
        return 'nil'
    elif type(v) is or_list.OrList:
        return str(v)
    elif type(v) is list or type(v) is tuple:
        return format_list(v)
    elif type(v) is int:
        return '{}'.format(v)
    else:
        return '"{}"'.format(v)

def format_list(alist):
    inner = ', '.join([ format_value(v) for v in alist ])

    return '[{}]'.format(inner)
