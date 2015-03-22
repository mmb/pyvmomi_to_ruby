from . import or_list

def format_value(v):
    if v is None:
        return 'nil'
    elif type(v) is or_list.OrList:
        return str(v)
    elif type(v) is list or type(v) is tuple:
        return format_list(v)
    elif type(v) is int:
        return '{0}'.format(v)
    else:
        return '"{0}"'.format(v)

def format_list(alist):
    inner = ', '.join([ format_value(v) for v in alist ])

    return '[{0}]'.format(inner)

def format_data_type_fields(fields):
    if fields is None:
        result = None
    else:
        result = []

        for field in fields:
            new_field = list(field)
            if new_field[-1] == 0:
                new_field.pop()
            result.append(new_field)

    return result
