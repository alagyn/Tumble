from tumble import Tumble


if __name__ == '__main__':
    tbl = Tumble(("The First", 10, "d"),
                 ("Second", 3, ".2f"),
                 ("Third", 6, "s"),
                 align=">")

    for x in range(10):
        tbl.print_row(x, x * 0.2, f'asdf{x}')
