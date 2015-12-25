

__author__ = 'cancobanoglu'
import numpy

VISA_RATIO = 0.3
FINAL_RATIO = 0.5
OPINION_NOTE_RATIO = 0.2

V1_NOTES = numpy.random.random_integers(0, 100, size=5)
F1_NOTES = numpy.random.random_integers(0, 100, size=5)

V2_NOTES = numpy.random.random_integers(0, 100, size=5)
F2_NOTES = numpy.random.random_integers(0, 100, size=5)

O_NOTES = numpy.random.random_integers(0, 100, size=5)

T1_NOTES = V1_NOTES * VISA_RATIO + F1_NOTES * FINAL_RATIO + O_NOTES * OPINION_NOTE_RATIO
T2_NOTES = V2_NOTES * VISA_RATIO + F2_NOTES * FINAL_RATIO + O_NOTES * OPINION_NOTE_RATIO

print 'printing first lessons notes ...'
print 'visa 1 notes :' + str(V1_NOTES)
print 'final 1 notes : ' + str(F1_NOTES)
print 'opinion notes : ' + str(O_NOTES)
print 'total 1 notes : ' + str(T1_NOTES)

print 'printing second lessons notes ...'
print 'visa 2 notes : ' + str(V2_NOTES)
print 'final 2 notes : ' + str(F2_NOTES)
print 'opinion notes : ' + str(O_NOTES)
print 'total 2 notes :' + str(T2_NOTES)


V1_NOTES_VECTOR = numpy.reshape(V1_NOTES, (5,1))
F1_NOTEST_VECTOR = numpy.reshape(F1_NOTES, (5,1))
T1_NOTEST_VECTOR = numpy.reshape(T1_NOTES, (5,1))
V2_NOTES_VECTOR = numpy.reshape(V2_NOTES, (5,1))
F2_NOTEST_VECTOR = numpy.reshape(F2_NOTES, (5,1))
T2_NOTEST_VECTOR = numpy.reshape(T2_NOTES, (5,1))

lesson_one = numpy.vstack((V1_NOTES,F1_NOTES,T1_NOTES)).T
lesson_two = numpy.vstack((V2_NOTES,F2_NOTES,T2_NOTES)).T

print lesson_one
