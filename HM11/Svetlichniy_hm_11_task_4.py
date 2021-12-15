def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("После локального присвоения:", spam)
    do_nonlocal()
    print("После nonlocal присвоения:", spam)
    do_global()
    print("После global присвоения:", spam)

scope_test()
print("В глобальной области видимости:", spam)