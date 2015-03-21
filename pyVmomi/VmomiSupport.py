import pyvmomi_to_ruby.or_list
import pyvmomi_to_ruby.formatter

F_LINK = pyvmomi_to_ruby.or_list.OrList(['link'])
F_LINKABLE = pyvmomi_to_ruby.or_list.OrList(['linkable'])
F_OPTIONAL = pyvmomi_to_ruby.or_list.OrList(['optional'])

def CreateDataType(a, b, c, d, e):
    if e is not None:
        e = [ list(x) for x in e ]
        for x in e:
            if x[-1] == 0:
                x.pop()

    print('    create_data_type("{a}", "{b}", "{c}", "{d}", {e})'.format(
        a=a,
        b=b,
        c=c,
        d=d,
        e=pyvmomi_to_ruby.formatter.format_value(e)))

def CreateManagedType(a, b, c, d, e, f):
    print('    create_managed_type("{a}", "{b}", "{c}", "{d}", {e}, {f})'.format(
        a=a,
        b=b,
        c=c,
        d=d,
        e=pyvmomi_to_ruby.formatter.format_value(e),
        f=pyvmomi_to_ruby.formatter.format_value(f)))

def CreateEnumType(a, b, c, d):
    print('    create_enum_type("{a}", "{b}", "{c}", {d})'.format(
        a=a,
        b=b,
        c=c,
        d=pyvmomi_to_ruby.formatter.format_value(d)))

def AddVersion(a, b, c, d, e):
    if d == 0:
        d = 'false'
    else:
        d = 'true'

    print('    add_version("{}", "{}", "{}", {}, "{}")'.format(
        a, b, c, d, e))

def AddVersionParent(a, b):
    print('    add_version_parent("{}", "{}")'.format(a, b))
