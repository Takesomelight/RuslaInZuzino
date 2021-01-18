from bearlibterminal import terminal

TITLE = "Rusla in Zuzino Adventure!"
W = 100 + 2 + 2
H = 80 + 2 + 2

def start_game():
    terminal.open()
    terminal.set("window: size=%dx%d, cellsize=8x8, title='%s'" % (W, H, TITLE))

    for x in range(W):
        terminal.put(x, 0, '#')
        terminal.put(x, H-1, '#')
        terminal.put(x, 1, '#')
        terminal.put(x, H-2, '#')
    for y in range(H):
        terminal.put(0, y, '#')
        terminal.put(W-1, y, '#')
        terminal.put(1, y, '#')
        terminal.put(W - 2, y, '#')

    terminal.refresh()
    while terminal.read() != terminal.TK_CLOSE:
        pass

    terminal.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
