
class TimeDefiner:
    def __init__(self):
        self.times = []
        self.point_count = 10
        self.currnet_step = 0

    def get_next_wait_time(self, current_time):
        self.times.append(current_time)
        return self.__get_next_wait_time()

    def __get_next_wait_time(self):
        times = self.times[::-1][:self.point_count][::-1]

        differents = []
        for i in range(len(times)-1):
            differents.append(times[i+1] - times[i])

        differents.reverse()
        common_different = 0
        for index, different in enumerate(differents):
            common_different += different/((index+1)**2)

        return self.times[-1] + common_different
