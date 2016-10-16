import pygame


class EventTimer:
    def __init__(self, event, time):
        self.event = event
        self.time = time

    def replace(self, event=None, time=None):
        if event is not None:
            self.event = event
        if time is not None:
            self.time = time

    def update(self, dt):
        self.time -= dt
        if self.time <= 0:
            pygame.event.post(self.event)


class CallTimer:
    def __init__(self, time, repeats, call, *args):
        self.time = [time, time]
        self.repeats = repeats
        self.call = call
        self.args = args

    def replace(self, time=None, call=None, *args):
        if time is not None:
            self.time = time
        if call is not None:
            self.call = call
            self.args = args

    def update(self, dt):
        if self.repeats == 0:
            return
        self.time[0] -= dt
        if self.time[0] <= 0:
            self.call(*self.args)
            if self.repeats < 0:
                self.time[0] = self.time[1]
            elif self.repeats > 0:
                self.repeats -= 1
                self.time[0] = self.time[1]


















