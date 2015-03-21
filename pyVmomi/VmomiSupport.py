import sys

import pyvmomi_to_ruby.or_list
import pyvmomi_to_ruby.formatter

F_LINK = pyvmomi_to_ruby.or_list.OrList(['link'])
F_LINKABLE = pyvmomi_to_ruby.or_list.OrList(['linkable'])
F_OPTIONAL = pyvmomi_to_ruby.or_list.OrList(['optional'])

def CreateDataType(a, b, c, d, e, out=sys.stdout):
    if e is not None:
        e = [ list(x) for x in e ]
        for x in e:
            if x[-1] == 0:
                x.pop()

    out.write('    create_data_type("{a}", "{b}", "{c}", "{d}", {e})\n'.format(
        a=a,
        b=b,
        c=c,
        d=d,
        e=pyvmomi_to_ruby.formatter.format_value(e)))

def CreateManagedType(a, b, c, d, e, f, out=sys.stdout):
    out.write('    create_managed_type("{a}", "{b}", "{c}", "{d}", {e}, {f})\n'.format(
        a=a,
        b=b,
        c=c,
        d=d,
        e=pyvmomi_to_ruby.formatter.format_value(e),
        f=pyvmomi_to_ruby.formatter.format_value(f)))

def CreateEnumType(a, b, c, d, out=sys.stdout):
    out.write('    create_enum_type("{a}", "{b}", "{c}", {d})\n'.format(
        a=a,
        b=b,
        c=c,
        d=pyvmomi_to_ruby.formatter.format_value(d)))

def AddVersion(a, b, c, d, e, out=sys.stdout):
    if d == 0:
        d = 'false'
    else:
        d = 'true'

    out.write('    add_version("{0}", "{1}", "{2}", {3}, "{4}")\n'.format(
        a, b, c, d, e))

def AddVersionParent(a, b, out=sys.stdout):
    out.write('    add_version_parent("{0}", "{1}")\n'.format(a, b))
