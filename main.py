from multiprocessing import Process, cpu_count

def check(n, iters, lastchecked):
    if n <= lastchecked:
        return [True, iters]
    if n == 1:
        return [True, iters]
    else:
        if n % 2 == 0:
            iters += 1
            return check(int(n / 2), iters, lastchecked)
        else:
            iters += 1
            return check(n * 3 + 1, iters, lastchecked)


def checkproc(chstart, chstop, checked):
    for i in range(chstart, chstop, 1):
        if not check(i, 0, checked):
            print('FALSE: ' + str(i))


def main():
    x = 1
    coef = 1000
    while True:
        intervals = []
        for i in range(1, cpu_count()):
            intervals.append(x + coef * i)
        procs = []
        for index, number in enumerate(intervals):
            proc = Process(target=checkproc(number - coef, number, x))
            procs.append(proc)
            proc.start()
            x += coef
        for pr in procs:
            pr.join()
        print('check all nums less than: ' + str(x))


if __name__ == '__main__':
    main()
