__author__ = 'cancobanoglu'
import numpy
import matplotlib.pyplot as plot

class DataSetGeneration:
    def __init__(self, count, v1_coeff, f1_coeff, k_coeff, v2_coeff, f2_coeff):
        self.total_count = count
        self.v1_c = v1_coeff
        self.v2_c = v2_coeff
        self.f1_c = f1_coeff
        self.f2_c = f2_coeff
        self.k_c = k_coeff

    def generate(self):
        V1_NOTES = numpy.random.random_integers(10, 100, size=self.total_count)
        F1_NOTES = numpy.random.random_integers(10, 100, size=self.total_count)

        V2_NOTES = numpy.random.random_integers(10, 100, size=self.total_count)
        F2_NOTES = numpy.random.random_integers(10, 100, size=self.total_count)

        K_NOTES = numpy.random.random_integers(10, 100, size=self.total_count)

        T1_NOTES = V1_NOTES * self.v1_c + F1_NOTES * self.f1_c + K_NOTES * self.k_c
        T2_NOTES = V2_NOTES * self.v2_c + F2_NOTES * self.f2_c + K_NOTES * self.k_c

        lesson_one = numpy.vstack((V1_NOTES, F1_NOTES, T1_NOTES)).T
        lesson_two = numpy.vstack((V2_NOTES, F2_NOTES, T2_NOTES)).T

        return [lesson_one, lesson_two]


class TwoDentridsLinearSinbad:
    def __init__(self, nu, init_ABar, init_v1_weight, init_v2_weight, init_f1_weight, init_f2_weight):
        self.nu = nu
        self.ABar = init_ABar
        self.v1_w = init_v1_weight
        self.v2_w = init_v2_weight
        self.f1_w = init_f1_weight
        self.f2_w = init_f2_weight
        self.RMSE_D1 = []
        self.RMSE_D2 = []

    def train(self, count, lesson_one, lesson_two, iterations=50):
        # predictions for lesson one
        Y1 = self.v1_w * lesson_one[:, 0] + self.f1_w * lesson_one[:, 1]
        # predictions for lesson two
        Y2 = self.v2_w * lesson_two[:, 0] + self.f2_w * lesson_two[:, 1]
        # run for RMSE_D1 and RMSE_D2
        self.RMSE_D1.append(self.RMSE(Y1, lesson_one[:, 2]))
        self.RMSE_D2.append(self.RMSE(Y2, lesson_two[:, 2]))

        beta = 0
        deviation = 0
        T = 0

        for _ in range(iterations):
            seq = numpy.random.random_integers(10, 99, size=count)
            for i in range(1, count):
                t = seq[i]

                Y1[t] = self.v1_w * lesson_one[:, 0][t] + self.f1_w * lesson_one[:, 1][t]
                self.v1_w = self.v1_w + self.nu * (lesson_one[:, 2][t] - Y1[t]) * lesson_one[:, 0][t]
                self.f1_w = self.f1_w + self.nu * (lesson_one[:, 2][t] - Y1[t]) * lesson_one[:, 1][t]

                Y2[t] = self.v2_w * lesson_two[:, 0][t] + self.f2_w * lesson_two[:, 1][t]
                self.v2_w = self.v2_w + self.nu * (lesson_two[:, 2][t] - Y2[t]) * lesson_two[:, 0][t]
                self.f2_w = self.f2_w + self.nu * (lesson_two[:, 2][t] - Y2[t]) * lesson_two[:, 1][t]

            D1 = self.RMSE(Y1, lesson_one[:, 2])
            D2 = self.RMSE(Y2, lesson_two[:, 2])

            self.RMSE_D1.append(D1)
            self.RMSE_D2.append(D2)

            # A = D1 + D2
            A = D1 + D2

            self.ABar = self.__A_Bar(A)

            deviation = self.__new_deviation(deviation, A, self.ABar)

            beta = 1 - 0.1 * deviation
            if beta < 0: beta = 0

            T = A - 0.1 * self.ABar + beta * (A - self.ABar)

            # E1 = T - 2 * D1
            # E2 = T - 2 * D2

        print "After training ---"
        print "Lesson 1 Vize W : " + str(self.v1_w)
        print "Lesson 1 Final W : " + str(self.f1_w)
        print "Lesson 2 Vize W : " + str(self.v2_w)
        print "Lesson 2 Final W : " + str(self.f2_w)

        plot.plot(self.RMSE_D1)
        plot.show()

    def RMSE(self, predictions, targets):
        return numpy.sqrt(numpy.mean(predictions - targets) ** 2)

    def __new_deviation(self, current_deviation, A, ABar):
        return current_deviation * 0.99 + numpy.abs(A - ABar) * 0.01

    def __A_Bar(self, A):
        return self.ABar * 0.99 + A * 0.01


d = DataSetGeneration(100, 0.2, 0.4, 0.4, 0.2, 0.4)
lesson_one, lesson_two = d.generate()

sinbad = TwoDentridsLinearSinbad(0.00005, 0, 0, 0, 0, 0)
sinbad.train(100, lesson_one, lesson_two, iterations=50)

