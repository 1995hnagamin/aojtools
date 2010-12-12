# coding: utf-8

import sys
import api

if len(sys.argv) < 2:
    print 'usage: %s problemid' % __file__
    os.exit()

def recursion(info, depth=0):
    for k,v in info:
        if k == "solved_list":
            print '  ' * depth + '- solved_list:'
            n = 5
            u = min(10, len(v.user))
            for i in xrange(u):
                if i % n == 0:
                    print '  ' * (depth+1),
                print v.user[i].id.ljust(10),
                if i % n == n-1 or i == u-1:
                    print ''
                if i == u-1 and u != len(v.user):
                    print '  ...(%d users)' % len(v.user)
            continue
        lst = [int, str, unicode]
        has = any(map(lambda cls: isinstance(v, cls), lst))
        print '%s%s %s' % ('  ' * depth, "+-"[has], k),
        if has:
            print '    ',v
        else:
            if isinstance(v, list):
                for item in v:
                    recursion(item, depth+1)
            else:
                print ''
                recursion(v, depth+1)

pid = sys.argv[1]
p = api.problem(pid)
recursion(p)
