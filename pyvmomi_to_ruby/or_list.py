class OrList(list):

    def __or__(self, other):
        return OrList(self.__add__(other))

    def __str__(self):
        inner = ', '.join([ ':{} => true'.format(x) for x in self ])

        return '{{{}}}'.format(inner)
