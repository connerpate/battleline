def test(*args):
    win = 0
    for x in args:
        win += 1
        print(win)
    if win > 0:
        print("You Win")
    else:
        print("You Lose")
