#!/usr/bin/python3
v=25
u=0
t=10

print('We have,\nv = {} m/s\nu = {} m/s\nt = {} s'.format(v,u,t))

print('acceleration(a)=?\nNow,\n   v = u + at\n=> a = (v-u) / t')

acc=(v-u)/t
print('     = ({}-{}) / {}\n     = {}'.format(v,u,t,acc))

print('\nHence, acceleration = {} m/s\u00b2.'.format(acc))

