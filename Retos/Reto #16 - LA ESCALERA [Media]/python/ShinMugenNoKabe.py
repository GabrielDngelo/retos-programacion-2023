def draw_ladder(steps: int):
    if steps == 0:
        print('__')
        return

    left_to_right = steps > 0
    range_step = -1 if left_to_right else 1

    # Imprimir último escalón
    if left_to_right:
        print(f"{'_' : >{(steps * 2) + 1}}")
    else:
        print('_')

    if left_to_right:
        for i in range(steps, 0, range_step):
            print(f"{'_|' : >{i * 2}}")
    else:
        for i in range(0, abs(steps), range_step):
            print(f"{'|_' : >{((i * 2) + 3)}}")


if __name__ == "__main__":
    draw_ladder(0)
    print("--------")
    draw_ladder(4)
    print("--------")
    draw_ladder(-7)