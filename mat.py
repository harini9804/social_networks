import numpy

A = numpy.mat('1 2;3 4')
v = numpy.mat('1 ; 1')
print v
print "###################"
for i in range(10):
    z = A *v
    z = z/numpy.linalg.norm(z)
    print z
    v = z
    print "****************"
