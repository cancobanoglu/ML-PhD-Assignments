from sklearn.tests.test_base import T

__author__ = 'cancobanoglu'
import numpy

VISA_RATIO = 0.3
FINAL_RATIO = 0.5
OPINION_NOTE_RATIO = 0.2

V1_NOTES = numpy.random.uniform(0, 100, size=5)
F1_NOTES = numpy.random.uniform(0, 100, size=5)

V2_NOTES = numpy.random.uniform(0, 100, size=5)
F2_NOTES = numpy.random.uniform(0, 100, size=5)

O_NOTES = numpy.random.uniform(0, 100, size=5)

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

print V1_NOTES_VECTOR