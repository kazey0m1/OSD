import os


def check_is_split_line(line):
    return '-'*69 in line


# same_cn=0
diff = 0
err = 0
with open('./test.json', 'r+', encoding='utf-8') as cname_test:
    same = 0
    write = ''
    cname = []
    for line in cname_test:
        # err=0
        first = line.find('"')
        second = line.find('"', first+1)
        if line[-4:-1] == '"}]' and line.find('.', first, second) != -1:
            linelist = list(line)
            linelist.pop()
            linelist.append(',')
            write = ''.join(linelist)
        elif line.find('}}}') == -1:
            linelist = list(line)
            linelist.pop()
            write = ''.join(linelist)
        else:
            write = line
        print(write)
        with open('./test3.json', 'a', encoding='utf-8') as restest:
            restest.write(write+'\n')
        # print(str(first)+'+'+str(second))
            # cname_test.writelines(line)

    #     if not check_is_split_line(line):
    #         if(line.find(',')>0):
    #             continue
    #         cname.append(line)
    #         print(cname)

    #     else:
    #         for i in range(0,len(cname)-1):
    #             if(cname[i][-3:-1]!=cname[i+1][-3:-1]):
    #                 err+=1
    #         if(err!=0):
    #             diff+=1
    #         else:
    #              same+=1

    #         print('处理数据ing...')
    #         cname = []
    # print("解析后在同一区域的域名有："+str(same))
    # print("解析后不在同一区域的域名有："+str(diff))
