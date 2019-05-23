#!/usr/bin/python
#_*_ coding: UTF-8 _*_
# python3.6

import visa,time
inst = visa.ResourceManager()
dp711 = inst.open_resource('ASRL3::INSTR')


#initialize...

print('\nStart the test:\n')
print('Connecting the dp711 Power Supply\n')

dp711.write('*IDN?')
dp711.read()
dp711.write(':APPLy CH1,10,0.01')


#setting test time
N = 10
PowerOnTime = 3
PowerOffTime = 3
SleepTime = 2

#open test file
with open('ceshi.txt','a') as fp:
    fp.write('New test is started on %s \n'% time.ctime())


print ('Test is start @ %s' % time.ctime())
for i in range(N):
    print('\n')
    print('Cycle %d:' %(i))
    dp711.write(':APPLy CH1,5,0.5')
    dp711.write(':OUTP ON')
    print('Power ON')
    time.sleep(PowerOnTime)
    dp711.write(':OUTP OFF')
    print('Power OFF\r')
    time.sleep(PowerOffTime)
    with open('ceshi.txt','a') as fp:
        fp.write('Completed Cycle %d:\r\n' %(i))

dp711.write(':APPLy CH1,10,1')
time.sleep(0.1)
dp711.close()

print('Test is completed @ {}\n'.format(time.ctime()))
with open('ceshi.txt','a') as fp:
    fp.write('Test is completed on {}'.format(time.ctime()))
