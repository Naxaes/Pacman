# class Foo(object):
#     def __init__(self, **kwargs):
#         self._state = kwargs
#
#     @property
#     def state(self):
#         for name, is_true in self._state.items():
#             if is_true:
#                 return name
#
#     @state.setter
#     def state(self, state):
#         for i in self._state:
#             if i == state:
#                 self._state[i] = True
#             else:
#                 self._state[i] = False
#
#
# import pygame
# pygame.init()
#
# screen = pygame.display.set_mode((100, 100))
# clock = pygame.time.Clock()
#
# while True:
#     clock.tick(60)
#
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONUP:
#             start = event.pos
#             print("start", start)
#         elif event.type == pygame.QUIT:
#             quit()
#
#     pygame.display.update()
#
#
# try:
#     import tkinter as tk  # Python 3
# except ImportError:
#     import Tkinter as tk  # Python 2
#
# root = tk.Tk()
#
# def print_pos(event):
#     print(event.x, event.y)
#
# root.bind("<Button-1>", print_pos)
# root.mainloop()


