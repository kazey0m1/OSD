import json
import requests
import dns.resolver
import subprocess
def dig(domainname):
    a,result=subprocess.getstatusoutput('dig '+domainname)
    answer=';; ANSWER SECTION:'
    if not answer in result:
        name=result[result.find('SOA')+4:result.find('. ')+1]
        b,result=subprocess.getstatusoutput('dig '+name)
    try:
        ans_sec=result.split(answer,1)[1].splitlines()[1]
    except:
        name=result[result.find('SOA')+4:result.find('. ')+1]
        b,result=subprocess.getstatusoutput('dig '+name)
        ans_sec=result.split(answer,1)[1].splitlines()[1]
    IP=ans_sec[ans_sec.find('A')+2:]
    return IP

def getData(IP):
    url="http://ip.taobao.com/service/getIpInfo.php?ip="+IP#locals()['cname'+str(i)]
    headers = {'content-type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    try:
        r=requests.get(url,headers=headers,timeout=1)
        data=r.text[r.text.find(':{')+1:-2]
        if r.status_code==404:
            data=getData(IP)
        if r.status_code==502:
            data=getData(IP)
        if not 'ip' in data:
            data=getData(IP)
    except:
        data=getData(IP)
    
    return data

filename='./test.json'
with open('./part_00.json.json','r') as cname_test:
    for line in cname_test:
        cname_dict=json.loads(line)
        domain=cname_dict['name'] #get domain_name

        ##取出name,写入json
        cname1=domain
        with open(filename,'a') as write:
            write.write('{"'+domain+'":{"subDomain":{\n')
        for i in range(2,domain.count('.')+2):
            locals()['cname'+str(i)]=locals()['cname'+str(i-1)][locals()['cname'+str(i-1)].find('.')+1:]

            #locals()['cname'+str(i)]=domain_list[i-1]
        for i in range(1,domain.count('.')+2):
            #取域名的IP
            print(locals()['cname'+str(i)])
            domain=locals()['cname'+str(i)]
            with open(filename,'a') as write:
                write.write(' "'+domain+'":[')            
            try:
                A=dns.resolver.query(domain,'A')
                for i in A.response.answer:   # 通过response.answer方法获取查询IP
                    for j in i.items:    
                        if j.rdtype == 1: 
                            IP=j.address   # 避免 "AttributeError: 'CNAME' object has no attribute 'address'" 错误
                            data=getData(IP)

                        #     url="http://ip.taobao.com/service/getIpInfo.php?ip="+IP#locals()['cname'+str(i)]
                        #     headers = {'content-type': 'application/json',
                        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
                        #     r=requests.get(url,headers=headers,timeout=0.5)
                        #     print(json.loads(r.json))
                            with open(filename,'a') as write:
                                write.write(data+']\n') 
                        else:
                            pass
                    
           
            except:
                IP=dig(domain)
                
            #     url="http://ip.taobao.com/service/getIpInfo.php?ip="+IP#locals()['cname'+str(i)]
            #     headers = {'content-type': 'application/json',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
            #     r=requests.get(url,headers=headers,timeout=1)
            #     print(r.text)
                data=getData(IP)
                with open(filename,'a') as write:
                    write.write(data+']\n') 
        with open(filename,'a') as write:
            write.write('}}}\n')    
        #     s=locals()['cname'+str(i)]+" "+r.text[-2:]
        #     #print()

        #     with open(filename,'a') as write:
        #         write.writelines(s)
        #         write.writelines('\n')
        # with open(filename,'a') as write:
        #         write.writelines('---------------------------------------------------------------------')
        #         write.writelines('\n')
            #print(locals()['cname'+str(i)])
        #cname2=cname1[cname1.find('.')+1:len(cname1)]
        #print(cname1,cname2)
        #print(cname2)