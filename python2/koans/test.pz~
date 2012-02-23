#!/usr/bin/env python
# -*- coding: utf-8 -*-

def score(seq):
    # You need to write this method
    
    str_seq = []
    list_str = []
    result = 0

    if len(seq) == 0:
        return result
    
    else:

        for num in seq:
            
            print 'initial',num , seq, result
            
            if seq.count(num) == 3:
                if num == 1:
                    result += 1000
                    print 'after triple 1',num , seq, result
                else:
                    result +=  num * 100
                    print 'after triple n',num , seq, result

                for trash in range(1, 4):
                    seq.remove(num)
                    print'trash removal:', num , seq, result

        for index in range(0, len(seq)):
            if seq[index] == 1:
                result += 100

            elif seq[index] == 5:
                result += 50
  
  #          print 'final', num , seq, result
  #          print '*'*30 
            print 'index:', index , 'value:', seq[index]
    return result

class tester():
    print score([5])
    print '^' * 30
    print score([2,5,2,2,3])
    print '^' * 30
    print score([1,5,5,1])

    pass
