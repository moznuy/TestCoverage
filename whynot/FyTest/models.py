from django.db import models
from fysom import FysomGlobalMixin, FysomGlobal

# Create your models here.
class TestMachine(FysomGlobalMixin, models.Model):
    GSM = FysomGlobal(
        events=[
            ('key_put',  'idle',  'engine_starting'),
            ('key_turn', 'engine_starting', 'stopped'),
            ('pedal_gas', 'stopped', 'moving'),
            ('pedal_stop', ['moving', 'stopped'], 'stopped'),
            ('key_out', 'stopped', 'idle'),
        ],
        initial='idle',
        state_field='state',
    )

    state = models.CharField(max_length=128)


    def on_enter_stopped(self, e):
        print(f"{self} stopped. Ready to move")

    def __str__(self):
        return f'Car "{self.state}" state'
