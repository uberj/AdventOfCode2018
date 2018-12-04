def build_sleeping_hours(input_):
    sleep_start = None
    g_num = None
    sleeping_hours = {}
    for line in input_:
        l, r = line.split("]")
        date, time = l.strip("[").split(" ")
        hour, minute = map(int, time.split(":"))
        r = r.strip()
        if r.startswith("Guard"):
            _, g_num = r.split("#")
            g_num = g_num.split(" ")[0]

        if r.startswith("falls asleep"):
            sleep_start = minute

        if r.startswith("wakes up"):
            for h in range(sleep_start, minute):
                assert g_num is not None
                sleeping_hours.setdefault(g_num, []).append(h)
    return sleeping_hours


class GuardWatch(object):
    def sort(self, input_):
        def sorter(line):
            l, r = line.split("]")
            date, time = l.strip("[").split(" ")
            return date+time
        return sorted(input_, key=sorter)

    def frequent_guard(self, input_):
        input_ = self.sort(input_)
        sleeping_hours = build_sleeping_hours(input_)

        common_hour_count = -1
        common_hour = None
        f_guard = None
        for g, hours_slept in sleeping_hours.items():
            for hour in hours_slept:
                hs = len(list(filter(lambda h: h == hour, hours_slept)))
                if hs > common_hour_count:
                    f_guard = g
                    common_hour_count = hs
                    common_hour = hour

        return f_guard, common_hour

    def best_guard(self, input_):
        input_ = self.sort(input_)
        sleeping_hours = build_sleeping_hours(input_)

        sleeps_the_most = None
        most_number_of_hours = -1
        best_hour = None
        most_hours_slept = -1
        for g, hours_slept in sleeping_hours.items():
            if len(hours_slept) >= most_hours_slept:
                most_hours_slept = len(hours_slept)
            else:
                continue

            for hour in hours_slept:
                hs = len(list(filter(lambda h: h == hour, hours_slept)))
                if hs <= 1:
                    continue

                if hs > most_number_of_hours:
                    most_number_of_hours = hs
                    best_hour = hour
                    sleeps_the_most = g

        return sleeps_the_most, best_hour


def challenge1():
    with open("inputs/gaurd-watch.txt", "r") as fd:
        bc = GuardWatch()
        g_num, hour = map(int, bc.best_guard(fd.readlines()))
        return g_num * hour


def challenge2():
    with open("inputs/gaurd-watch.txt", "r") as fd:
        bc = GuardWatch()
        g_num, hour = map(int, bc.frequent_guard(fd.readlines()))
        return g_num * hour


if __name__ == "__main__":
    print(challenge1())
    print(challenge2())
