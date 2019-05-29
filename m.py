from fysom import FysomGlobalMixin, FysomGlobal, Fysom

class MyFysomGlobal(FysomGlobal):
    def _enter_state(self, obj, e):
        super()._enter_state(obj, e)
        print(f'{obj} entered {e.dst} state')


class Model(FysomGlobalMixin, object):
    GSM = FysomGlobal(
        events=[('warn',  'green',  'yellow'),
                {
                    'name': 'panic',
                    'src': ['green', 'yellow'],
                    'dst': 'red',
                    'cond': [  # can be function object or method name
                        'is_angry',  # by default target is "True"
                        {True: 'is_very_angry', 'else': 'yellow'}
                    ]
                },
                ('calm',  'red',    'yellow'),
                ('clear', 'yellow', 'green')],
        initial='green',
        final='red',
        state_field='state'
    )

    def __init__(self):
        self._state = None
        super(Model, self).__init__()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        print(f'new state: {value}')

    def is_angry(self, event):
        return True

    def is_very_angry(self, event):
        return False

    def __str__(self):
        return self.state


if __name__ == '__main__':

    obj = Model()
    obj2 = Model()
    obj.on_leave_green = lambda e: print(e)
    print(obj.current)  # 'green')
    print(obj2.current)
    obj.warn()
    obj.calm()
    print(obj.current)
    print(obj2.current)
    obj.is_state('yellow')  # True
    # conditions and conditional transition
    obj.panic()
    print(obj.current)  # 'yellow'
    obj.is_finished()  # False
